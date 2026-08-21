# Restaurante App - Semana 10: Persistencia de Productos mediante JSON

## Descripción General

Esta es la **versión 2.0** del proyecto `restaurante_app`, que incorpora un sistema de persistencia para productos mediante archivos JSON. Los productos registrados se guardan automáticamente en un archivo externo, permitiendo que se conserven entre ejecuciones de la aplicación.

## Mejoras de la Semana 10

### Persistencia de Datos
- **Guardado automático**: Cada vez que se registra, actualiza o elimina un producto, los cambios se persisten inmediatamente en `datos/productos.json`.
- **Carga al iniciar**: Cuando la aplicación se ejecuta, todos los productos almacenados se recuperan del archivo JSON y se reconstruyen como objetos `Producto`.
- **Sin pérdida de datos**: Los productos no se pierden al cerrar la aplicación.

### Arquitectura Mejorada
- **ArchivoServicio**: Nuevo servicio centralizado para la lectura y escritura de archivos JSON.
- **Métodos de Serialización**: La clase `Producto` ahora incluye métodos para convertirse a diccionario y reconstruirse desde diccionarios.
- **Separación de Responsabilidades**: `main.py` coordina el flujo, `Restaurante` gestiona la lógica, `ArchivoServicio` maneja la persistencia.

### Manejo de Excepciones Mejorado
Se han implementado controles para las siguientes situaciones:
- **FileNotFoundError**: Si el archivo no existe en el primer inicio, la aplicación inicia con una colección vacía.
- **json.JSONDecodeError**: Si el archivo contiene JSON inválido, se registra la advertencia y se inicia con colección vacía.
- **PermissionError**: Si no hay permisos para leer o escribir, se muestra un mensaje de error.
- **KeyError y ValueError**: Los registros incompletos o inválidos se ignoran individualmente sin detener la aplicación.

## Estructura del Proyecto

```
Semana 10/
├── datos/
│   └── productos.json              # Archivo de persistencia (se crea al guardar)
├── restaurante_app/
│   ├── __init__.py
│   ├── modelos/
│   │   ├── __init__.py
│   │   ├── producto.py             # Clase Producto con serialización
│   │   └── usuario.py              # Clase Usuario
│   └── servicios/
│       ├── __init__.py
│       ├── archivo_servicio.py     # Nuevo servicio de persistencia
│       └── restaurante.py          # Servicio principal
├── main.py                         # Punto de entrada mejorado
└── README.md                       # Este archivo
```

## Cómo Usar

### Requisitos
- Python 3.7+
- No requiere dependencias externas (usa módulos estándar: `json`, `os`, `dataclasses`, `typing`)

### Instalación y Ejecución

1. **Clonar el repositorio**:
   ```bash
   git clone <URL_del_repositorio>
   cd Semana\ 10
   ```

2. **Ejecutar la aplicación**:
   ```bash
   python main.py
   ```

### Flujo de Uso

#### Primer Inicio
1. La aplicación verifica si existe `datos/productos.json`
2. Si no existe, inicia con una colección vacía
3. Se muestra el menú principal

#### Registrar un Producto
1. Seleccione la opción "1. Registrar producto"
2. Ingrese: código, nombre, categoría y precio
3. El producto se registra y **se guarda inmediatamente** en el archivo JSON

#### Persistencia Entre Ejecuciones
1. Registre algunos productos
2. Cierre la aplicación (opción 9)
3. Ejecute nuevamente `python main.py`
4. Los productos anteriores estarán disponibles

#### Actualizar un Producto
1. Seleccione la opción "3. Actualizar producto"
2. Ingrese el código del producto
3. Modifique los campos deseados
4. Los cambios se guardan en el archivo JSON

#### Eliminar un Producto
1. Seleccione la opción "4. Eliminar producto"
2. Ingrese el código del producto
3. El producto se elimina y el archivo se actualiza

### Formato del Archivo JSON

El archivo `datos/productos.json` contiene un arreglo de objetos con la siguiente estructura:

```json
[
  {
    "codigo": "P001",
    "nombre": "Hamburguesa",
    "categoria": "Platos Principales",
    "precio": 12.5
  },
  {
    "codigo": "P002",
    "nombre": "Ensalada César",
    "categoria": "Entradas",
    "precio": 8.99
  }
]
```

## Componentes Principales

### Producto (`modelos/producto.py`)
- **Atributos**: código, nombre, categoría, precio
- **Validaciones**: Valida que ningún campo esté vacío y que el precio sea no-negativo
- **Métodos nuevos**:
  - `a_diccionario()`: Convierte el producto a un diccionario para serialización
  - `desde_diccionario(datos)`: Método estático que reconstruye un producto desde un diccionario

### Usuario (`modelos/usuario.py`)
- Entidad general del sistema
- Permanece en memoria durante esta semana (no se persiste)

