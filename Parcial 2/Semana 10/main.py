from typing import Tuple, Dict
import os
from restaurante_app.modelos.producto import Producto
from restaurante_app.modelos.usuario import Usuario
from restaurante_app.servicios.restaurante import Restaurante
from restaurante_app.servicios.archivo_servicio import ArchivoServicio

MENU: Tuple[str, ...] = (
    "1. Registrar producto",
    "2. Buscar producto",
    "3. Actualizar producto",
    "4. Eliminar producto",
    "5. Listar productos",
    "6. Registrar usuario",
    "7. Listar usuarios",
    "8. Mostrar categorías",
    "9. Salir",
)

restaurante = Restaurante()
ruta_productos = os.path.join(os.path.dirname(__file__), "datos", "productos.json")
archivo_servicio = ArchivoServicio(ruta_productos)


def cargar_productos_al_inicio() -> None:
    """Carga los productos almacenados al iniciar la aplicación."""
    productos_cargados = archivo_servicio.cargar_productos()
    restaurante.cargar_productos(productos_cargados)
    print(f"✓ {len(productos_cargados)} producto(s) cargado(s) desde el archivo.\n")


def guardar_productos() -> bool:
    """Guarda los productos actuales en el archivo JSON."""
    return archivo_servicio.guardar_productos(restaurante.listar_productos())


def registrar_producto_ui() -> None:
    try:
        codigo = input("Código del producto: ").strip()
        nombre = input("Nombre: ").strip()
        categoria = input("Categoría: ").strip()
        precio_str = input("Precio: ").strip()
        precio = float(precio_str)

        producto = Producto(codigo=codigo, nombre=nombre, categoria=categoria, precio=precio)

        if restaurante.registrar_producto(producto):
            if guardar_productos():
                print("✓ Producto registrado y guardado correctamente.")
            else:
                print("⚠ Producto registrado en memoria, pero no se guardó en el archivo.")
        else:
            print("✗ Error: código de producto duplicado.")
    except ValueError as e:
        print(f"✗ Error: {e}")


def buscar_producto_ui() -> None:
    codigo = input("Código a buscar: ").strip()
    p = restaurante.buscar_producto_por_codigo(codigo)
    if p:
        print(p)
    else:
        print("✗ Producto no encontrado.")


def actualizar_producto_ui() -> None:
    codigo = input("Código del producto a actualizar: ").strip()
    p = restaurante.buscar_producto_por_codigo(codigo)
    if not p:
        print("✗ Producto no encontrado.")
        return
    print(f"Producto actual: {p}")
    nombre = input("Nuevo nombre (enter para mantener): ").strip()
    categoria = input("Nueva categoría (enter para mantener): ").strip()
    precio_str = input("Nuevo precio (enter para mantener): ").strip()
    precio = None
    if precio_str != '':
        try:
            precio = float(precio_str)
        except ValueError:
            print("✗ Precio inválido.")
            return
    if restaurante.actualizar_producto(codigo, nombre or None, categoria or None, precio):
        if guardar_productos():
            print("✓ Producto actualizado y guardado correctamente.")
        else:
            print("⚠ Producto actualizado en memoria, pero no se guardó en el archivo.")
    else:
        print("✗ No se pudo actualizar el producto.")


def eliminar_producto_ui() -> None:
    codigo = input("Código del producto a eliminar: ").strip()
    if restaurante.eliminar_producto(codigo):
        if guardar_productos():
            print("✓ Producto eliminado y guardado correctamente.")
        else:
            print("⚠ Producto eliminado de memoria, pero los cambios no se guardaron en el archivo.")
    else:
        print("✗ Producto no encontrado.")


def listar_productos_ui() -> None:
    productos = restaurante.listar_productos()
    if not productos:
        print("No hay productos registrados.")
        return
    print("\n--- Lista de Productos ---")
    for p in productos:
        print(f"  {p}")
    print()


def registrar_usuario_ui() -> None:
    identificacion = input("Identificación: ").strip()
    nombre = input("Nombre: ").strip()
    correo = input("Correo: ").strip()
    usuario = Usuario(identificacion=identificacion, nombre=nombre, correo=correo)
    if restaurante.registrar_usuario(usuario):
        print("✓ Usuario registrado.")
    else:
        print("✗ Error: identificación duplicada.")


def listar_usuarios_ui() -> None:
    usuarios = restaurante.listar_usuarios()
    if not usuarios:
        print("No hay usuarios registrados.")
        return
    print("\n--- Lista de Usuarios ---")
    for u in usuarios:
        print(f"  {u}")
    print()


def mostrar_categorias_ui() -> None:
    categorias = restaurante.obtener_categorias_unicas()
    if not categorias:
        print("No hay categorías registradas.")
        return
    print("\n--- Categorías Disponibles ---")
    for c in sorted(categorias):
        print(f"  - {c}")
    print()


def main() -> None:
    print("\n========================================")
    print("    SISTEMA DE RESTAURANTE - Semana 10")
    print("        (Persistencia de Productos)")
    print("========================================\n")

    cargar_productos_al_inicio()

    acciones: Dict[str, callable] = {
        '1': registrar_producto_ui,
        '2': buscar_producto_ui,
        '3': actualizar_producto_ui,
        '4': eliminar_producto_ui,
        '5': listar_productos_ui,
        '6': registrar_usuario_ui,
        '7': listar_usuarios_ui,
        '8': mostrar_categorias_ui,
    }

    while True:
        print("\n========================================")
        print("        SISTEMA DE RESTAURANTE")
        print("========================================")
        for item in MENU:
            print(item)
        opcion = input("Seleccione una opción: ").strip()
        if opcion == '9':
            print("\n✓ Saliendo del sistema...")
            break
        accion = acciones.get(opcion)
        if accion:
            try:
                accion()
            except Exception as e:
                print(f"✗ Ocurrió un error: {e}")
        else:
            print("✗ Opción inválida.")


if __name__ == '__main__':
    main()
