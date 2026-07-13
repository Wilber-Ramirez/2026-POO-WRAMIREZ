# Clase Bebida - representa una bebida específica del restaurante
from .producto import Producto


class Bebida(Producto):
    """
    Clase que representa una bebida del restaurante.
    Hereda de Producto e incorpora atributos específicos de bebidas.
    
    Demuestra herencia y polimorfismo: una Bebida es un Producto pero con
    características adicionales propias.
    """
    
    def __init__(
        self, 
        codigo: str, 
        nombre: str, 
        categoria: str, 
        precio: float,
        tamaño_ml: int,
        tipo_envase: str
    ) -> None:
        """
        Constructor de la clase Bebida.
        
        Args:
            codigo: Identificador único de la bebida
            nombre: Nombre de la bebida
            categoria: Categoría de la bebida (Bebida Fría, Bebida Caliente, etc.)
            precio: Precio de la bebida
            tamaño_ml: Tamaño en mililitros
            tipo_envase: Tipo de envase (Lata, Botella, Vaso, etc.)
            
        Raises:
            ValueError: Si los datos no cumplen con las validaciones
        """
        # Llamar al constructor de la clase padre
        super().__init__(codigo, nombre, categoria, precio)
        
        if tamaño_ml <= 0:
            raise ValueError("El tamaño de la bebida debe ser mayor a cero.")
        if not tipo_envase or not tipo_envase.strip():
            raise ValueError("El tipo de envase no puede estar vacío.")
        
        self.tamaño_ml: int = tamaño_ml
        self.tipo_envase: str = tipo_envase.strip()
    
    def mostrar_informacion(self) -> str:
        """
        Retorna la información de la bebida en formato legible.
        Sobrescribe el método de la clase padre para mostrar información específica.
        """
        return (
            f"[BEBIDA] Código: {self.codigo} | Nombre: {self.nombre} | "
            f"Categoría: {self.categoria} | Precio: ${self.precio:.2f} | "
            f"Tamaño: {self.tamaño_ml}ml | Envase: {self.tipo_envase}"
        )
    
    def __repr__(self) -> str:
        """Representación en string del objeto Bebida."""
        return (
            f"Bebida(codigo='{self.codigo}', nombre='{self.nombre}', "
            f"tamaño_ml={self.tamaño_ml}, envase='{self.tipo_envase}')"
        )
