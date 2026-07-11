# Clase de servicio Restaurante - administra productos y clientes
class Restaurante:
    """
    Clase de servicio que administra la lista de productos y clientes del restaurante.
    Permite registrar, listar y buscar productos y clientes.
    """
    
    def __init__(self, nombre_restaurante):
        """
        Inicializa un restaurante con un nombre y listas vacías de productos y clientes.
        
        Args:
            nombre_restaurante: Nombre del restaurante
        """
        self.nombre_restaurante = nombre_restaurante
        self.productos = []  # Lista para almacenar los productos
        self.clientes = []   # Lista para almacenar los clientes
        self.proximo_id_cliente = 1  # Contador para IDs de clientes
    
    # ============ MÉTODOS PARA PRODUCTOS ============
    
    def registrar_producto(self, producto):
        """
        Registra un nuevo producto en el restaurante.
        
        Args:
            producto: Objeto Producto a registrar
        """
        self.productos.append(producto)
        print(f"✓ Producto '{producto.nombre}' registrado exitosamente.")
    
    def listar_productos(self):
        """Muestra todos los productos registrados en el restaurante."""
        print(f"\n{'='*70}")
        print(f"  PRODUCTOS REGISTRADOS")
        print(f"{'='*70}")
        
        if not self.productos:
            print("No hay productos registrados.")
            print(f"{'='*70}\n")
            return
        
        for idx, producto in enumerate(self.productos, 1):
            print(f"{idx}. {producto.mostrar_informacion()}")
        
        print(f"{'='*70}\n")
    
    def buscar_producto(self, nombre):
        """
        Busca un producto por nombre.
        
        Args:
            nombre: Nombre del producto a buscar
            
        Returns:
            Objeto Producto si lo encuentra, None si no existe
        """
        for producto in self.productos:
            if producto.nombre.lower() == nombre.lower():
                print(f"\n{'='*70}")
                print(f"  RESULTADO DE BÚSQUEDA")
                print(f"{'='*70}")
                print(f"✓ Encontrado: {producto.mostrar_informacion()}")
                print(f"{'='*70}\n")
                return producto
        
        print(f"\n✗ Producto '{nombre}' no encontrado.\n")
        return None
    
    # ============ MÉTODOS PARA CLIENTES ============
    
    def registrar_cliente(self, nombre, correo):
        """
        Registra un nuevo cliente en el restaurante.
        
        Args:
            nombre: Nombre del cliente
            correo: Correo del cliente
            
        Returns:
            Objeto Cliente creado
        """
        from modelos import Cliente
        
        cliente = Cliente(
            id_cliente=self.proximo_id_cliente,
            nombre=nombre,
            correo=correo
        )
        self.clientes.append(cliente)
        self.proximo_id_cliente += 1
        print(f"✓ Cliente '{cliente.nombre}' registrado exitosamente. ID: {cliente.id_cliente}")
        return cliente
    
    def listar_clientes(self):
        """Muestra todos los clientes registrados en el restaurante."""
        print(f"\n{'='*70}")
        print(f"  CLIENTES REGISTRADOS")
        print(f"{'='*70}")
        
        if not self.clientes:
            print("No hay clientes registrados.")
            print(f"{'='*70}\n")
            return
        
        for idx, cliente in enumerate(self.clientes, 1):
            print(f"{idx}. {cliente}")
        
        print(f"{'='*70}\n")
    
    def buscar_cliente(self, nombre):
        """
        Busca un cliente por nombre.
        
        Args:
            nombre: Nombre del cliente a buscar
            
        Returns:
            Objeto Cliente si lo encuentra, None si no existe
        """
        for cliente in self.clientes:
            if cliente.nombre.lower() == nombre.lower():
                print(f"\n{'='*70}")
                print(f"  RESULTADO DE BÚSQUEDA")
                print(f"{'='*70}")
                print(f"✓ Encontrado: {cliente}")
                print(f"{'='*70}\n")
                return cliente
        
        print(f"\n✗ Cliente '{nombre}' no encontrado.\n")
        return None
    
    def obtener_estadisticas(self):
        """Retorna estadísticas del restaurante."""
        return {
            'total_productos': len(self.productos),
            'total_clientes': len(self.clientes)
        }
