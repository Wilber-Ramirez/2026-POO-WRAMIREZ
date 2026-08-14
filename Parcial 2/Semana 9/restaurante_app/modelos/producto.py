from dataclasses import dataclass

@dataclass
class Producto:
    codigo: str
    nombre: str
    categoria: str
    precio: float

    def __str__(self) -> str:
        return f"{self.codigo} - {self.nombre} ({self.categoria}) - ${self.precio:.2f}"
