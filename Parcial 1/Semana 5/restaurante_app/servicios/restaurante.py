# Clase que gestiona los productos y clientes del restaurante

from modelos.producto import Producto
from modelos.cliente import Cliente


class Restaurante:
    """
    Clase que administra el restaurante, manejando listas de productos y clientes.
    Proporciona métodos para agregar, listar y gestionar la información del restaurante.
    """
    
    def __init__(self, nombre_restaurante: str, direccion: str):
        """
        Constructor de la clase Restaurante.
        
        Args:
            nombre_restaurante: Nombre del restaurante (tipo str)
            direccion: Dirección del restaurante (tipo str)
        """
        self.nombre_restaurante: str = nombre_restaurante
        self.direccion: str = direccion
        self.lista_productos: list[Producto] = []
        self.lista_clientes: list[Cliente] = []
    
    def agregar_producto(self, producto: Producto) -> None:
        """
        Agrega un producto a la lista de productos del restaurante.
        
        Args:
            producto: Objeto Producto a agregar
        """
        self.lista_productos.append(producto)
    
    def agregar_cliente(self, cliente: Cliente) -> None:
        """
        Agrega un cliente a la lista de clientes del restaurante.
        
        Args:
            cliente: Objeto Cliente a agregar
        """
        self.lista_clientes.append(cliente)
    
    def listar_productos(self) -> None:
        """
        Muestra en consola todos los productos registrados en el restaurante.
        """
        if not self.lista_productos:
            print("No hay productos registrados.")
            return
        
        print("\n=== LISTA DE PRODUCTOS ===")
        for producto in self.lista_productos:
            print(f"  {producto}")
    
    def listar_clientes(self) -> None:
        """
        Muestra en consola todos los clientes registrados en el restaurante.
        """
        if not self.lista_clientes:
            print("No hay clientes registrados.")
            return
        
        print("\n=== LISTA DE CLIENTES ===")
        for cliente in self.lista_clientes:
            print(f"  {cliente}")
    
    def obtener_resumen_restaurante(self) -> str:
        """
        Retorna un resumen con información general del restaurante.
        
        Returns:
            Cadena con información del restaurante
        """
        cantidad_productos = len(self.lista_productos)
        cantidad_clientes = len(self.lista_clientes)
        return f"Restaurante: {self.nombre_restaurante} | Dirección: {self.direccion} | Productos: {cantidad_productos} | Clientes: {cantidad_clientes}"
    
    def mostrar_informacion_completa(self) -> None:
        """
        Muestra la información completa del restaurante con detalles de productos y clientes.
        """
        print("\n" + "="*50)
        print(self.obtener_resumen_restaurante())
        print("="*50)
        
        self.listar_productos()
        self.listar_clientes()
