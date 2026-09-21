from __future__ import annotations

from pathlib import Path

from restaurante_app.modelos.producto import Producto
from restaurante_app.modelos.usuario import Usuario
from restaurante_app.modelos.venta import Venta
from restaurante_app.servicios.archivo_servicio import ArchivoServicio


class RestauranteServicio:
    def __init__(self, ruta_datos: str | Path | None = None) -> None:
        base = Path(__file__).resolve().parents[1]
        self.archivos = ArchivoServicio(ruta_datos or base / "datos")
        self._productos = self.archivos.cargar_productos()
        self._usuarios = self.archivos.cargar_usuarios()
        self._ventas = self.archivos.cargar_ventas()

    def autenticar(self, identificacion: str, contrasena: str) -> Usuario | None:
        return next((u for u in self._usuarios
                     if u.identificacion == identificacion.strip() and u.contrasena == contrasena), None)

    def listar_usuarios(self) -> list[Usuario]:
        return list(self._usuarios)

    def buscar_usuario(self, identificacion: str) -> Usuario | None:
        return next((u for u in self._usuarios if u.identificacion == identificacion.strip()), None)

    def buscar_producto(self, codigo: str) -> Producto | None:
        return next((p for p in self._productos if p.codigo == codigo.strip()), None)

    def listar_productos(self) -> list[Producto]:
        return list(self._productos)

    def registrar_producto(self, producto: Producto) -> bool:
        if self.buscar_producto(producto.codigo):
            return False
        self._productos.append(producto)
        self.archivos.guardar_productos(self._productos)
        return True

    def actualizar_producto(self, codigo: str, nombre: str, categoria: str,
                            precio: float, stock: int) -> bool:
        producto = self.buscar_producto(codigo)
        if producto is None:
            return False
        producto.nombre = Producto._campo(nombre, "nombre")
        producto.categoria = Producto._campo(categoria, "categoria")
        if precio < 0 or stock < 0:
            raise ValueError("Precio y stock deben ser mayores o iguales a cero.")
        producto.precio, producto.stock = float(precio), int(stock)
        self.archivos.guardar_productos(self._productos)
        return True

    def eliminar_producto(self, codigo: str) -> bool:
        producto = self.buscar_producto(codigo)
        if producto is None:
            return False
        self._productos.remove(producto)
        self.archivos.guardar_productos(self._productos)
        return True

    def listar_ventas(self) -> list[Venta]:
        return list(self._ventas)

    def registrar_venta(self, usuario_id: str, producto_codigo: str) -> Venta:
        usuario = self.buscar_usuario(usuario_id)
        producto = self.buscar_producto(producto_codigo)
        if usuario is None:
            raise ValueError("El usuario seleccionado no existe.")
        if producto is None:
            raise ValueError("El producto seleccionado no existe.")
        venta = Venta(usuario.identificacion, producto.codigo)
        self._ventas.append(venta)
        self.archivos.guardar_ventas(self._ventas)
        return venta
