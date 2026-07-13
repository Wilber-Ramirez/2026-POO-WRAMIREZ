# Punto de entrada del sistema - Menú interactivo
from modelos import Producto, Bebida, Cliente
from servicios import Restaurante


def mostrar_menu_principal() -> None:
    """Muestra el menú principal del sistema."""
    print("\n" + "="*50)
    print("    SISTEMA DE RESTAURANTE")
    print("="*50)
    print("1. Registrar producto")
    print("2. Registrar bebida")
    print("3. Registrar cliente")
    print("-" * 50)
    print("4. Listar productos")
    print("5. Listar clientes")
    print("-" * 50)
    print("6. Salir")
    print("="*50)


def registrar_producto(restaurante: Restaurante) -> None:
    """Permite al usuario registrar un nuevo producto."""
    try:
        print("\n--- REGISTRAR PRODUCTO ---")
        codigo = input("Código del producto: ").strip()
        nombre = input("Nombre del producto: ").strip()
        categoria = input("Categoría del producto: ").strip()
        
        try:
            precio = float(input("Precio del producto: $"))
        except ValueError:
            print("✗ El precio debe ser un número válido.")
            return
        
        # Crear objeto Producto usando el constructor
        producto = Producto(
            codigo=codigo,
            nombre=nombre,
            categoria=categoria,
            precio=precio
        )
        
        restaurante.registrar_producto(producto)
    
    except ValueError as e:
        print(f"✗ Error: {e}")


def registrar_bebida(restaurante: Restaurante) -> None:
    """Permite al usuario registrar una nueva bebida."""
    try:
        print("\n--- REGISTRAR BEBIDA ---")
        codigo = input("Código de la bebida: ").strip()
        nombre = input("Nombre de la bebida: ").strip()
        categoria = input("Categoría de la bebida: ").strip()
        
        try:
            precio = float(input("Precio de la bebida: $"))
            tamaño = int(input("Tamaño en mililitros (ml): "))
        except ValueError:
            print("✗ El precio y tamaño deben ser números válidos.")
            return
        
        tipo_envase = input("Tipo de envase (Lata, Botella, Vaso, etc.): ").strip()
        
        # Crear objeto Bebida usando el constructor
        bebida = Bebida(
            codigo=codigo,
            nombre=nombre,
            categoria=categoria,
            precio=precio,
            tamaño_ml=tamaño,
            tipo_envase=tipo_envase
        )
        
        restaurante.registrar_producto(bebida)
    
    except ValueError as e:
        print(f"✗ Error: {e}")


def registrar_cliente(restaurante: Restaurante) -> None:
    """Permite al usuario registrar un nuevo cliente."""
    try:
        print("\n--- REGISTRAR CLIENTE ---")
        identificacion = input("Identificación del cliente: ").strip()
        nombre = input("Nombre del cliente: ").strip()
        correo = input("Correo del cliente: ").strip()
        
        # Crear objeto Cliente usando el constructor
        cliente = Cliente(
            identificacion=identificacion,
            nombre=nombre,
            correo=correo
        )
        
        restaurante.registrar_cliente(cliente)
    
    except ValueError as e:
        print(f"✗ Error: {e}")


def main() -> None:
    """Función principal que ejecuta el sistema restaurante_app."""
    restaurante = Restaurante("La Buena Mesa")
    
    print("\n" + "="*50)
    print("  BIENVENIDO AL SISTEMA DE RESTAURANTE")
    print("="*50)
    
    while True:
        mostrar_menu_principal()
        opcion = input("Seleccione una opción (1-6): ").strip()
        
        if opcion == "1":
            registrar_producto(restaurante)
        
        elif opcion == "2":
            registrar_bebida(restaurante)
        
        elif opcion == "3":
            registrar_cliente(restaurante)
        
        elif opcion == "4":
            restaurante.listar_productos()
        
        elif opcion == "5":
            restaurante.listar_clientes()
        
        elif opcion == "6":
            print("\n" + "="*50)
            print("  ¡Gracias por usar el sistema!")
            print("="*50 + "\n")
            break
        
        else:
            print("✗ Opción no válida. Intente de nuevo.")


if __name__ == "__main__":
    main()
