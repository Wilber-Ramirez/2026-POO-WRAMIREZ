# Clase que representa un producto del restaurante

class Producto:
    """
    Clase que representa un producto (plato o bebida) disponible en el restaurante.
    Almacena información sobre el producto y su disponibilidad.
    """
    
    def __init__(self, codigo: int, nombre: str, descripcion: str, precio: float, disponible: bool):
        """
        Constructor de la clase Producto.
        
        Args:
            codigo: Identificador único del producto (tipo int)
            nombre: Nombre del producto (tipo str)
            descripcion: Descripción breve del producto (tipo str)
            precio: Precio del producto en unidades monetarias (tipo float)
            disponible: Indica si el producto está disponible (tipo bool)
        """
        self.codigo: int = codigo
        self.nombre: str = nombre
        self.descripcion: str = descripcion
        self.precio: float = precio
        self.disponible: bool = disponible
    
    def __str__(self) -> str:
        """
        Representación en texto de un objeto Producto.
        
        Returns:
            Cadena de texto con la información del producto
        """
        estado = "Disponible" if self.disponible else "No disponible"
        return f"Producto(ID: {self.codigo}, Nombre: {self.nombre}, Precio: ${self.precio:.2f}, Estado: {estado})"
    
    def cambiar_disponibilidad(self, disponible: bool) -> None:
        """
        Cambia el estado de disponibilidad del producto.
        
        Args:
            disponible: Nuevo estado de disponibilidad
        """
        self.disponible = disponible
    
    def obtener_informacion_completa(self) -> str:
        """
        Retorna la información completa del producto.
        
        Returns:
            Cadena con descripción detallada del producto
        """
        return f"{self.nombre}: {self.descripcion} - Precio: ${self.precio:.2f}"
