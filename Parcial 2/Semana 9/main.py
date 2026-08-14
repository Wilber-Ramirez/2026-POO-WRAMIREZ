from typing import Tuple, Dict
from restaurante_app.modelos.producto import Producto
from restaurante_app.modelos.usuario import Usuario
from restaurante_app.servicios.restaurante import Restaurante

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

def registrar_producto_ui() -> None:
    try:
        codigo = input("Código del producto: ").strip()
        nombre = input("Nombre: ").strip()
        categoria = input("Categoría: ").strip()
        precio_str = input("Precio: ").strip()
        precio = float(precio_str)
    except ValueError:
        print("Entrada inválida para el precio.")
        return

    producto = Producto(codigo=codigo, nombre=nombre, categoria=categoria, precio=precio)
    if restaurante.registrar_producto(producto):
        print("Producto registrado correctamente.")
    else:
        print("Error: código de producto duplicado.")


def buscar_producto_ui() -> None:
    codigo = input("Código a buscar: ").strip()
    p = restaurante.buscar_producto_por_codigo(codigo)
    if p:
        print(p)
    else:
        print("Producto no encontrado.")


def actualizar_producto_ui() -> None:
    codigo = input("Código del producto a actualizar: ").strip()
    p = restaurante.buscar_producto_por_codigo(codigo)
    if not p:
        print("Producto no encontrado.")
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
            print("Precio inválido.")
            return
    if restaurante.actualizar_producto(codigo, nombre or None, categoria or None, precio):
        print("Producto actualizado.")
    else:
        print("No se pudo actualizar el producto.")


def eliminar_producto_ui() -> None:
    codigo = input("Código del producto a eliminar: ").strip()
    if restaurante.eliminar_producto(codigo):
        print("Producto eliminado.")
    else:
        print("Producto no encontrado.")


def listar_productos_ui() -> None:
    productos = restaurante.listar_productos()
    if not productos:
        print("No hay productos registrados.")
        return
    for p in productos:
        print(p)


def registrar_usuario_ui() -> None:
    identificacion = input("Identificación: ").strip()
    nombre = input("Nombre: ").strip()
    correo = input("Correo: ").strip()
    usuario = Usuario(identificacion=identificacion, nombre=nombre, correo=correo)
    if restaurante.registrar_usuario(usuario):
        print("Usuario registrado.")
    else:
        print("Error: identificación duplicada.")


def listar_usuarios_ui() -> None:
    usuarios = restaurante.listar_usuarios()
    if not usuarios:
        print("No hay usuarios registrados.")
        return
    for u in usuarios:
        print(u)


def mostrar_categorias_ui() -> None:
    categorias = restaurante.obtener_categorias_unicas()
    if not categorias:
        print("No hay categorías registradas.")
        return
    for c in sorted(categorias):
        print(f"- {c}")


def main() -> None:
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
            print("Saliendo...")
            break
        accion = acciones.get(opcion)
        if accion:
            try:
                accion()
            except Exception as e:
                print(f"Ocurrió un error: {e}")
        else:
            print("Opción inválida.")

if __name__ == '__main__':
    main()
