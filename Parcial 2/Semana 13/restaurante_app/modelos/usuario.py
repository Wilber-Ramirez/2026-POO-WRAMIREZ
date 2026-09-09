from __future__ import annotations

from typing import Any, Dict


class Usuario:
    def __init__(self, identificacion: str, nombre: str, correo: str) -> None:
        self.identificacion = self._validar_campo(identificacion, "identificación")
        self.nombre = self._validar_campo(nombre, "nombre")
        self.correo = self._validar_campo(correo, "correo")

    @staticmethod
    def _validar_campo(valor: str, nombre: str) -> str:
        if valor is None or not str(valor).strip():
            raise ValueError(f"El campo {nombre} no puede estar vacío.")
        return str(valor).strip()

    def __str__(self) -> str:
        return f"{self.identificacion} - {self.nombre} <{self.correo}>"

    def a_diccionario(self) -> Dict[str, Any]:
        return {
            "identificacion": self.identificacion,
            "nombre": self.nombre,
            "correo": self.correo,
        }

    @classmethod
    def desde_diccionario(cls, datos: Dict[str, Any]) -> "Usuario":
        try:
            return cls(
                identificacion=datos["identificacion"],
                nombre=datos["nombre"],
                correo=datos["correo"],
            )
        except (KeyError, TypeError, ValueError) as exc:
            raise ValueError(f"No se puede reconstruir Usuario desde el diccionario: {exc}") from exc
