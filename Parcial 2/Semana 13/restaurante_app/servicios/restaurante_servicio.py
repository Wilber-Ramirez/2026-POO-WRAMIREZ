from __future__ import annotations

import os
from typing import Dict, List, Optional

from restaurante_app.modelos.producto import Producto
from restaurante_app.modelos.usuario import Usuario
from restaurante_app.servicios.archivo_servicio import ArchivoServicio


class RestauranteServicio:
    """Servicio que expone operaciones de lectura y validación para la UI."""

    def __init__(self, ruta_datos: Optional[str] = None) -> None:
        if ruta_datos is None:
            ruta_datos = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "datos"))

        self._archivo = ArchivoServicio(ruta_datos)
        self._productos: List[Producto] = self._archivo.cargar_productos()
        self._usuarios: List[Usuario] = self._archivo.cargar_usuarios()

        # índices en memoria
        self._indice_productos: Dict[str, Producto] = {p.codigo: p for p in self._productos}
        self._indice_usuarios: Dict[str, Usuario] = {u.identificacion: u for u in self._usuarios}

    def listar_productos(self) -> List[Producto]:
        return list(self._productos)

    def listar_usuarios(self) -> List[Usuario]:
        return list(self._usuarios)

    def validar_acceso(self, identificacion: str, clave: str) -> bool:
        """Validación pedagógica: la 'clave' es comparada con el correo del usuario en los datos.
        No es autenticación real.
        """
        if not identificacion or not clave:
            return False
        usuario = self._indice_usuarios.get(identificacion)
        if usuario is None:
            return False
        return usuario.correo == clave
