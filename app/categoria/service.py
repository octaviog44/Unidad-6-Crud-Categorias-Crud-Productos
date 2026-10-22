
from sqlmodel import Session, select
from fastapi import HTTPException

from app.categoria.model import Categoria
from app.categoria.schema import CategoriaCreate, CategoriaUpdate


def obtener_categorias(session: Session):
    statement = select(Categoria)
    return session.exec(statement).all()


def obtener_categoria(session: Session, categoria_id: int):
    return session.get(Categoria, categoria_id)


def crear_categoria(session: Session, datos: CategoriaCreate):

    # Verificar si ya existe una categoria con ese nombre
    statement = select(Categoria).where(
        Categoria.nombre == datos.nombre
    )

    categoria_existente = session.exec(statement).first()

    if categoria_existente:
        raise HTTPException(
            status_code=409,
            detail="Ya existe una categoria con ese nombre"
        )

    categoria = Categoria.model_validate(datos)

    session.add(categoria)
    session.commit()
    session.refresh(categoria)

    return categoria


def actualizar_categoria(
    session: Session,
    categoria_id: int,
    datos: CategoriaUpdate
):
    categoria = session.get(Categoria, categoria_id)

    if categoria is None:
        return None

    datos_actualizados = datos.model_dump(exclude_unset=True)

    # Verificar que el nuevo nombre no pertenezca a otra categoria
    if "nombre" in datos_actualizados:
        statement = select(Categoria).where(
            Categoria.nombre == datos_actualizados["nombre"],
            Categoria.id != categoria_id
        )

        categoria_existente = session.exec(statement).first()

        if categoria_existente:
            raise HTTPException(
                status_code=409,
                detail="Ya existe otra categoria con ese nombre"
            )

    categoria.sqlmodel_update(datos_actualizados)

    session.add(categoria)
    session.commit()
    session.refresh(categoria)

    return categoria


def eliminar_categoria(session: Session, categoria_id: int):
    categoria = session.get(Categoria, categoria_id)

    if categoria is None:
        return False

    session.delete(categoria)
    session.commit()

    return True
