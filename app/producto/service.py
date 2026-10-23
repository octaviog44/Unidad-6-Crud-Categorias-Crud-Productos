
from sqlmodel import Session, select
from fastapi import HTTPException

from app.producto.model import Producto
from app.producto.schema import ProductoCreate, ProductoUpdate

from app.categoria.model import Categoria
from app.producto.model import ProductoCategoria
from app.producto.schema import ProductoCategoriaCreate


def obtener_productos(session: Session):
    statement = select(Producto)
    return session.exec(statement).all()


def obtener_producto(session: Session, producto_id: int):
    return session.get(Producto, producto_id)


def crear_producto(session: Session, datos: ProductoCreate):
    # Verificar si ya existe un producto con ese nombre
    statement = select(Producto).where(
        Producto.nombre == datos.nombre
    )

    producto_existente = session.exec(statement).first()

    if producto_existente:
        raise HTTPException(
            status_code=409,
            detail="Ya existe un producto con ese nombre"
        )

    producto = Producto.model_validate(datos)

    session.add(producto)
    session.commit()
    session.refresh(producto)

    return producto


def actualizar_producto(
    session: Session,
    producto_id: int,
    datos: ProductoUpdate
):
    producto = session.get(Producto, producto_id)

    if producto is None:
        return None

    datos_actualizados = datos.model_dump(exclude_unset=True)

    # Verificar que el nombre no pertenezca a otro producto
    if "nombre" in datos_actualizados:
        statement = select(Producto).where(
            Producto.nombre == datos_actualizados["nombre"],
            Producto.id != producto_id
        )

        producto_existente = session.exec(statement).first()

        if producto_existente:
            raise HTTPException(
                status_code=409,
                detail="Ya existe otro producto con ese nombre"
            )

    producto.sqlmodel_update(datos_actualizados)

    session.add(producto)
    session.commit()
    session.refresh(producto)

    return producto


def eliminar_producto(session: Session, producto_id: int):
    producto = session.get(Producto, producto_id)

    if producto is None:
        return False

    session.delete(producto)
    session.commit()

    return True





def obtener_relaciones(session: Session):
    statement = select(ProductoCategoria)
    return session.exec(statement).all()


def crear_relacion(
    session: Session,
    datos: ProductoCategoriaCreate
):
    producto = session.get(Producto, datos.producto_id)
    if producto is None:
        raise HTTPException(
            status_code=404,
            detail="Producto no encontrado"
        )

    categoria = session.get(Categoria, datos.categoria_id)
    if categoria is None:
        raise HTTPException(
            status_code=404,
            detail="Categoria no encontrada"
        )

    relacion_existente = session.get(
        ProductoCategoria,
        (datos.producto_id, datos.categoria_id)
    )

    if relacion_existente:
        raise HTTPException(
            status_code=409,
            detail="El producto ya esta asociado a esa categoria"
        )

    relacion = ProductoCategoria.model_validate(datos)
    session.add(relacion)
    session.commit()
    session.refresh(relacion)

    return relacion


def eliminar_relacion(
    session: Session,
    producto_id: int,
    categoria_id: int
):
    relacion = session.get(
        ProductoCategoria,
        (producto_id, categoria_id)
    )

    if relacion is None:
        return False

    session.delete(relacion)
    session.commit()

    return True