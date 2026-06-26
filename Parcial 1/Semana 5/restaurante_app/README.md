# Sistema de Gestión de Restaurante

## 📋 Descripción del Proyecto

Este proyecto implementa un **sistema básico de gestión de restaurante** utilizando **Programación Orientada a Objetos (POO)** en Python. El objetivo es demostrar la aplicación correcta de identificadores, convenciones de nombres, tipos de datos básicos y la estructura modular de proyectos Python.

El sistema permite administrar:
- **Productos**: Platos y bebidas disponibles en el restaurante
- **Clientes**: Personas registradas en el sistema
- **Restaurante**: Gestión centralizada de productos y clientes

## 🏗️ Estructura del Proyecto

```
restaurante_app/
├── modelos/
│   ├── __init__.py           # Módulo de modelos
│   ├── producto.py           # Clase Producto
│   └── cliente.py            # Clase Cliente
├── servicios/
│   ├── __init__.py           # Módulo de servicios
│   └── restaurante.py        # Clase Restaurante
├── main.py                   # Punto de entrada del programa
└── README.md                 # Este archivo
```

## 📚 Clases Principales

### 1. **Clase Producto** (`modelos/producto.py`)

Representa un producto (plato o bebida) disponible en el restaurante.

**Atributos:**
- `codigo: int` - Identificador único del producto
- `nombre: str` - Nombre del producto
- `descripcion: str` - Descripción breve del producto
- `precio: float` - Precio del producto
- `disponible: bool` - Estado de disponibilidad

**Métodos:**
- `__init__()` - Constructor
- `__str__()` - Representación en texto
- `cambiar_disponibilidad()` - Actualiza la disponibilidad
- `obtener_informacion_completa()` - Retorna detalles del producto

**Ejemplo:**
```python
hamburguesa = Producto(
    codigo=101,
    nombre="Hamburguesa Clásica",
    descripcion="Hamburguesa hecha con carne de res premium",
    precio=15.99,
    disponible=True
)
print(hamburguesa)  # Usa __str__()
```

### 2. **Clase Cliente** (`modelos/cliente.py`)

Representa un cliente registrado en el sistema del restaurante.

**Atributos:**
- `cedula: int` - Número de identificación del cliente
- `nombre: str` - Nombre completo
- `correo_electronico: str` - Email de contacto
- `telefono: str` - Número de teléfono
- `es_miembro_frecuente: bool` - Indica si es cliente frecuente

**Métodos:**
- `__init__()` - Constructor
- `__str__()` - Representación en texto
- `obtener_informacion_contacto()` - Retorna email y teléfono
- `convertir_a_miembro_frecuente()` - Cambia estado a miembro frecuente

**Ejemplo:**
```python
cliente = Cliente(
    cedula=1234567,
    nombre="Juan Pérez García",
    correo_electronico="juan.perez@email.com",
    telefono="+57 3001234567",
    es_miembro_frecuente=True
)
print(cliente)  # Usa __str__()
```

### 3. **Clase Restaurante** (`servicios/restaurante.py`)

Administra el restaurante, gestiona listas de productos y clientes.

**Atributos:**
- `nombre_restaurante: str` - Nombre del establecimiento
- `direccion: str` - Ubicación del restaurante
- `lista_productos: list[Producto]` - Lista de productos disponibles
- `lista_clientes: list[Cliente]` - Lista de clientes registrados

**Métodos:**
- `__init__()` - Constructor
- `agregar_producto()` - Agrega producto a la lista
- `agregar_cliente()` - Agrega cliente a la lista
- `listar_productos()` - Muestra todos los productos
- `listar_clientes()` - Muestra todos los clientes
- `obtener_resumen_restaurante()` - Retorna resumen general
- `mostrar_informacion_completa()` - Muestra información detallada

**Ejemplo:**
```python
restaurante = Restaurante(
    nombre_restaurante="El Buen Sabor",
    direccion="Calle Principal 123"
)
restaurante.agregar_producto(hamburguesa)
restaurante.agregar_cliente(cliente)
restaurante.mostrar_informacion_completa()
```

## 🚀 Cómo Ejecutar el Programa

### Requisitos Previos
- Python 3.8 o superior instalado

### Pasos para Ejecutar

1. **Navegar a la carpeta del proyecto:**
```bash
cd restaurante_app
```

2. **Ejecutar el programa:**
```bash
python main.py
```

3. **Resultado Esperado:**
El programa mostrará:
- Resumen del restaurante
- Lista de productos con precios y disponibilidad
- Lista de clientes con estado (frecuente o regular)
- Detalles completos de productos y clientes
- Cambios realizados en el sistema
- Información actualizada

