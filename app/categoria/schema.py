from sqlmodel import SQLModel


class CategoriaCreate(SQLModel):
    nombre: str
    descripcion: str


class CategoriaUpdate(SQLModel):
    nombre: str | None = None
    descripcion: str | None = None


class CategoriaResponse(SQLModel):
    id: int
    nombre: str
    descripcion: str