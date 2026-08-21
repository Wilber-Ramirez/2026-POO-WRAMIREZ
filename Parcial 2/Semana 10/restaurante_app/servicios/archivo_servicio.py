import json
import os
from typing import List
from restaurante_app.modelos.producto import Producto


class ArchivoServicio:
    """Servicio responsable de la persistencia de productos en JSON."""

    def __init__(self, ruta_archivo: str) -> None:
        """
        Inicializa el servicio de archivo.
        
        Args:
            ruta_archivo: Ruta donde se almacena el archivo de productos.
        """
        self.ruta_archivo = ruta_archivo
        self._asegurar_directorio()

    def _asegurar_directorio(self) -> None:
        """Crea el directorio si no existe."""
        directorio = os.path.dirname(self.ruta_archivo)
        if directorio and not os.path.exists(directorio):
            os.makedirs(directorio, exist_ok=True)

    def cargar_productos(self) -> List[Producto]:
        """
        Carga los productos desde el archivo JSON.
        
        Returns:
            Lista de objetos Producto cargados del archivo.
            Si el archivo no existe, retorna una lista vacía.
            
        Raises:
            Controla excepciones específicas sin detener la aplicación.
        """
        productos = []

        try:
            if not os.path.exists(self.ruta_archivo):
                print(f"Archivo {self.ruta_archivo} no encontrado. Iniciando con colección vacía.")
                return productos

            with open(self.ruta_archivo, 'r', encoding='utf-8') as archivo:
                datos = json.load(archivo)

            if not isinstance(datos, list):
                print(f"Advertencia: El archivo contiene un formato inesperado. Se iniciará con colección vacía.")
                return productos

            for idx, registro in enumerate(datos):
                try:
                    producto = Producto.desde_diccionario(registro)
                    productos.append(producto)
                except ValueError as e:
                    print(f"Advertencia: Registro {idx} inválido y será ignorado. Detalles: {e}")
                except KeyError as e:
                    print(f"Advertencia: Registro {idx} incompleto (falta clave {e}). Será ignorado.")

        except FileNotFoundError:
            print(f"Archivo {self.ruta_archivo} no encontrado. Iniciando con colección vacía.")
        except json.JSONDecodeError as e:
            print(f"Error: El archivo JSON no tiene un formato válido. {e}. Se iniciará con colección vacía.")
        except PermissionError:
            print(f"Error: Permiso denegado al leer {self.ruta_archivo}. Se iniciará con colección vacía.")
        except Exception as e:
            print(f"Error inesperado al cargar productos: {e}. Se iniciará con colección vacía.")

        return productos

    def guardar_productos(self, productos: List[Producto]) -> bool:
        """
        Guarda los productos en el archivo JSON.
        
        Args:
            productos: Lista de objetos Producto a guardar.
            
        Returns:
            True si la operación fue exitosa, False en caso contrario.
        """
        try:
            self._asegurar_directorio()
            datos = [p.a_diccionario() for p in productos]

            with open(self.ruta_archivo, 'w', encoding='utf-8') as archivo:
                json.dump(datos, archivo, ensure_ascii=False, indent=2)

            return True

        except PermissionError:
            print(f"Error: Permiso denegado al escribir en {self.ruta_archivo}.")
            return False
        except TypeError as e:
            print(f"Error: No se pueden serializar los productos: {e}")
            return False
        except Exception as e:
            print(f"Error inesperado al guardar productos: {e}")
            return False
