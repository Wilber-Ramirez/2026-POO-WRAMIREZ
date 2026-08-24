from __future__ import annotations

from typing import Any, Dict


class Producto:
    def __init__(self, codigo: str, nombre: str, categoria: str, precio: float, stock: int = 0) -> None:
        self.codigo = self._validar_campo(codigo, "codigo")
        self.nombre = self._validar_campo(nombre, "nombre")
        self.categoria = self._validar_campo(categoria, "categoria")

        if precio < 0:
            raise ValueError("El precio del producto no puede ser negativo.")
        if stock < 0:
            raise ValueError("El stock del producto no puede ser negativo.")

        self.precio = float(precio)
        self.stock = int(stock)

    @staticmethod
    def _validar_campo(valor: str, nombre: str) -> str:
        if valor is None or not str(valor).strip():
            raise ValueError(f"El campo {nombre} no puede estar vacío.")
        return str(valor).strip()

    def vender(self, cantidad: int) -> bool:
        if cantidad <= 0:
            raise ValueError("La cantidad vendida debe ser mayor que cero.")
        if cantidad > self.stock:
            raise ValueError("La cantidad solicitada supera el stock disponible.")

        self.stock -= cantidad
        return True

    def __str__(self) -> str:
        return f"{self.codigo} - {self.nombre} ({self.categoria}) - ${self.precio:.2f} - Stock: {self.stock}"

    def a_diccionario(self) -> Dict[str, Any]:
        return {
            "codigo": self.codigo,
            "nombre": self.nombre,
            "categoria": self.categoria,
            "precio": self.precio,
            "stock": self.stock,
        }

    @classmethod
    def desde_diccionario(cls, datos: Dict[str, Any]) -> "Producto":
        try:
            return cls(
                codigo=datos["codigo"],
                nombre=datos["nombre"],
                categoria=datos["categoria"],
                precio=float(datos["precio"]),
                stock=int(datos.get("stock", 0)),
            )
        except (KeyError, TypeError, ValueError) as exc:
            raise ValueError(f"No se puede reconstruir Producto desde el diccionario: {exc}") from exc
