
import CategoriaCard from "./CategoriaCard";
import type { Categoria } from "../types/categoria";

type CategoriaListProps = {
  categorias: Categoria[];
  onEdit: (categoria: Categoria) => void;
  onDelete: (id: number) => void;
};

function CategoriaList({
  categorias,
  onEdit,
  onDelete,
}: CategoriaListProps) {
  if (categorias.length === 0) {
    return (
      <p className="text-gray-500 text-center py-8">
        Todavía no hay categorías registradas.
      </p>
    );
  }

  return (
    <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
      {categorias.map((categoria) => (
        <CategoriaCard
          key={categoria.id}
          categoria={categoria}
          onEdit={onEdit}
          onDelete={onDelete}
        />
      ))}
    </div>
  );
}

export default CategoriaList;
