from __future__ import annotations

import sys
from pathlib import Path

if __package__ is None or __package__ == "":
    sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from restaurante_app.modelos.producto import Producto
from restaurante_app.modelos.usuario import Usuario
from restaurante_app.servicios.restaurante import Restaurante


def menu() -> None:
    print("\n=== RESTAURANTE APP ===")
    print("1. Registrar usuario")
    print("2. Listar usuarios")
    print("3. Registrar producto")
    print("4. Listar productos")
    print("5. Vender producto")
    print("6. Consultar ventas por usuario")
    print("7. Salir")


def ingresar_usuario(restaurante: Restaurante) -> None:
    identificacion = input("Identificación del usuario: ").strip()
    nombre = input("Nombre del usuario: ").strip()
    correo = input("Correo del usuario: ").strip()

    try:
        usuario = Usuario(identificacion, nombre, correo)
        if restaurante.registrar_usuario(usuario):
            print("Usuario registrado correctamente.")
        else:
            print("No se pudo registrar el usuario. Ya existe un usuario con esa identificación.")
    except ValueError as exc:
        print(f"Error: {exc}")


def ingresar_producto(restaurante: Restaurante) -> None:
    codigo = input("Código del producto: ").strip()
    nombre = input("Nombre del producto: ").strip()
    categoria = input("Categoría del producto: ").strip()
    try:
        precio = float(input("Precio del producto: ").strip())
        stock = int(input("Stock disponible: ").strip())
        producto = Producto(codigo, nombre, categoria, precio)
        if restaurante.registrar_producto(producto):
            print("Producto registrado correctamente.")
        else:
            print("No se pudo registrar el producto. Ya existe un producto con ese código.")
    except ValueError as exc:
        print(f"Error: {exc}")


def vender_producto(restaurante: Restaurante) -> None:
    identificacion = input("Identificación del usuario: ").strip()
    codigo = input("Código del producto: ").strip()
    try:
        cantidad = int(input("Cantidad a vender: ").strip())
        if restaurante.vender_producto(codigo, identificacion, cantidad):
            print("Venta registrada correctamente.")
        else:
            print("La venta no se pudo completar. Verifica usuario, producto, stock y cantidad.")
    except ValueError as exc:
        print(f"Error: {exc}")


def consultar_ventas(restaurante: Restaurante) -> None:
    identificacion = input("Identificación del usuario: ").strip()
    ventas = restaurante.ventas_por_usuario(identificacion)

    if not ventas:
        print("No se encontraron ventas para ese usuario.")
        return

    print(f"Ventas realizadas por {identificacion}:")
    for venta in ventas:
        producto = restaurante.buscar_producto(venta.producto_codigo)
        nombre_producto = producto.nombre if producto is not None else "Producto no encontrado"
        print(f"- {producto.codigo if producto else venta.producto_codigo} | {nombre_producto} | Cantidad: {venta.cantidad}")


def listar_usuarios(restaurante: Restaurante) -> None:
    usuarios = restaurante.listar_usuarios()
    if not usuarios:
        print("No hay usuarios registrados.")
        return

    for usuario in usuarios:
        print(usuario)


def listar_productos(restaurante: Restaurante) -> None:
    productos = restaurante.listar_productos()
    if not productos:
        print("No hay productos registrados.")
        return

    for producto in productos:
        print(producto)


def main() -> None:
    restaurante = Restaurante()

    while True:
        menu()
        opcion = input("Seleccione una opción: ").strip()

        if opcion == "1":
            ingresar_usuario(restaurante)
        elif opcion == "2":
            listar_usuarios(restaurante)
        elif opcion == "3":
            ingresar_producto(restaurante)
        elif opcion == "4":
            listar_productos(restaurante)
        elif opcion == "5":
            vender_producto(restaurante)
        elif opcion == "6":
            consultar_ventas(restaurante)
        elif opcion == "7":
            print("Gracias por usar el sistema.")
            break
        else:
            print("Opción no válida. Intente nuevamente.")


if __name__ == "__main__":
    main()
