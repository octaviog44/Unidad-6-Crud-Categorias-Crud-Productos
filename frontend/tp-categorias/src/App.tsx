
import { useEffect, useState } from "react";
import Navbar from "./components/Navbar";
import CategoriaList from "./components/CategoriaList";
import CategoriaModal from "./components/CategoriaModal";
import type { Categoria } from "./types/categoria";

const API_URL = "http://127.0.0.1:8000/categorias/";

function App() {
  const [categorias, setCategorias] = useState<Categoria[]>([]);
  const [isModalOpen, setIsModalOpen] = useState(false);
  const [categoriaSeleccionada, setCategoriaSeleccionada] =
    useState<Categoria | null>(null);
  const [cargando, setCargando] = useState(true);
  const [error, setError] = useState("");

  const cargarCategorias = async () => {
    try {
      setError("");

      const respuesta = await fetch(API_URL);

      if (!respuesta.ok) {
        throw new Error("No se pudieron cargar las categorías.");
      }

      const datos: Categoria[] = await respuesta.json();
      setCategorias(datos);
    } catch (error) {
      console.error("Error al cargar categorías:", error);
      setError(
        "No se pudieron cargar las categorías. Verificá que el backend esté funcionando."
      );
    } finally {
      setCargando(false);
    }
  };

  useEffect(() => {
    void cargarCategorias();
  }, []);

  const handleCreate = () => {
    setCategoriaSeleccionada(null);
    setIsModalOpen(true);
  };

  const handleEdit = (categoria: Categoria) => {
    setCategoriaSeleccionada(categoria);
    setIsModalOpen(true);
  };

  const handleDelete = async (id: number) => {
    const confirmar = window.confirm(
      "¿Estás seguro de que querés eliminar esta categoría?"
    );

    if (!confirmar) return;

    try {
      const respuesta = await fetch(`${API_URL}${id}`, {
        method: "DELETE",
      });

      if (!respuesta.ok) {
        throw new Error("No se pudo eliminar la categoría.");
      }

      await cargarCategorias();
    } catch (error) {
      console.error("Error al eliminar categoría:", error);
      alert("No se pudo eliminar la categoría.");
    }
  };

  const handleSubmit = async (datos: Omit<Categoria, "id">) => {
    const editando = categoriaSeleccionada !== null;

    const url = editando
      ? `${API_URL}${categoriaSeleccionada.id}`
      : API_URL;

    try {
      const respuesta = await fetch(url, {
        method: editando ? "PUT" : "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify(datos),
      });

      if (!respuesta.ok) {
        const detalle = await respuesta.text();
        throw new Error(detalle || "No se pudo guardar la categoría.");
      }

      setIsModalOpen(false);
      setCategoriaSeleccionada(null);

      await cargarCategorias();
    } catch (error) {
      console.error("Error al guardar categoría:", error);
      alert(
        error instanceof Error
          ? `No se pudo guardar la categoría: ${error.message}`
          : "No se pudo guardar la categoría."
      );
    }
  };

  const handleCloseModal = () => {
    setIsModalOpen(false);
    setCategoriaSeleccionada(null);
  };

  return (
    <div className="min-h-screen bg-gray-100">
      <Navbar />

      <main className="mx-auto max-w-6xl px-6 py-8">
        <div className="mb-6 flex flex-wrap items-center justify-between gap-4">
          <div>
            <h2 className="text-2xl font-semibold text-gray-800">
              Categorías
            </h2>
            <p className="mt-1 text-gray-600">
              Administrá las categorías de productos.
            </p>
          </div>

          <button
            onClick={handleCreate}
            className="rounded-md bg-blue-600 px-4 py-2 font-medium text-white hover:bg-blue-700"
          >
            + Nueva categoría
          </button>
        </div>

        {cargando && (
          <p className="py-8 text-center text-gray-600">
            Cargando categorías...
          </p>
        )}

        {!cargando && error && (
          <div className="rounded-md bg-red-100 p-4 text-red-700">
            <p>{error}</p>
            <button
              onClick={() => {
                setCargando(true);
                void cargarCategorias();
              }}
              className="mt-2 font-semibold underline"
            >
              Reintentar
            </button>
          </div>
        )}

        {!cargando && !error && (
          <CategoriaList
            categorias={categorias}
            onEdit={handleEdit}
            onDelete={handleDelete}
          />
        )}

        <CategoriaModal
          isOpen={isModalOpen}
          categoria={categoriaSeleccionada}
          onClose={handleCloseModal}
          onSubmit={handleSubmit}
        />
      </main>
    </div>
  );
}

export default App;
