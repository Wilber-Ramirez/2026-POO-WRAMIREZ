from dataclasses import dataclass


@dataclass
class Cliente:
    """Clase que representa un cliente del restaurante.
    
    Atributos:
        id_cliente: Identificador único del cliente
        nombre: Nombre del cliente
        correo: Correo electrónico del cliente
    """
    id_cliente: int
    nombre: str
    correo: str
    
    def __str__(self):
        """Retorna una representación legible del cliente."""
        return f"ID: {self.id_cliente} | Nombre: {self.nombre} | Correo: {self.correo}"