### Restaurante (`servicios/restaurante.py`)
- Gestiona las colecciones de productos y usuarios
- Métodos para registrar, buscar, actualizar, eliminar y listar productos
- Método `obtener_productos_dict()` para obtener productos en formato diccionario

### ArchivoServicio (`servicios/archivo_servicio.py`) - NUEVO
- **Responsabilidad**: Centralizar toda la lectura y escritura de archivos JSON
- **Métodos principales**:
  - `cargar_productos()`: Lee el archivo JSON y retorna una lista de objetos Producto
  - `guardar_productos(productos)`: Guarda una lista de Producto al archivo JSON
- **Manejo de excepciones**:
  - Controla `FileNotFoundError`, `json.JSONDecodeError`, `PermissionError`
  - Valida cada registro y ignora los inválidos
  - Registra advertencias sin detener la aplicación

### main.py
- Punto de entrada de la aplicación
- Crea las instancias de `Restaurante` y `ArchivoServicio`
- Carga productos al iniciar
- Coordina el menú interactivo
- Llama a `guardar_productos()` después de operaciones que modifican la colección

## Flujo de Carga

```
Inicio de la aplicación
    ↓
main.py crea ArchivoServicio
    ↓
Se intenta leer datos/productos.json
    ↓
json.load() recupera la información
    ↓
Se valida la estructura obtenida
    ↓
Cada registro válido se convierte en Producto(...)
    ↓
Los objetos se entregan al servicio Restaurante
    ↓
El menú trabaja normalmente con objetos Producto
```

## Flujo de Guardado

```
Usuario registra/actualiza/elimina un producto
    ↓
main.py solicita la operación al servicio Restaurante
    ↓
Restaurante modifica la colección en memoria
    ↓
Los objetos Producto se convierten a diccionarios
    ↓
ArchivoServicio utiliza json.dump()
    ↓
Se actualiza datos/productos.json
```

## Validación de Persistencia

### Prueba Minima Recomendada

1. **Ejecutar main.py**
   ```bash
   python main.py
   ```

2. **Registrar productos**
   - Opción 1
   - Producto 1: código "P001", nombre "Hamburguesa", categoría "Platos", precio 15.5
   - Producto 2: código "P002", nombre "Pizza", categoría "Platos", precio 18.0

3. **Verificar archivo**
   - Abra `datos/productos.json`
   - Confirme que contiene los 2 productos

4. **Cerrar y reiniciar**
   - Salir con opción 9
   - Ejecutar nuevamente `python main.py`

5. **Verificar carga**
   - Opción 5 para listar productos
   - Confirme que los 2 productos anteriores están disponibles

6. **Actualizar y verificar**
   - Opción 3 para actualizar "P001"
   - Cambiar precio a 16.5
   - Salir
   - Reiniciar y listar
   - Confirme que el precio se mantuvo en 16.5

7. **Eliminar y verificar**
   - Opción 4 para eliminar "P002"
   - Salir
   - Reiniciar y listar
   - Confirme que solo "P001" existe

## Manejo de Errores

### Archivo Corrupto
Si `datos/productos.json` contiene JSON inválido:
- Se muestra una advertencia
- La aplicación inicia con colección vacía
- Puede continuar registrando nuevos productos

### Registro Incompleto
Si un registro en el JSON no contiene todas las claves esperadas:
- Se ignora ese registro específico
- Los otros registros válidos se cargan normalmente
- Se muestra una advertencia en la consola

### Permiso Denegado
Si no hay permisos para leer o escribir:
- Se muestra un mensaje de error descriptivo
- En lectura: inicia con colección vacía
- En escritura: informa que los cambios no se guardaron

## Características Conservadas

✓ Menú interactivo completo
✓ Registro de productos con validaciones
✓ Búsqueda por código
✓ Actualización de productos
✓ Eliminación de productos
✓ Listado de productos
✓ Gestión de usuarios (en memoria)
✓ Listado de categorías
✓ Anotaciones de tipos en todo el código

## Restricciones Cumplidas

✓ No reemplaza Producto por diccionarios
✓ Utiliza módulos estándar (json, os, dataclasses, typing)
✓ Evita `except: pass` genéricos
✓ Mantiene nombres descriptivos
✓ Incluye archivos `__init__.py` en paquetes
✓ Valida registros sin detener la aplicación
✓ No desarrolla interfaces gráficas
✓ No utiliza bases de datos

## Próximos Pasos

En futuras semanas, se podría considerar:
- Persistencia de usuarios
- Persistencia de pedidos
- Búsqueda avanzada con múltiples criterios
- Reportes y estadísticas
- Sistema de autenticación

## Autor

Desarrollado para el curso de POO en Python - Semana 10

---

**Última actualización**: Agosto 2026