## 📝 Características Implementadas

✅ **Convenciones de Nombres:**
- PascalCase para nombres de clases: `Producto`, `Cliente`, `Restaurante`
- snake_case para atributos y métodos: `nombre_restaurante`, `agregar_producto`, `es_miembro_frecuente`
- snake_case para nombres de archivos: `producto.py`, `cliente.py`, `restaurante.py`

✅ **Tipos de Datos:**
- Tipos básicos: `str`, `int`, `float`, `bool`
- Tipo compuesto: `list` (listas de productos y clientes)
- Anotaciones de tipo en parámetros y atributos

✅ **Programación Orientada a Objetos:**
- Clases bien definidas con responsabilidades específicas
- Constructor `__init__()` en todas las clases
- Método especial `__str__()` para representación legible
- Métodos que encapsulan la lógica de cada entidad

✅ **Modularidad:**
- Separación en carpetas: `modelos` y `servicios`
- Archivos `__init__.py` para crear paquetes Python
- Importaciones correctas entre módulos

✅ **Buenas Prácticas:**
- Comentarios explicativos en secciones clave
- Docstrings en clases y métodos
- Código organizado y legible
- Sin nombres genéricos (no usa `x`, `dato`, `objeto`, etc.)

## 📊 Ejemplo de Salida

```
Sistema de Gestión de Restaurante
----------------------------------------
==================================================
Restaurante: El Buen Sabor | Dirección: Calle Principal 123, Centro | Productos: 3 | Clientes: 3
===================================================

=== LISTA DE PRODUCTOS ===
  Producto(ID: 101, Nombre: Hamburguesa Clásica, Precio: $15.99, Estado: Disponible)
  Producto(ID: 102, Nombre: Ensalada César, Precio: $12.50, Estado: Disponible)
  Producto(ID: 103, Nombre: Limonada Casera, Precio: $3.99, Estado: No disponible)

=== LISTA DE CLIENTES ===
  Cliente(Cédula: 1234567, Nombre: Juan Pérez García, Estado: Miembro frecuente)
  Cliente(Cédula: 9876543, Nombre: María Rodríguez López, Estado: Cliente regular)
  Cliente(Cédula: 5555555, Nombre: Carlos Martínez Silva, Estado: Miembro frecuente)

=== DETALLES DE PRODUCTOS ===
  • Hamburguesa Clásica: Hamburguesa hecha con carne de res premium y salsas caseras - Precio: $15.99
  • Ensalada César: Ensalada fresca con lechuga romana, crutones y aderezo César - Precio: $12.50
  • Limonada Casera: Bebida refrescante preparada con limones naturales - Precio: $3.99

=== DETALLES DE CLIENTES ===
  • Juan Pérez García
    Email: juan.perez@email.com, Teléfono: +57 3001234567
  • María Rodríguez López
    Email: maria.rodriguez@email.com, Teléfono: +57 3009876543
  • Carlos Martínez Silva
    Email: carlos.martinez@email.com, Teléfono: +57 3005555555

=== CAMBIOS EN EL SISTEMA ===
✓ María Rodríguez López ahora es miembro frecuente.
✓ Limonada Casera ahora está disponible.
```

## 🎓 Conceptos de Programación Aplicados

1. **Clases y Objetos**: Definición de clases que modelan entidades del dominio
2. **Encapsulación**: Atributos privados y métodos públicos
3. **Constructores**: Inicialización de objetos con estado inicial
4. **Método `__str__()`**: Representación legible de objetos
5. **Listas**: Almacenamiento de múltiples objetos de un tipo
6. **Importaciones**: Modularidad mediante importación entre módulos
7. **Tipo de Datos**: Uso correcto de tipos básicos y compuestos
8. **Convenciones**: Seguimiento de estándares de nombres PEP 8

## 📖 Reflexión sobre el Diseño

Este sistema demuestra principios fundamentales de POO:

- **Responsabilidad Única**: Cada clase tiene un propósito claro
  - `Producto`: Representa un artículo del menú
  - `Cliente`: Almacena información de contacto
  - `Restaurante`: Coordina la gestión de productos y clientes

- **Reutilización**: Las clases pueden instanciarse múltiples veces

- **Mantenibilidad**: El código es fácil de entender y modificar

- **Escalabilidad**: Nuevas funcionalidades pueden agregarse sin afectar código existente

## 📝 Autor

**Curso**: Programación Orientada a Objetos - Semana 5  
**Periodo Académico**: Parcial 1  
**Tema**: Identificadores, tipos de datos y proyectos modulares en Python

---

*Última actualización: Junio 2026*
