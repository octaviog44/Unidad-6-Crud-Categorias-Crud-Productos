
from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.core.database import crear_tablas
from app.categoria.router import router as categoria_router
from app.producto.router import router as producto_router
from app.producto_categoria_router import router as producto_categoria_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    crear_tablas()
    yield


app = FastAPI(
    title="API de Categorias y Productos",
    description="Trabajo Practico Unidad 6 - Programacion IV",
    version="1.0.0",
    lifespan=lifespan
)


app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)


app.include_router(categoria_router)
app.include_router(producto_router)
app.include_router(producto_categoria_router)

@app.get("/")
def inicio():
    return {
        "mensaje": "API de Categorias y Productos funcionando"
    }
