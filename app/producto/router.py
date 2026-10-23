
from fastapi import APIRouter, Depends, HTTPException, status
from sqlmodel import Session

from app.core.database import get_session
from app.producto.schema import (
    ProductoCreate,
    ProductoUpdate,
    ProductoResponse
)
from app.producto import service


router = APIRouter(
    prefix="/productos",
    tags=["Productos"]
)


@router.get("/", response_model=list[ProductoResponse])
def listar_productos(
    session: Session = Depends(get_session)
):
    return service.obtener_productos(session)


@router.get("/{producto_id}", response_model=ProductoResponse)
def buscar_producto(
    producto_id: int,
    session: Session = Depends(get_session)
):
    producto = service.obtener_producto(session, producto_id)

    if producto is None:
        raise HTTPException(
            status_code=404,
            detail="Producto no encontrado"
        )

    return producto


@router.post(
    "/",
    response_model=ProductoResponse,
    status_code=status.HTTP_201_CREATED
)
def crear_producto(
    datos: ProductoCreate,
    session: Session = Depends(get_session)
):
    return service.crear_producto(session, datos)


@router.put("/{producto_id}", response_model=ProductoResponse)
def actualizar_producto(
    producto_id: int,
    datos: ProductoUpdate,
    session: Session = Depends(get_session)
):
    producto = service.actualizar_producto(
        session,
        producto_id,
        datos
    )

    if producto is None:
        raise HTTPException(
            status_code=404,
            detail="Producto no encontrado"
        )

    return producto


@router.delete("/{producto_id}")
def eliminar_producto(
    producto_id: int,
    session: Session = Depends(get_session)
):
    eliminado = service.eliminar_producto(
        session,
        producto_id
    )

    if not eliminado:
        raise HTTPException(
            status_code=404,
            detail="Producto no encontrado"
        )

    return {"mensaje": "Producto eliminado correctamente"}
