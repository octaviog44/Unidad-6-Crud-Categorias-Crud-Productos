
from fastapi import APIRouter, Depends, HTTPException, status
from sqlmodel import Session

from app.core.database import get_session
from app.categoria.schema import (
    CategoriaCreate,
    CategoriaUpdate,
    CategoriaResponse
)
from app.categoria import service


router = APIRouter(
    prefix="/categorias",
    tags=["Categorias"]
)


@router.get("/", response_model=list[CategoriaResponse])
def listar_categorias(
    session: Session = Depends(get_session)
):
    return service.obtener_categorias(session)


@router.get("/{categoria_id}", response_model=CategoriaResponse)
def buscar_categoria(
    categoria_id: int,
    session: Session = Depends(get_session)
):
    categoria = service.obtener_categoria(session, categoria_id)

    if categoria is None:
        raise HTTPException(
            status_code=404,
            detail="Categoria no encontrada"
        )

    return categoria


@router.post(
    "/",
    response_model=CategoriaResponse,
    status_code=status.HTTP_201_CREATED
)
def crear_categoria(
    datos: CategoriaCreate,
    session: Session = Depends(get_session)
):
    return service.crear_categoria(session, datos)


@router.put("/{categoria_id}", response_model=CategoriaResponse)
def actualizar_categoria(
    categoria_id: int,
    datos: CategoriaUpdate,
    session: Session = Depends(get_session)
):
    categoria = service.actualizar_categoria(
        session,
        categoria_id,
        datos
    )

    if categoria is None:
        raise HTTPException(
            status_code=404,
            detail="Categoria no encontrada"
        )

    return categoria


@router.delete("/{categoria_id}")
def eliminar_categoria(
    categoria_id: int,
    session: Session = Depends(get_session)
):
    eliminado = service.eliminar_categoria(
        session,
        categoria_id
    )

    if not eliminado:
        raise HTTPException(
            status_code=404,
            detail="Categoria no encontrada"
        )

    return {"mensaje": "Categoria eliminada correctamente"}
