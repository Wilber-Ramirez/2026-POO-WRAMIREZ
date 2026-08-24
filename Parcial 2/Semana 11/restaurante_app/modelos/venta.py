from __future__ import annotations

from typing import Any, Dict


class Venta:
    def __init__(self, usuario_id: str, producto_codigo: str, cantidad: int) -> None:
        self.usuario_id = self._validar_campo(usuario_id, "usuario_id")
        self.producto_codigo = self._validar_campo(producto_codigo, "producto_codigo")

        if cantidad <= 0:
            raise ValueError("La cantidad vendida debe ser mayor que cero.")

        self.cantidad = int(cantidad)

    @staticmethod
    def _validar_campo(valor: str, nombre: str) -> str:
        if valor is None or not str(valor).strip():
            raise ValueError(f"El campo {nombre} no puede estar vacío.")
        return str(valor).strip()

    def __str__(self) -> str:
        return f"Usuario: {self.usuario_id} | Producto: {self.producto_codigo} | Cantidad: {self.cantidad}"

    def a_diccionario(self) -> Dict[str, Any]:
        return {
            "usuario_id": self.usuario_id,
            "producto_codigo": self.producto_codigo,
            "cantidad": self.cantidad,
        }

    @classmethod
    def desde_diccionario(cls, datos: Dict[str, Any]) -> "Venta":
        try:
            return cls(
                usuario_id=datos["usuario_id"],
                producto_codigo=datos["producto_codigo"],
                cantidad=int(datos["cantidad"]),
            )
        except (KeyError, TypeError, ValueError) as exc:
            raise ValueError(f"No se puede reconstruir Venta desde el diccionario: {exc}") from exc
