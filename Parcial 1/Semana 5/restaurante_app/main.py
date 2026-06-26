# Punto de entrada del sistema de gestión de restaurante
# Este archivo crea objetos de Producto y Cliente, los agrega al Restaurante y muestra la información

from modelos.producto import Producto
from modelos.cliente import Cliente
from servicios.restaurante import Restaurante


def main() -> None:
    """
    Función principal que ejecuta el sistema de gestión de restaurante.
    Crea productos, clientes, los agrega a un restaurante y muestra la información.
    """

    restaurante_principal = Restaurante(
        nombre_restaurante="El Buen Sabor",
        direccion="Calle Principal 123, Centro"
    )
    
    print("Sistema de Gestión de Restaurante")
    print("-" * 40)

    producto_1 = Producto(
        codigo=101,
        nombre="Hamburguesa Clásica",
        descripcion="Hamburguesa hecha con carne de res premium y salsas caseras",
        precio=15.99,
        disponible=True
    )
    producto_2 = Producto(
        codigo=102,
        nombre="Ensalada César",
        descripcion="Ensalada fresca con lechuga romana, crutones y aderezo César",
        precio=12.50,
        disponible=True
    )
    producto_3 = Producto(
        codigo=103,
        nombre="Limonada Casera",
        descripcion="Bebida refrescante preparada con limones naturales",
        precio=3.99,
        disponible=False
    )
    cliente_1 = Cliente(
        cedula=2400203618,
        nombre="Luis Garcia Bone",
        correo_electronico="joseluis@gmail.com",
        telefono="+593 988283641",
        es_miembro_frecuente=True
    )
    cliente_2 = Cliente(
        cedula=1068355001,
        nombre="Wilber Ramirez Lindao",
        correo_electronico="rlwilber02@gmail.com",
        telefono="+593 961346061",
        es_miembro_frecuente=False
    )
    cliente_3 = Cliente(
        cedula=2400361507,
        nombre="Edson Suarez Lindao",
        correo_electronico="edson.suarez@gmail.com",
        telefono="+593 981656466",
        es_miembro_frecuente=True
    )

    restaurante_principal.agregar_producto(producto_1)
    restaurante_principal.agregar_producto(producto_2)
    restaurante_principal.agregar_producto(producto_3)

    restaurante_principal.agregar_cliente(cliente_1)
    restaurante_principal.agregar_cliente(cliente_2)
    restaurante_principal.agregar_cliente(cliente_3)

    restaurante_principal.mostrar_informacion_completa()

    print("\n=== DETALLES DE PRODUCTOS ===")
    for producto in restaurante_principal.lista_productos:
        print(f"  • {producto.obtener_informacion_completa()}")
    
    print("\n=== DETALLES DE CLIENTES ===")
    for cliente in restaurante_principal.lista_clientes:
        print(f"  • {cliente.nombre}")
        print(f"    {cliente.obtener_informacion_contacto()}")

    print("\n=== CAMBIOS EN EL SISTEMA ===")
    cliente_2.convertir_a_miembro_frecuente()
    print(f"✓ {cliente_2.nombre} ahora es miembro frecuente.")
    
    producto_3.cambiar_disponibilidad(True)
    print(f"✓ {producto_3.nombre} ahora está disponible.")

    print("\n=== INFORMACIÓN ACTUALIZADA ===")
    restaurante_principal.mostrar_informacion_completa()


if __name__ == "__main__":
    main()
