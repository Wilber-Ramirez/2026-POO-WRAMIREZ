# Clase padre Producto - representa un producto general del restaurante
class Producto:
    """
    Clase padre que representa un producto genérico del restaurante.
    Encapsula atributos comunes a todos los productos.
    """
    
    def __init__(self, nombre, precio, disponibilidad=True):
        """
        Inicializa un producto con su información básica.
        
        Args:
            nombre: Nombre del producto
            precio: Precio del producto (debe ser positivo)
            disponibilidad: Indica si el producto está disponible (True por defecto)
        """
        self.nombre = nombre
        self.__precio = precio  # Atributo privado (encapsulado)
        self.disponibilidad = disponibilidad
    
    # Métodos de acceso (getters) y modificación (setters)
    def obtener_precio(self):
        """Retorna el precio del producto."""
        return self.__precio
    
    def cambiar_precio(self, nuevo_precio):
        """
        Cambia el precio del producto con validación.
        
        Args:
            nuevo_precio: Nuevo precio a establecer
            
        Raises:
            ValueError: Si el precio es negativo o igual a cero
        """
        if nuevo_precio <= 0:
            raise ValueError("El precio debe ser mayor a cero.")
        self.__precio = nuevo_precio
    
    def obtener_disponibilidad(self):
        """Retorna el estado de disponibilidad del producto."""
        return "Disponible" if self.disponibilidad else "No disponible"
    
    def cambiar_disponibilidad(self, estado):
        """Cambia el estado de disponibilidad del producto."""
        self.disponibilidad = estado
    
    def mostrar_informacion(self):
        """
        Muestra la información básica del producto.
        Este método será sobrescrito en las clases hijas.
        """
        print(f"\n--- Producto ---")
        print(f"Nombre: {self.nombre}")
        print(f"Precio: ${self.__precio:.2f}")
        print(f"Estado: {self.obtener_disponibilidad()}")
