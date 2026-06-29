# Clase hija Platillo - hereda de Producto
from .producto import Producto


class Platillo(Producto):
    """
    Clase que representa un platillo (comida) del restaurante.
    Hereda de Producto y agrega atributos específicos de platillos.
    """
    
    def __init__(self, nombre, precio, tipo_platillo, calorias, tiempo_preparacion, disponibilidad=True):
        """
        Inicializa un platillo con atributos adicionales.
        
        Args:
            nombre: Nombre del platillo
            precio: Precio del platillo
            tipo_platillo: Tipo de platillo (e.g., "Entrada", "Plato Fuerte", "Postre")
            calorias: Cantidad de calorías
            tiempo_preparacion: Tiempo de preparación en minutos
            disponibilidad: Estado de disponibilidad (True por defecto)
        """
        super().__init__(nombre, precio, disponibilidad)  # Llama al constructor de la clase padre
        self.tipo_platillo = tipo_platillo
        self.calorias = calorias
        self.tiempo_preparacion = tiempo_preparacion
    
    # Métodos específicos del platillo
    def obtener_tipo_platillo(self):
        """Retorna el tipo de platillo."""
        return self.tipo_platillo
    
    def obtener_calorias(self):
        """Retorna la cantidad de calorías."""
        return self.calorias
    
    def obtener_tiempo_preparacion(self):
        """Retorna el tiempo de preparación en minutos."""
        return self.tiempo_preparacion
    
    def mostrar_informacion(self):
        """
        Sobrescribe el método de la clase padre para mostrar información específica de platillos.
        Demuestra polimorfismo.
        """
        print(f"\n--- Platillo ---")
        print(f"Nombre: {self.nombre}")
        print(f"Tipo: {self.tipo_platillo}")
        print(f"Precio: ${self.obtener_precio():.2f}")
        print(f"Calorías: {self.calorias} kcal")
        print(f"Tiempo de preparación: {self.tiempo_preparacion} minutos")
        print(f"Estado: {self.obtener_disponibilidad()}")
