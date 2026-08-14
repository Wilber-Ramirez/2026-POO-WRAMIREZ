from typing import List, Optional, Set
from restaurante_app.modelos.producto import Producto
from restaurante_app.modelos.usuario import Usuario

class Restaurante:
    def __init__(self) -> None:
        self._productos: List[Producto] = []
        self._usuarios: List[Usuario] = []

    # Productos
    def registrar_producto(self, producto: Producto) -> bool:
        if self.buscar_producto_por_codigo(producto.codigo) is not None:
            return False
        self._productos.append(producto)
        return True

    def buscar_producto_por_codigo(self, codigo: str) -> Optional[Producto]:
        for p in self._productos:
            if p.codigo == codigo:
                return p
        return None

    def actualizar_producto(self, codigo: str, nombre: Optional[str] = None,
                             categoria: Optional[str] = None, precio: Optional[float] = None) -> bool:
        p = self.buscar_producto_por_codigo(codigo)
        if p is None:
            return False
        if nombre is not None and nombre != '':
            p.nombre = nombre
        if categoria is not None and categoria != '':
            p.categoria = categoria
        if precio is not None:
            p.precio = precio
        return True

    def eliminar_producto(self, codigo: str) -> bool:
        p = self.buscar_producto_por_codigo(codigo)
        if p is None:
            return False
        self._productos.remove(p)
        return True

    def listar_productos(self) -> List[Producto]:
        return list(self._productos)

    # Usuarios
    def registrar_usuario(self, usuario: Usuario) -> bool:
        if any(u.identificacion == usuario.identificacion for u in self._usuarios):
            return False
        self._usuarios.append(usuario)
        return True

    def listar_usuarios(self) -> List[Usuario]:
        return list(self._usuarios)

    # Otras utilidades
    def obtener_categorias_unicas(self) -> Set[str]:
        return set(p.categoria for p in self._productos)
