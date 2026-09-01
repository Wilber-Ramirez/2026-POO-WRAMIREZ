from __future__ import annotations

import json
import os
from typing import List

from restaurante_app.modelos.producto import Producto
from restaurante_app.modelos.usuario import Usuario
from restaurante_app.modelos.venta import Venta


class ArchivoServicio:
    def __init__(self, ruta_directorio: str) -> None:
        self.ruta_directorio = ruta_directorio
        self._asegurar_directorio()

    def _asegurar_directorio(self) -> None:
        if self.ruta_directorio and not os.path.exists(self.ruta_directorio):
            os.makedirs(self.ruta_directorio, exist_ok=True)

    def _ruta_archivo(self, nombre_archivo: str) -> str:
        return os.path.join(self.ruta_directorio, nombre_archivo)

    def cargar_productos(self) -> List[Producto]:
        ruta = self._ruta_archivo("productos.json")
        if not os.path.exists(ruta):
            return []

        try:
            with open(ruta, "r", encoding="utf-8-sig") as archivo:
                datos = json.load(archivo)

            if not isinstance(datos, list):
                return []

            productos: List[Producto] = []
            for indice, registro in enumerate(datos):
                try:
                    productos.append(Producto.desde_diccionario(registro))
                except (KeyError, TypeError, ValueError) as exc:
                    print(f"Advertencia: registro inválido en productos.json en índice {indice}: {exc}")
            return productos
        except FileNotFoundError:
            return []
        except json.JSONDecodeError as exc:
            print(f"Error: productos.json contiene JSON inválido: {exc}")
            return []
        except PermissionError:
            print(f"Error: No tienes permisos de lectura sobre productos.json.")
            return []

    def guardar_productos(self, productos: List[Producto]) -> bool:
        ruta = self._ruta_archivo("productos.json")
        try:
            self._asegurar_directorio()
            with open(ruta, "w", encoding="utf-8") as archivo:
                json.dump([producto.a_diccionario() for producto in productos], archivo, ensure_ascii=False, indent=2)
            return True
        except PermissionError:
            print(f"Error: No tienes permisos de escritura sobre productos.json.")
            return False
        except (TypeError, ValueError) as exc:
            print(f"Error: no se pudieron serializar los productos: {exc}")
            return False

    def cargar_usuarios(self) -> List[Usuario]:
        ruta = self._ruta_archivo("usuarios.json")
        if not os.path.exists(ruta):
            return []

        try:
            with open(ruta, "r", encoding="utf-8-sig") as archivo:
                datos = json.load(archivo)

            if not isinstance(datos, list):
                return []

            usuarios: List[Usuario] = []
            for indice, registro in enumerate(datos):
                try:
                    usuarios.append(Usuario.desde_diccionario(registro))
                except (KeyError, TypeError, ValueError) as exc:
                    print(f"Advertencia: registro inválido en usuarios.json en índice {indice}: {exc}")
            return usuarios
        except FileNotFoundError:
            return []
        except json.JSONDecodeError as exc:
            print(f"Error: usuarios.json contiene JSON inválido: {exc}")
            return []
        except PermissionError:
            print(f"Error: No tienes permisos de lectura sobre usuarios.json.")
            return []

    def guardar_usuarios(self, usuarios: List[Usuario]) -> bool:
        ruta = self._ruta_archivo("usuarios.json")
        try:
            self._asegurar_directorio()
            with open(ruta, "w", encoding="utf-8") as archivo:
                json.dump([usuario.a_diccionario() for usuario in usuarios], archivo, ensure_ascii=False, indent=2)
            return True
        except PermissionError:
            print(f"Error: No tienes permisos de escritura sobre usuarios.json.")
            return False
        except (TypeError, ValueError) as exc:
            print(f"Error: no se pudieron serializar los usuarios: {exc}")
            return False

    def cargar_ventas(self) -> List[Venta]:
        ruta = self._ruta_archivo("ventas.json")
        if not os.path.exists(ruta):
            return []

        try:
            with open(ruta, "r", encoding="utf-8-sig") as archivo:
                datos = json.load(archivo)

            if not isinstance(datos, list):
                return []

            ventas: List[Venta] = []
            for indice, registro in enumerate(datos):
                try:
                    ventas.append(Venta.desde_diccionario(registro))
                except (KeyError, TypeError, ValueError) as exc:
                    print(f"Advertencia: registro inválido en ventas.json en índice {indice}: {exc}")
            return ventas
        except FileNotFoundError:
            return []
        except json.JSONDecodeError as exc:
            print(f"Error: ventas.json contiene JSON inválido: {exc}")
            return []
        except PermissionError:
            print(f"Error: No tienes permisos de lectura sobre ventas.json.")
            return []

    def guardar_ventas(self, ventas: List[Venta]) -> bool:
        ruta = self._ruta_archivo("ventas.json")
        try:
            self._asegurar_directorio()
            with open(ruta, "w", encoding="utf-8") as archivo:
                json.dump([venta.a_diccionario() for venta in ventas], archivo, ensure_ascii=False, indent=2)
            return True
        except PermissionError:
            print(f"Error: No tienes permisos de escritura sobre ventas.json.")
            return False
        except (TypeError, ValueError) as exc:
            print(f"Error: no se pudieron serializar las ventas: {exc}")
            return False
