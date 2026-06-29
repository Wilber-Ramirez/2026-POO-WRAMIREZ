# Clase de servicio Restaurante - administra los productos
class Restaurante:
    """
    Clase de servicio que administra la lista de productos del restaurante.
    Permite agregar, eliminar y mostrar productos.
    """
    
    def __init__(self, nombre_restaurante):
        """
        Inicializa un restaurante con un nombre y una lista vacía de productos.
        
        Args:
            nombre_restaurante: Nombre del restaurante
        """
        self.nombre_restaurante = nombre_restaurante
        self.productos = []  # Lista para almacenar los productos
    
    def agregar_producto(self, producto):
        """
        Agrega un producto a la lista del restaurante.
        
        Args:
            producto: Objeto producto a agregar
        """
        self.productos.append(producto)
        print(f"✓ '{producto.nombre}' agregado al restaurante.")
    
    def eliminar_producto(self, nombre):
        """
        Elimina un producto de la lista del restaurante por su nombre.
        
        Args:
            nombre: Nombre del producto a eliminar
        """
        for producto in self.productos:
            if producto.nombre.lower() == nombre.lower():
                self.productos.remove(producto)
                print(f"✓ '{producto.nombre}' eliminado del restaurante.")
                return
        print(f"✗ Producto '{nombre}' no encontrado.")
    
    def obtener_cantidad_productos(self):
        """Retorna la cantidad de productos registrados."""
        return len(self.productos)
    
    def mostrar_menu(self):
        """
        Muestra toda la información del menú del restaurante.
        Demuestra polimorfismo al recorrer la lista y ejecutar mostrar_informacion()
        según el tipo de objeto.
        """
        print(f"\n{'='*50}")
        print(f"  MENÚ DE {self.nombre_restaurante.upper()}")
        print(f"{'='*50}")
        print(f"Total de productos: {self.obtener_cantidad_productos()}\n")
        
        if not self.productos:
            print("No hay productos registrados en el menú.")
            return
        
        # Polimorfismo: recorre la lista de productos y ejecuta mostrar_informacion()
        # El método ejecutado depende del tipo de objeto (Platillo, Bebida, etc.)
        for producto in self.productos:
            producto.mostrar_informacion()
        
        print(f"\n{'='*50}\n")
    
    def mostrar_platillos(self):
        """Muestra solo los platillos del restaurante."""
        from modelos import Platillo
        
        print(f"\n--- PLATILLOS ---")
        platillos = [p for p in self.productos if isinstance(p, Platillo)]
        
        if not platillos:
            print("No hay platillos registrados.")
            return
        
        for platillo in platillos:
            platillo.mostrar_informacion()
    
    def mostrar_bebidas(self):
        """Muestra solo las bebidas del restaurante."""
        from modelos import Bebida
        
        print(f"\n--- BEBIDAS ---")
        bebidas = [p for p in self.productos if isinstance(p, Bebida)]
        
        if not bebidas:
            print("No hay bebidas registradas.")
            return
        
        for bebida in bebidas:
            bebida.mostrar_informacion()
