
import type { Categoria } from "../types/categoria";

type CategoriaCardProps = {
  categoria: Categoria;
  onEdit: (categoria: Categoria) => void;
  onDelete: (id: number) => void;
};

function CategoriaCard({
  categoria,
  onEdit,
  onDelete,
}: CategoriaCardProps) {
  return (
    <div className="bg-white rounded-lg shadow-md p-6 border border-gray-200">
      <h3 className="text-xl font-semibold text-gray-800">
        {categoria.nombre}
      </h3>

      <p className="text-gray-600 mt-2">
        {categoria.descripcion}
      </p>

      <div className="flex gap-3 mt-5">
        <button
          onClick={() => onEdit(categoria)}
          className="bg-yellow-500 hover:bg-yellow-600 text-white px-4 py-2 rounded-md cursor-pointer"
        >
          Editar
        </button>

        <button
          onClick={() => onDelete(categoria.id)}
          className="bg-red-500 hover:bg-red-600 text-white px-4 py-2 rounded-md cursor-pointer"
        >
          Eliminar
        </button>
      </div>
    </div>
  );
}

export default CategoriaCard;
