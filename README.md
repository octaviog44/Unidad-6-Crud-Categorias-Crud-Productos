# API de Categorías y Productos

Trabajo práctico de la Unidad 6 de Programación IV.

## Descripción

API REST desarrollada con FastAPI y SQLModel para administrar categorías, productos y las asociaciones entre ambos. Los datos se almacenan en una base de datos SQLite.

## Tecnologías utilizadas

- Python
- FastAPI
- SQLModel
- SQLite
- python-dotenv

## Requisitos previos

- Python instalado.
- Visual Studio Code.
- Extensión REST Client de Visual Studio Code para ejecutar las solicitudes del archivo `productos.http`.

## Instalación

Clonar el repositorio o descargar el proyecto y abrir una terminal en la carpeta `fastapi-productos`.

Crear un entorno virtual:

```bash
python -m venv .venv
```

Activarlo en Windows con Git Bash:

```bash
source .venv/Scripts/activate
```

Instalar las dependencias:

```bash
pip install -r requirements.txt
```

## Configuración

La aplicación utiliza SQLite y guarda los datos en el archivo `productos.db`.

Si se utiliza el archivo `.env`, debe contener:

```env
DATABASE_URL=sqlite:///./productos.db
```

## Ejecución

Desde la raíz del proyecto, con el entorno virtual activado, ejecutar:

```bash
python -m fastapi dev app/main.py
```

La API estará disponible en:

- API: http://127.0.0.1:8000
- Documentación interactiva: http://127.0.0.1:8000/docs

## Endpoints

### Categorías

| Método | Ruta | Operación |
|---|---|---|
| GET | `/categorias/` | Listar categorías |
| GET | `/categorias/{categoria_id}` | Buscar una categoría |
| POST | `/categorias/` | Crear una categoría |
| PUT | `/categorias/{categoria_id}` | Actualizar una categoría |
| DELETE | `/categorias/{categoria_id}` | Eliminar una categoría |

### Productos

| Método | Ruta | Operación |
|---|---|---|
| GET | `/productos/` | Listar productos |
| GET | `/productos/{producto_id}` | Buscar un producto |
| POST | `/productos/` | Crear un producto |
| PUT | `/productos/{producto_id}` | Actualizar un producto |
| DELETE | `/productos/{producto_id}` | Eliminar un producto |

### Asociaciones entre productos y categorías

| Método | Ruta | Operación |
|---|---|---|
| GET | `/producto-categoria/` | Listar asociaciones |
| POST | `/producto-categoria/` | Asociar un producto con una categoría |
| DELETE | `/producto-categoria/{producto_id}/{categoria_id}` | Eliminar una asociación |

## Pruebas

El archivo `productos.http` contiene solicitudes para probar los endpoints de productos y sus asociaciones. Las solicitudes pueden ejecutarse desde Visual Studio Code utilizando la extensión REST Client.

También se puede utilizar la documentación interactiva disponible en `/docs`.

## CORS

La API permite solicitudes desde `http://localhost:5173`, origen configurado para el frontend de desarrollo.

## Estructura principal

```text
fastapi-productos/
├── app/
│   ├── core/
│   │   └── database.py
│   ├── categoria/
│   │   ├── model.py
│   │   ├── schema.py
│   │   ├── service.py
│   │   └── router.py
│   ├── producto/
│   │   ├── model.py
│   │   ├── schema.py
│   │   ├── service.py
│   │   └── router.py
│   ├── producto_categoria_router.py
│   └── main.py
├── productos.http
├── requirements.txt
├── .env
├── .gitignore
└── README.md
```
