# Semana 7: Sistema Restaurante App - Programación Orientada a Objetos

## 📋 Descripción de la Actividad

Desarrollo de una versión mejorada del sistema **restaurante_app** utilizando **Programación Orientada a Objetos (POO)** en Python. El sistema permite registrar, listar y buscar productos y clientes de un restaurante mediante un menú interactivo ejecutado desde consola.

Esta actividad tiene como objetivo que el estudiante:
- Comprenda cómo un dato ingresado por consola se transforma en un objeto mediante el constructor
- Entienda cómo ese objeto se almacena en una clase de servicio
- Aprenda cómo se puede listar o buscar dentro del sistema
- Aplique conceptos fundamentales de POO como encapsulación, validación y arquitectura por capas

## 📁 Estructura del Proyecto

```
restaurante_app/
├── modelos/
│   ├── __init__.py               # Inicializador del paquete modelos
│   ├── producto.py               # Clase Producto con constructor, @property y @setter
│   └── cliente.py                # Clase Cliente con @dataclass
├── servicios/
│   ├── __init__.py               # Inicializador del paquete servicios
│   └── restaurante.py            # Clase Restaurante (administrador de datos)
├── main.py                       # Punto de entrada: menú interactivo
└── README.md                     # Esta documentación
```

## 🎯 Conceptos de POO Implementados

### 1. **Encapsulación**
- Atributos privados en `Producto` (`_nombre`, `_categoria`, `_precio`, `_disponible`)
- Acceso controlado mediante decoradores `@property` (lectura)
- Modificación controlada mediante decoradores `@setter` (escritura con validación)
- Protección contra valores inválidos

### 2. **Constructores y Creación de Objetos**
- Constructor `__init__()` tradicional en clase `Producto`
- Validaciones en el constructor (nombre, categoría, precio)
- Decorador `@dataclass` en clase `Cliente` para automatizar constructor
- Transformación de datos de consola → objetos Python

### 3. **Validación de Datos**
- Validación en constructor de Producto
- Validación en setters de Producto
- Captura de excepciones `ValueError` para manejo de errores
- Mensajes descriptivos para el usuario

### 4. **Arquitectura por Capas**
- **Capa de Modelos**: `Producto` y `Cliente` (entidades del dominio)
- **Capa de Servicios**: `Restaurante` (lógica de negocio)
- **Capa de Presentación**: `main.py` (interfaz de usuario)

## 📊 Responsabilidades de Cada Clase

### Clase Producto (`modelos/producto.py`)

**Constructor:**
```python
def __init__(self, nombre, categoria, precio, disponible=True)
```

**Atributos Privados:**
- `_nombre`: str (no puede estar vacío)
- `_categoria`: str (no puede estar vacía)
- `_precio`: float (debe ser mayor a cero)
- `_disponible`: bool (estado de disponibilidad)

**Decoradores @property:**
- `nombre` - Acceso de lectura controlada
- `categoria` - Acceso de lectura controlada
- `precio` - Acceso de lectura controlada
- `disponible` - Acceso de lectura controlada

**Decoradores @setter:**
- `nombre.setter` - Con validación: no vacío
- `categoria.setter` - Con validación: no vacía
- `precio.setter` - Con validación: > 0
- `disponible.setter` - Sin validación especial

**Métodos:**
- `mostrar_informacion()` - Retorna string con formato legible

### Clase Cliente (`modelos/cliente.py`)

**Implementación:** `@dataclass`

**Atributos:**
- `id_cliente`: int (identificador único)
- `nombre`: str (nombre del cliente)
- `correo`: str (correo electrónico)

**Métodos:**
- `__str__()` - Representación legible del cliente

### Clase Restaurante (`servicios/restaurante.py`)

**Responsabilidad Principal:** Administrar listas de productos y clientes

**Métodos de Productos:**
- `registrar_producto(producto)` - Agrega nuevo producto a la lista
- `listar_productos()` - Muestra todos los productos registrados
- `buscar_producto(nombre)` - Busca producto por nombre exacto

