from sqlmodel import SQLModel, Field
from sqlalchemy import Column, JSON


class ProductoCategoria(SQLModel, table=True):
    producto_id: int = Field(
        foreign_key="producto.id",
        primary_key=True
    )

    categoria_id: int = Field(
        foreign_key="categoria.id",
        primary_key=True
    )


class Producto(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)

    nombre: str = Field(index=True, unique=True)
    descripcion: str
    precio_base: str

    imagen_url: list[str] = Field(
        default_factory=list,
        sa_column=Column(JSON)
    )

    disponible: bool = True