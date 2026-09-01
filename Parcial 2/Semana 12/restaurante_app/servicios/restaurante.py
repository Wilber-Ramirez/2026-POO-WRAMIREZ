from __future__ import annotations

import os
from typing import Dict, List, Optional

from restaurante_app.modelos.producto import Producto
from restaurante_app.modelos.usuario import Usuario
from restaurante_app.modelos.venta import Venta
from restaurante_app.servicios.archivo_servicio import ArchivoServicio


class Restaurante:
    def __init__(self, ruta_datos: Optional[str] = None) -> None:
        if ruta_datos is None:
            ruta_datos = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "datos"))

        self._archivo_servicio = ArchivoServicio(ruta_datos)
        self._productos: List[Producto] = self._archivo_servicio.cargar_productos()
        self._usuarios: List[Usuario] = self._archivo_servicio.cargar_usuarios()
        self._ventas: List[Venta] = self._archivo_servicio.cargar_ventas()

        # Índices en memoria para búsquedas rápidas por clave única
        self._indice_productos: Dict[str, Producto] = {p.codigo: p for p in self._productos}
        self._indice_usuarios: Dict[str, Usuario] = {u.identificacion: u for u in self._usuarios}
        # Mapa de usuario_id -> lista de ventas para evitar recorrer todas las ventas
        self._ventas_por_usuario: Dict[str, List[Venta]] = {}
        for venta in self._ventas:
            self._ventas_por_usuario.setdefault(venta.usuario_id, []).append(venta)

    def buscar_producto(self, codigo: str) -> Optional[Producto]:
        return self._indice_productos.get(codigo)

    def buscar_usuario(self, identificacion: str) -> Optional[Usuario]:
        return self._indice_usuarios.get(identificacion)

    def registrar_producto(self, producto: Producto) -> bool:
        if producto.codigo in self._indice_productos:
            return False

        self._productos.append(producto)
        self._indice_productos[producto.codigo] = producto
        self._archivo_servicio.guardar_productos(self._productos)
        return True

    def actualizar_producto(
        self,
        codigo: str,
        nombre: Optional[str] = None,
        categoria: Optional[str] = None,
        precio: Optional[float] = None,
        stock: Optional[int] = None,
    ) -> bool:
        producto = self._indice_productos.get(codigo)
        if producto is None:
            return False

        if nombre is not None and nombre.strip():
            producto.nombre = nombre.strip()
        if categoria is not None and categoria.strip():
            producto.categoria = categoria.strip()
        if precio is not None:
            if precio < 0:
                raise ValueError("El precio no puede ser negativo.")
            producto.precio = float(precio)
        if stock is not None:
            if stock < 0:
                raise ValueError("El stock no puede ser negativo.")
            producto.stock = int(stock)

        # La instancia del producto ya está en la lista principal, solo es necesario persistir
        self._archivo_servicio.guardar_productos(self._productos)
        return True

    def eliminar_producto(self, codigo: str) -> bool:
        producto = self._indice_productos.get(codigo)
        if producto is None:
            return False

        try:
            self._productos.remove(producto)
        except ValueError:
            pass
        del self._indice_productos[codigo]
        self._archivo_servicio.guardar_productos(self._productos)
        return True

    def listar_productos(self) -> List[Producto]:
        return list(self._productos)

    def registrar_usuario(self, usuario: Usuario) -> bool:
        if usuario.identificacion in self._indice_usuarios:
            return False

        self._usuarios.append(usuario)
        self._indice_usuarios[usuario.identificacion] = usuario
        self._archivo_servicio.guardar_usuarios(self._usuarios)
        return True

    def listar_usuarios(self) -> List[Usuario]:
        return list(self._usuarios)

    def vender_producto(self, codigo_producto: str, identificacion_usuario: str, cantidad: int) -> bool:
        usuario = self._indice_usuarios.get(identificacion_usuario)
        producto = self._indice_productos.get(codigo_producto)

        if usuario is None or producto is None:
            return False
        if cantidad <= 0 or producto.stock < cantidad:
            return False

        venta = Venta(usuario.identificacion, producto.codigo, cantidad)
        self._ventas.append(venta)
        # Mantener índice de ventas por usuario actualizado
        self._ventas_por_usuario.setdefault(usuario.identificacion, []).append(venta)

        producto.vender(cantidad)

        self._archivo_servicio.guardar_ventas(self._ventas)
        self._archivo_servicio.guardar_productos(self._productos)
        return True

    def ventas_por_usuario(self, identificacion_usuario: str) -> List[Venta]:
        # Usar el índice en memoria para devolver las ventas relacionadas
        return list(self._ventas_por_usuario.get(identificacion_usuario, []))

    def listar_ventas(self) -> List[Venta]:
        return list(self._ventas)