**Métodos de Clientes:**
- `registrar_cliente(nombre, correo)` - Crea y agrega nuevo cliente
- `listar_clientes()` - Muestra todos los clientes registrados
- `buscar_cliente(nombre)` - Busca cliente por nombre exacto

**Atributos Internos:**
- `nombre_restaurante`: str
- `productos`: list (almacena objetos Producto)
- `clientes`: list (almacena objetos Cliente)
- `proximo_id_cliente`: int (contador de IDs)

## 🖥️ Menú Interactivo (`main.py`)

```
========================================
        SISTEMA DE RESTAURANTE
========================================
1. Registrar producto
2. Listar productos
3. Buscar producto
----------------------------------------
4. Registrar cliente
5. Listar clientes
6. Buscar cliente
----------------------------------------
7. Salir
```

**Características:**
- Menú que se repite hasta seleccionar opción 7
- Solicita datos al usuario mediante `input()`
- Crea objetos usando constructores
- Llama a métodos de `Restaurante` para almacenar datos
- Manejo de errores y validaciones

## 🔄 Flujo de Ejecución del Sistema

```
┌──────────────────┐
│ input() usuario  │
└────────┬─────────┘
         │
         ▼
┌──────────────────────────┐
│ Captura de datos:        │
│ nombre, categoría, etc.  │
└────────┬─────────────────┘
         │
         ▼
┌──────────────────────────┐
│ Validación de datos:     │
│ No vacío, precio > 0     │
└────────┬─────────────────┘
         │
         ▼
┌──────────────────────────┐
│ Constructor del Modelo:  │
│ Producto(...) o          │
│ Cliente(...)             │
└────────┬─────────────────┘
         │
         ▼
┌──────────────────────────┐
│ Creación del Objeto      │
└────────┬─────────────────┘
         │
         ▼
┌──────────────────────────┐
│ Registro en Restaurante: │
│ lista.append(objeto)     │
└────────┬─────────────────┘
         │
         ▼
┌──────────────────────────┐
│ Listado o Búsqueda:      │
│ Presentar resultados     │
└──────────────────────────┘
```

## 🚀 Cómo Ejecutar

```bash
# Navegar a la carpeta
cd "Parcial 1\Semana 7"

# Ejecutar el programa
python main.py
```

## 📝 Ejemplo de Uso Completo

**Paso 1: Registrar Producto**
```
Opción: 1
Nombre del producto: Sopa de Cebolla
Categoría del producto: Entrada
Precio del producto: $8.50
✓ Producto 'Sopa de Cebolla' registrado exitosamente.
```

**Paso 2: Registrar Cliente**
```
Opción: 4
Nombre del cliente: María García
Correo del cliente: maria@email.com
✓ Cliente 'María García' registrado exitosamente. ID: 1
```

**Paso 3: Listar Productos**
```
Opción: 2
======================================================================
  PRODUCTOS REGISTRADOS
======================================================================
1. Nombre: Sopa de Cebolla | Categoría: Entrada | Precio: $8.50 | ✓ Disponible
```

**Paso 4: Listar Clientes**
```
Opción: 5
======================================================================
  CLIENTES REGISTRADOS
======================================================================
1. ID: 1 | Nombre: María García | Correo: maria@email.com
```

## ✅ Requisitos Cumplidos

### Estructura y Archivos
- ✅ Proyecto con estructura modular solicitada
- ✅ Carpetas: `modelos/`, `servicios/`
- ✅ Archivos `__init__.py` en ambas carpetas
- ✅ Archivos: `producto.py`, `cliente.py`, `restaurante.py`, `main.py`

