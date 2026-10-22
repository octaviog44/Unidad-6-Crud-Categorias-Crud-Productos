from sqlmodel import SQLModel, Field


class ProductoCreate(SQLModel):
    nombre: str
    descripcion: str
    precio_base: str
    imagen_url: list[str] = Field(default_factory=list)
    disponible: bool = True


class ProductoUpdate(SQLModel):
    nombre: str | None = None
    descripcion: str | None = None
    precio_base: str | None = None
    imagen_url: list[str] | None = None
    disponible: bool | None = None


class ProductoResponse(SQLModel):
    id: int
    nombre: str
    descripcion: str
    precio_base: str
    imagen_url: list[str]
    disponible: bool


class ProductoCategoriaCreate(SQLModel):
    producto_id: int
    categoria_id: int


class ProductoCategoriaResponse(SQLModel):
    producto_id: int
    categoria_id: int