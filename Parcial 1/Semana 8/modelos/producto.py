# Clase base Producto - representa un producto general del restaurante
class Producto:
    """
    Clase base que representa un producto del restaurante.
    Define atributos y comportamiento común a todos los productos.
    """
    
    def __init__(self, codigo: str, nombre: str, categoria: str, precio: float) -> None:
        """
        Constructor de la clase Producto.
        
        Args:
            codigo: Identificador único del producto
            nombre: Nombre del producto
            categoria: Categoría del producto
            precio: Precio del producto
            
        Raises:
            ValueError: Si los datos no cumplen con las validaciones
        """
        if not codigo or not codigo.strip():
            raise ValueError("El código del producto no puede estar vacío.")
        if not nombre or not nombre.strip():
            raise ValueError("El nombre del producto no puede estar vacío.")
        if not categoria or not categoria.strip():
            raise ValueError("La categoría del producto no puede estar vacía.")
        if precio <= 0:
            raise ValueError("El precio del producto debe ser mayor a cero.")
        
        self.codigo: str = codigo.strip()
        self.nombre: str = nombre.strip()
        self.categoria: str = categoria.strip()
        self.precio: float = precio
    
    def mostrar_informacion(self) -> str:
        """
        Retorna la información del producto en formato legible.
        Este método puede ser sobrescrito por subclases.
        """
        return (
            f"[PRODUCTO] Código: {self.codigo} | Nombre: {self.nombre} | "
            f"Categoría: {self.categoria} | Precio: ${self.precio:.2f}"
        )
    
    def __repr__(self) -> str:
        """Representación en string del objeto Producto."""
        return f"Producto(codigo='{self.codigo}', nombre='{self.nombre}', precio={self.precio})"
