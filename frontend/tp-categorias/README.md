# Frontend - Gestión de Categorías

Trabajo práctico de la Unidad 6 de Programación IV.

## Descripción

Aplicación web desarrollada con React y TypeScript para administrar categorías de productos. Consume una API REST desarrollada con FastAPI y permite listar, crear, editar y eliminar categorías.

## Tecnologías utilizadas

- React
- TypeScript
- Vite
- Tailwind CSS
- Fetch API
- pnpm

## Requisitos previos

- Node.js instalado.
- pnpm instalado.
- Backend de FastAPI configurado y en ejecución.

## Instalación

Abrir una terminal en la carpeta `tp-categorias` y ejecutar:

```bash
pnpm install
```

## Ejecución

Iniciar el servidor de desarrollo:

```bash
pnpm dev
```

La aplicación estará disponible en:

http://localhost:5173/

## Comunicación con el backend

La aplicación consume la API de FastAPI mediante `fetch`.

La URL base utilizada para las categorías es:

`http://127.0.0.1:8000/categorias/`

Para que la comunicación funcione, el backend debe estar iniciado y permitir solicitudes desde el origen `http://localhost:5173`.

## Funcionalidades

- Listar categorías existentes.
- Crear categorías mediante un formulario modal.
- Editar categorías existentes.
- Eliminar categorías con confirmación.
- Actualizar la lista después de cada operación.
- Mostrar un mensaje cuando ocurre un error al cargar las categorías.

## Compilación de producción

Para verificar los tipos de TypeScript y generar la versión de producción, ejecutar:

```bash
pnpm build
```

Los archivos generados se guardan en la carpeta `dist/`.

## Estructura principal

```text
tp-categorias/
├── src/
│   ├── components/
│   │   ├── Navbar.tsx
│   │   ├── CategoriaCard.tsx
│   │   ├── CategoriaList.tsx
│   │   └── CategoriaModal.tsx
│   ├── types/
│   │   └── categoria.ts
│   ├── App.tsx
│   ├── index.css
│   └── main.tsx
├── package.json
├── vite.config.ts
└── README.md
```