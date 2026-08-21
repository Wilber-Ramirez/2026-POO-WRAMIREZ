from dataclasses import dataclass

@dataclass
class Usuario:
    identificacion: str
    nombre: str
    correo: str

    def __str__(self) -> str:
        return f"{self.identificacion} - {self.nombre} <{self.correo}>"
