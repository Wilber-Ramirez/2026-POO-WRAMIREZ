class Producto:
    """Clase que representa un producto del restaurante.
    
    Atributos:
        nombre: Nombre del producto
        categoria: Categoría del producto
        precio: Precio del producto
        disponible: Disponibilidad del producto
    """
    
    def __init__(self, nombre, categoria, precio, disponible=True):
        """Constructor de la clase Producto.
        
        Args:
            nombre: Nombre del producto (no puede estar vacío)
            categoria: Categoría del producto (no puede estar vacía)
            precio: Precio del producto (debe ser mayor a cero)
            disponible: Disponibilidad del producto (por defecto True)
            
        Raises:
            ValueError: Si los datos no cumplen con las validaciones
        """
        # Validaciones en el constructor
        if not nombre or not nombre.strip():
            raise ValueError("El nombre del producto no puede estar vacío.")
        if not categoria or not categoria.strip():
            raise ValueError("La categoría del producto no puede estar vacía.")
        if precio <= 0:
            raise ValueError("El precio del producto debe ser mayor a cero.")
        
        self._nombre = nombre
        self._categoria = categoria
        self._precio = precio
        self._disponible = disponible
    
    @property
    def nombre(self):
        """Obtiene el nombre del producto."""
        return self._nombre
    
    @nombre.setter
    def nombre(self, valor):
        """Establece el nombre del producto con validación."""
        if not valor or not valor.strip():
            raise ValueError("El nombre del producto no puede estar vacío.")
        self._nombre = valor
    
    @property
    def categoria(self):
        """Obtiene la categoría del producto."""
        return self._categoria
    
    @categoria.setter
    def categoria(self, valor):
        """Establece la categoría del producto con validación."""
        if not valor or not valor.strip():
            raise ValueError("La categoría del producto no puede estar vacía.")
        self._categoria = valor
    
    @property
    def precio(self):
        """Obtiene el precio del producto."""
        return self._precio
    
    @precio.setter
    def precio(self, valor):
        """Establece el precio del producto con validación."""
        if valor <= 0:
            raise ValueError("El precio del producto debe ser mayor a cero.")
        self._precio = valor
    
    @property
    def disponible(self):
        """Obtiene la disponibilidad del producto."""
        return self._disponible
    
    @disponible.setter
    def disponible(self, valor):
        """Establece la disponibilidad del producto."""
        self._disponible = valor
    
    def mostrar_informacion(self):
        """Muestra la información del producto de forma legible."""
        estado = "✓ Disponible" if self._disponible else "✗ No disponible"
        return f"Nombre: {self._nombre} | Categoría: {self._categoria} | Precio: ${self._precio:.2f} | {estado}"
