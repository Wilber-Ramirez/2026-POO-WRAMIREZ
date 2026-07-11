# Sistema Restaurante App - Programación Orientada a Objetos

## Descripción
Sistema mejorado de gestión de productos y clientes de un restaurante implementado con Programación Orientada a Objetos (POO) en Python. Permite registrar, listar y buscar productos y clientes mediante un menú interactivo ejecutado desde consola.

## Estructura del Proyecto

```
restaurante_app/
├── modelos/
│   ├── __init__.py           # Inicializador del paquete modelos
│   ├── producto.py           # Clase Producto con @property y @setter
│   └── cliente.py            # Clase Cliente con @dataclass
├── servicios/
│   ├── __init__.py           # Inicializador del paquete servicios
│   └── restaurante.py        # Clase Restaurante (servicio)
└── main.py                   # Punto de entrada del programa
```

## Conceptos de POO Aplicados

### 1. **Encapsulación**
- Atributos privados en la clase `Producto` (con `_nombre`, `_categoria`, `_precio`, `_disponible`)
- Uso de decoradores `@property` para acceso controlado de lectura
- Uso de decoradores `@setter` para acceso controlado de escritura con validaciones

### 2. **Constructores y Creación de Objetos**
- Constructor `__init__()` en la clase `Producto` que recibe parámetros validados
- Decorador `@dataclass` en la clase `Cliente` para automatizar la creación de constructores
- Transformación de datos ingresados por consola en objetos mediante constructores

### 3. **Validación de Datos**
- Validación en setters: nombre no puede estar vacío
- Validación en setters: categoría no puede estar vacía
- Validación en setters: precio debe ser mayor a cero
- Captura de excepciones `ValueError` para manejar errores

### 4. **Arquitectura por Capas**
- **Capa de Modelos**: Define las entidades `Producto` y `Cliente`
- **Capa de Servicios**: Clase `Restaurante` administra la lógica de negocio
- **Capa de Presentación**: Archivo `main.py` maneja la interfaz de usuario

## Responsabilidades de cada clase

### Clase Producto (modelos/producto.py)
- **Atributos**: nombre, categoría, precio, disponible
- **Métodos**: 
  - `@property nombre/categoria/precio/disponible` para acceso de lectura
  - `@setter nombre/categoria/precio/disponible` para acceso de escritura con validación
  - `mostrar_informacion()` para retornar información formateada

### Clase Cliente (modelos/cliente.py)
- **Atributos**: id_cliente, nombre, correo
- **Implementación**: @dataclass (automáticamente genera __init__, __repr__, etc.)
- **Métodos**: `__str__()` para representación legible

### Clase Restaurante (servicios/restaurante.py)
- **Responsabilidad**: Administrar listas de productos y clientes
- **Métodos de Productos**: 
  - `registrar_producto(producto)` - Agrega nuevo producto
  - `listar_productos()` - Muestra todos los productos
  - `buscar_producto(nombre)` - Busca producto por nombre
- **Métodos de Clientes**:
  - `registrar_cliente(nombre, correo)` - Agrega nuevo cliente
  - `listar_clientes()` - Muestra todos los clientes
  - `buscar_cliente(nombre)` - Busca cliente por nombre

## Menú Interactivo

El sistema presenta el siguiente menú:

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

## Flujo de Ejecución

1. **Input**: El usuario selecciona una opción del menú
2. **Captura de Datos**: Se solicita información al usuario mediante input()
3. **Validación**: Se validan los datos ingresados
4. **Creación de Objeto**: Se utiliza el constructor del modelo para crear el objeto
5. **Almacenamiento**: Se registra en la lista del servicio Restaurante
6. **Presentación**: Se muestra el resultado al usuario

Este flujo evidencia la relación entre entrada de datos → creación de objetos → almacenamiento → consulta.

## Cómo ejecutar

```bash
cd "Parcial 1\Semana 6"
python main.py
```

## Ejemplo de Uso

```
1. Registrar producto
   → Ingresar: Pizza Margherita | Platillos | 12.50
   → Se crea: Producto("Pizza Margherita", "Platillos", 12.50)

2. Listar productos
   → Muestra: Nombre: Pizza Margherita | Categoría: Platillos | Precio: $12.50 | ✓ Disponible

3. Registrar cliente
   → Ingresar: Juan Pérez | juan@email.com
   → Se crea: Cliente(id_cliente=1, nombre="Juan Pérez", correo="juan@email.com")

4. Buscar cliente
   → Ingresa búsqueda: Juan Pérez
   → Retorna: ID: 1 | Nombre: Juan Pérez | Correo: juan@email.com
```

## Requisitos Cumplidos

✅ Proyecto con estructura modular solicitada  
✅ Clase Producto implementada con constructor __init__()  
✅ Decoradores @property para acceso controlado  
✅ Decoradores @setter para modificación con validaciones  
✅ Validación: nombre del producto no está vacío  
✅ Validación: categoría del producto no está vacía  
✅ Validación: precio del producto es mayor a cero  
✅ Método mostrar_informacion() en Producto  
✅ Clase Cliente implementada con @dataclass  
✅ Atributos en Cliente: nombre, correo, id_cliente  
✅ Clase Restaurante administra productos y clientes  
✅ Métodos: registrar, listar y buscar productos  
✅ Métodos: registrar, listar y buscar clientes  
✅ Menú interactivo en main.py  
✅ Objetos creados desde input() del usuario  
✅ Sin objetos quemados en el código  
✅ Importaciones correctas entre módulos  
✅ Sistema ejecutable desde main.py  
✅ Nombres descriptivos y convenciones Python (snake_case)  
✅ Comentarios explicativos en código  
✅ Archivos __init__.py en carpetas modelos y servicios  

## Restricciones Respetadas

✅ No se copió código del ejemplo docente  
✅ Código comprensible y documentado  
✅ Sin interfaces gráficas ni frameworks  
✅ Sin bases de datos ni archivos externos  
✅ Nombres descriptivos (no x, dato, objeto, clase1)  
✅ Objetos dinámicos creados desde input(), no quemados  
✅ Estructura modular en carpetas (no todo en un archivo)  
✅ Archivos __init__.py incluidos  
✅ @property, @setter y @dataclass utilizados según requisitos