### Clase Producto
- ✅ Constructor tradicional `__init__()` implementado
- ✅ Atributos: nombre, categoría, precio, disponible
- ✅ Decoradores `@property` para acceso controlado
- ✅ Decoradores `@setter` con validaciones básicas
- ✅ Validación: nombre no puede estar vacío
- ✅ Validación: categoría no puede estar vacía
- ✅ Validación: precio debe ser mayor a cero
- ✅ Método `mostrar_informacion()` implementado

### Clase Cliente
- ✅ Decorador `@dataclass` utilizado
- ✅ Atributos: id_cliente, nombre, correo
- ✅ Constructor automático generado por @dataclass
- ✅ Representación legible mediante `__str__()`

### Clase Restaurante
- ✅ Administra lista de productos
- ✅ Administra lista de clientes
- ✅ Método `registrar_producto(producto)`
- ✅ Método `listar_productos()`
- ✅ Método `buscar_producto(nombre)`
- ✅ Método `registrar_cliente(nombre, correo)`
- ✅ Método `listar_clientes()`
- ✅ Método `buscar_cliente(nombre)`

### Menú Interactivo
- ✅ Menú con 7 opciones implementado
- ✅ Opción 1: Registrar producto
- ✅ Opción 2: Listar productos
- ✅ Opción 3: Buscar producto
- ✅ Opción 4: Registrar cliente
- ✅ Opción 5: Listar clientes
- ✅ Opción 6: Buscar cliente
- ✅ Opción 7: Salir
- ✅ Ciclo infinito hasta seleccionar salir

### Programación
- ✅ Objetos creados dinámicamente desde `input()` del usuario
- ✅ Sin objetos quemados directamente en el código
- ✅ Importaciones correctas entre módulos
- ✅ Sistema ejecutable desde `main.py`
- ✅ Nombres descriptivos y convenciones Python (snake_case)
- ✅ Comentarios explicativos en el código

## 🚫 Restricciones Respetadas

- ✅ No se copió literalmente el ejemplo docente de biblioteca
- ✅ Código comprensible y documentado
- ✅ Sin interfaces gráficas ni frameworks (solo consola)
- ✅ Sin bases de datos ni archivos externos
- ✅ Nombres descriptivos (no x, dato, objeto, clase1, metodo1)
- ✅ Objetos dinámicos creados desde `input()`, no quemados en código
- ✅ Estructura modular en carpetas (no todo en un archivo)
- ✅ Archivos `__init__.py` incluidos
- ✅ `@property`, `@setter` y `@dataclass` utilizados según requisitos

## 🔍 Conceptos Clave Demostrables

Este proyecto evidencia que el estudiante comprende:

1. **Transformación datos → objetos**
   - Entrada de consola → constructor → objeto Python

2. **Almacenamiento en servicios**
   - Objetos creados se guardan en listas de `Restaurante`

3. **Consulta de información**
   - Métodos de listado y búsqueda acceden a los datos almacenados

4. **Encapsulación**
   - Acceso controlado mediante `@property` y `@setter`
   - Validaciones evitan datos inválidos

5. **Arquitectura modular**
   - Separación clara de responsabilidades
   - Mantenibilidad y escalabilidad del código

## 📚 Referencias de Implementación

### Uso de @dataclass
```python
from dataclasses import dataclass

@dataclass
class Cliente:
    id_cliente: int
    nombre: str
    correo: str
```

### Uso de @property y @setter
```python
class Producto:
    def __init__(self, nombre, categoria, precio):
        self._nombre = nombre
    
    @property
    def nombre(self):
        return self._nombre
    
    @nombre.setter
    def nombre(self, valor):
        if not valor.strip():
            raise ValueError("No puede estar vacío")
        self._nombre = valor
```

## ✨ Conclusión

El sistema **restaurante_app** implementado en Semana 7 demuestra la aplicación correcta de:
- Programación Orientada a Objetos
- Arquitectura por capas
- Validación de datos
- Interfaces de usuario interactivas
- Buenas prácticas de Python

El proyecto cumple con todos los requisitos solicitados y está listo para ser evaluado.
