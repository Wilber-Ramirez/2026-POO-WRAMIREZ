# Clase de servicio Restaurante - administra productos, bebidas y clientes
from typing import List, Optional
from modelos import Producto, Bebida, Cliente


class Restaurante:
    """
    Clase de servicio que administra las colecciones de productos y clientes.
    
    Demuestra el principio de responsabilidad única:
    - Solo administra listas
    - Valida unicidad de identificadores
    - Utiliza polimorfismo para procesar Producto y Bebida uniformemente
    """
    
    def __init__(self, nombre: str) -> None:
        """
        Constructor de la clase Restaurante.
        
        Args:
            nombre: Nombre del restaurante
        """
        self.nombre: str = nombre
        self.productos: List[Producto] = []  # Contiene Producto y Bebida
        self.clientes: List[Cliente] = []
    
    # ============ MÉTODOS PARA PRODUCTOS ============
    
    def registrar_producto(self, producto: Producto) -> bool:
        """
        Registra un nuevo producto en el restaurante.
        
        Args:
            producto: Objeto Producto o Bebida a registrar
            
        Returns:
            True si se registró exitosamente, False si ya existe el código
        """
        # Validar que el código no se repita
        if self._codigo_existe(producto.codigo):
            print(f"✗ El código '{producto.codigo}' ya existe.")
            return False
        
        self.productos.append(producto)
        print(f"✓ {tipo_producto(producto)} '{producto.nombre}' registrado exitosamente.")
        return True
    
    def listar_productos(self) -> None:
        """
        Lista todos los productos registrados.
        Demuestra polimorfismo: cada objeto ejecuta su propia versión de mostrar_informacion()
        """
        print(f"\n{'='*80}")
        print(f"  PRODUCTOS REGISTRADOS EN {self.nombre.upper()}")
        print(f"{'='*80}")
        
        if not self.productos:
            print("No hay productos registrados.")
            print(f"{'='*80}\n")
            return
        
        # Polimorfismo: cada producto ejecuta su propia versión de mostrar_informacion()
        for idx, producto in enumerate(self.productos, 1):
            print(f"{idx}. {producto.mostrar_informacion()}")
        
        print(f"{'='*80}\n")
    
    def buscar_producto_por_codigo(self, codigo: str) -> Optional[Producto]:
        """
        Busca un producto por su código.
        
        Args:
            codigo: Código del producto a buscar
            
        Returns:
            Objeto Producto encontrado o None
        """
        for producto in self.productos:
            if producto.codigo.lower() == codigo.lower():
                return producto
        return None
    
    def _codigo_existe(self, codigo: str) -> bool:
        """
        Verifica si un código de producto ya está registrado.
        
        Args:
            codigo: Código a verificar
            
        Returns:
            True si el código existe, False en caso contrario
        """
        return any(p.codigo.lower() == codigo.lower() for p in self.productos)
    
    # ============ MÉTODOS PARA CLIENTES ============
    
    def registrar_cliente(self, cliente: Cliente) -> bool:
        """
        Registra un nuevo cliente en el restaurante.
        
        Args:
            cliente: Objeto Cliente a registrar
            
        Returns:
            True si se registró exitosamente, False si ya existe la identificación
        """
        # Validar que la identificación no se repita
        if self._identificacion_existe(cliente.identificacion):
            print(f"✗ La identificación '{cliente.identificacion}' ya existe.")
            return False
        
        self.clientes.append(cliente)
        print(f"✓ Cliente '{cliente.nombre}' registrado exitosamente.")
        return True
    
    def listar_clientes(self) -> None:
        """Lista todos los clientes registrados."""
        print(f"\n{'='*80}")
        print(f"  CLIENTES REGISTRADOS EN {self.nombre.upper()}")
        print(f"{'='*80}")
        
        if not self.clientes:
            print("No hay clientes registrados.")
            print(f"{'='*80}\n")
            return
        
        for idx, cliente in enumerate(self.clientes, 1):
            print(f"{idx}. {cliente.mostrar_informacion()}")
        
        print(f"{'='*80}\n")
    
    def buscar_cliente_por_identificacion(self, identificacion: str) -> Optional[Cliente]:
        """
        Busca un cliente por su identificación.
        
        Args:
            identificacion: Identificación del cliente a buscar
            
        Returns:
            Objeto Cliente encontrado o None
        """
        for cliente in self.clientes:
            if cliente.identificacion.lower() == identificacion.lower():
                return cliente
        return None
    
    def _identificacion_existe(self, identificacion: str) -> bool:
        """
        Verifica si una identificación ya está registrada.
        
        Args:
            identificacion: Identificación a verificar
            
        Returns:
            True si existe, False en caso contrario
        """
        return any(c.identificacion.lower() == identificacion.lower() for c in self.clientes)
    
    # ============ MÉTODOS DE ESTADÍSTICAS ============
    
    def obtener_estadisticas(self) -> dict:
        """
        Retorna estadísticas del restaurante.
        
        Returns:
            Diccionario con cantidad de productos y clientes
        """
        productos_normales = sum(1 for p in self.productos if type(p).__name__ == 'Producto')
        bebidas = sum(1 for p in self.productos if isinstance(p, Bebida))
        
        return {
            'total_productos': len(self.productos),
            'productos': productos_normales,
            'bebidas': bebidas,
            'total_clientes': len(self.clientes)
        }


def tipo_producto(producto: Producto) -> str:
    """
    Función auxiliar para determinar el tipo de producto.
    
    Args:
        producto: Objeto Producto o Bebida
        
    Returns:
        String con el tipo de producto
    """
    if isinstance(producto, Bebida):
        return "Bebida"
    return "Producto"
