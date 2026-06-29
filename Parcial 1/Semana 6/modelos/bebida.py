# Clase hija Bebida - hereda de Producto
from .producto import Producto


class Bebida(Producto):
    """
    Clase que representa una bebida disponible en el restaurante.
    Hereda de Producto y agrega atributos específicos de bebidas.
    """
    
    def __init__(self, nombre, precio, tipo_bebida, volumen_ml, es_fria, disponibilidad=True):
        """
        Inicializa una bebida con atributos adicionales.
        
        Args:
            nombre: Nombre de la bebida
            precio: Precio de la bebida
            tipo_bebida: Tipo de bebida (e.g., "Gaseosa", "Jugo", "Café", "Té")
            volumen_ml: Volumen de la bebida en mililitros
            es_fria: Indica si la bebida se sirve fría (True) o caliente (False)
            disponibilidad: Estado de disponibilidad (True por defecto)
        """
        super().__init__(nombre, precio, disponibilidad)  # Llama al constructor de la clase padre
        self.tipo_bebida = tipo_bebida
        self.volumen_ml = volumen_ml
        self.es_fria = es_fria
    
    # Métodos específicos de la bebida
    def obtener_tipo_bebida(self):
        """Retorna el tipo de bebida."""
        return self.tipo_bebida
    
    def obtener_volumen(self):
        """Retorna el volumen en mililitros."""
        return self.volumen_ml
    
    def obtener_temperatura(self):
        """Retorna el tipo de temperatura de servicio."""
        return "Fría" if self.es_fria else "Caliente"
    
    def mostrar_informacion(self):
        """
        Sobrescribe el método de la clase padre para mostrar información específica de bebidas.
        Demuestra polimorfismo.
        """
        print(f"\n--- Bebida ---")
        print(f"Nombre: {self.nombre}")
        print(f"Tipo: {self.tipo_bebida}")
        print(f"Precio: ${self.obtener_precio():.2f}")
        print(f"Volumen: {self.volumen_ml} ml")
        print(f"Temperatura de servicio: {self.obtener_temperatura()}")
        print(f"Estado: {self.obtener_disponibilidad()}")
