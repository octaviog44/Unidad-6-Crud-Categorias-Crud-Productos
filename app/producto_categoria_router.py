from fastapi import APIRouter, Depends, HTTPException, status
from sqlmodel import Session

from app.core.database import get_session
from app.producto.schema import (
    ProductoCategoriaCreate,
    ProductoCategoriaResponse
)
from app.producto import service

router = APIRouter(
    prefix="/producto-categoria",
    tags=["ProductoCategoria"]
)


@router.get(
    "/",
    response_model=list[ProductoCategoriaResponse]
)
def listar_relaciones(
    session: Session = Depends(get_session)
):
    return service.obtener_relaciones(session)


@router.post(
    "/",
    response_model=ProductoCategoriaResponse,
    status_code=status.HTTP_201_CREATED
)
def crear_relacion(
    datos: ProductoCategoriaCreate,
    session: Session = Depends(get_session)
):
    return service.crear_relacion(session, datos)


@router.delete("/{producto_id}/{categoria_id}")
def eliminar_relacion(
    producto_id: int,
    categoria_id: int,
    session: Session = Depends(get_session)
):
    eliminado = service.eliminar_relacion(
        session,
        producto_id,
        categoria_id
    )

    if not eliminado:
        raise HTTPException(
            status_code=404,
            detail="Relacion no encontrada"
        )

    return {"mensaje": "Relacion eliminada correctamente"}