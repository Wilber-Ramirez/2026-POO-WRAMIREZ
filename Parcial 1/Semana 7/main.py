from modelos import Producto, Cliente
from servicios import Restaurante


def mostrar_menu_principal():
    """Muestra el menú principal del sistema."""
    print("\n" + "="*50)
    print("    SISTEMA DE RESTAURANTE")
    print("="*50)
    print("1. Registrar producto")
    print("2. Listar productos")
    print("3. Buscar producto")
    print("-" * 50)
    print("4. Registrar cliente")
    print("5. Listar clientes")
    print("6. Buscar cliente")
    print("-" * 50)
    print("7. Salir")
    print("="*50)


def registrar_nuevo_producto(restaurante):
    """Permite al usuario registrar un nuevo producto."""
    try:
        print("\n--- REGISTRAR PRODUCTO ---")
        nombre = input("Nombre del producto: ").strip()
        if not nombre:
            print("✗ El nombre del producto no puede estar vacío.")
            return
        
        categoria = input("Categoría del producto: ").strip()
        if not categoria:
            print("✗ La categoría del producto no puede estar vacía.")
            return
        
        try:
            precio = float(input("Precio del producto: $"))
        except ValueError:
            print("✗ El precio debe ser un número válido.")
            return
        
        # Crear objeto Producto usando el constructor
        producto = Producto(
            nombre=nombre,
            categoria=categoria,
            precio=precio,
            disponible=True
        )
        
        restaurante.registrar_producto(producto)
    
    except ValueError as e:
        print(f"✗ Error: {e}")


def registrar_nuevo_cliente(restaurante):
    """Permite al usuario registrar un nuevo cliente."""
    try:
        print("\n--- REGISTRAR CLIENTE ---")
        nombre = input("Nombre del cliente: ").strip()
        if not nombre:
            print("✗ El nombre del cliente no puede estar vacío.")
            return
        
        correo = input("Correo del cliente: ").strip()
        if not correo:
            print("✗ El correo del cliente no puede estar vacío.")
            return
        
        # Registrar cliente usando el método del restaurante
        restaurante.registrar_cliente(nombre, correo)
    
    except Exception as e:
        print(f"✗ Error: {e}")


def buscar_producto(restaurante):
    """Permite al usuario buscar un producto."""
    nombre = input("\nIngrese el nombre del producto a buscar: ").strip()
    if not nombre:
        print("✗ Debe ingresar un nombre para buscar.")
        return
    
    restaurante.buscar_producto(nombre)


def buscar_cliente(restaurante):
    """Permite al usuario buscar un cliente."""
    nombre = input("\nIngrese el nombre del cliente a buscar: ").strip()
    if not nombre:
        print("✗ Debe ingresar un nombre para buscar.")
        return
    
    restaurante.buscar_cliente(nombre)


def main():
    """Función principal que ejecuta el sistema restaurante_app."""
    restaurante = Restaurante("La Buena Mesa")
    
    print("\n" + "="*50)
    print("  BIENVENIDO AL SISTEMA DE RESTAURANTE")
    print("="*50)
    
    while True:
        mostrar_menu_principal()
        opcion = input("Seleccione una opción (1-7): ").strip()
        
        if opcion == "1":
            registrar_nuevo_producto(restaurante)
        
        elif opcion == "2":
            restaurante.listar_productos()
        
        elif opcion == "3":
            buscar_producto(restaurante)
        
        elif opcion == "4":
            registrar_nuevo_cliente(restaurante)
        
        elif opcion == "5":
            restaurante.listar_clientes()
        
        elif opcion == "6":
            buscar_cliente(restaurante)
        
        elif opcion == "7":
            print("\n" + "="*50)
            print("  ¡Gracias por usar el sistema!")
            print("="*50 + "\n")
            break
        
        else:
            print("✗ Opción no válida. Intente de nuevo.")


if __name__ == "__main__":
    main()
