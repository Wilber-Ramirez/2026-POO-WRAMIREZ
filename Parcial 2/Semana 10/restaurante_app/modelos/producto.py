from dataclasses import dataclass
from typing import Dict, Any

@dataclass
class Producto:
    codigo: str
    nombre: str
    categoria: str
    precio: float

    def __post_init__(self) -> None:
        if not self.codigo or not self.codigo.strip():
            raise ValueError("El código del producto no puede estar vacío.")
        if not self.nombre or not self.nombre.strip():
            raise ValueError("El nombre del producto no puede estar vacío.")
        if not self.categoria or not self.categoria.strip():
            raise ValueError("La categoría del producto no puede estar vacía.")
        if self.precio < 0:
            raise ValueError("El precio no puede ser negativo.")

    def __str__(self) -> str:
        return f"{self.codigo} - {self.nombre} ({self.categoria}) - ${self.precio:.2f}"

    def a_diccionario(self) -> Dict[str, Any]:
        """Convierte el producto a un diccionario para serialización JSON."""
        return {
            "codigo": self.codigo,
            "nombre": self.nombre,
            "categoria": self.categoria,
            "precio": self.precio
        }

    @staticmethod
    def desde_diccionario(datos: Dict[str, Any]) -> 'Producto':
        """Reconstruye un Producto desde un diccionario."""
        try:
            codigo = datos.get("codigo", "").strip()
            nombre = datos.get("nombre", "").strip()
            categoria = datos.get("categoria", "").strip()
            precio = float(datos.get("precio", 0))

            return Producto(codigo=codigo, nombre=nombre, categoria=categoria, precio=precio)
        except (ValueError, TypeError, KeyError) as e:
            raise ValueError(f"No se puede reconstruir Producto desde diccionario: {e}")
