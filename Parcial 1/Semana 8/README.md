# Semana 8: Sistema Restaurante App - Herencia y Polimorfismo

## 📋 Descripción de la Actividad

Desarrollo de una versión mejorada del sistema **restaurante_app** que demuestra la aplicación de **herencia, polimorfismo y los principios SOLID** en Python. El sistema permite registrar productos, bebidas y clientes mediante un menú interactivo ejecutado desde consola.

Esta actividad tiene como objetivo que el estudiante:
- Comprenda cómo aplicar herencia para extender funcionalidad sin modificar código base
- Entienda el polimorfismo y cómo objetos diferentes pueden responder al mismo mensaje
- Aplique el principio de sustitución de Liskov (un objeto Bebida funciona como Producto)
- Demuestre responsabilidad única en cada clase
- Utilice una sola colección para almacenar objetos de diferentes tipos

## 🎯 Conceptos SOLID Implementados

### S — Responsabilidad Única
- **Producto**: Define atributos y comportamiento común
- **Bebida**: Extiende Producto con características específicas
- **Cliente**: Solo representa información de clientes
- **Restaurante**: Administra colecciones y validaciones
- **main.py**: Solo coordina interacción con usuario

### O — Abierto/Cerrado
- La clase `Bebida` extiende `Producto` sin modificar su código
- Se puede agregar nuevas subclases (ej: Postre) sin alterar el servicio

### L — Sustitución de Liskov
- Un objeto `Bebida` se puede usar como `Producto` sin problemas
- `mostrar_informacion()` funciona para ambos tipos
- La lista de productos admite tanto `Producto` como `Bebida`

## 📁 Estructura del Proyecto

```
restaurante_app/
├── modelos/
│   ├── __init__.py               # Inicializador del paquete modelos
│   ├── producto.py               # Clase base Producto
│   ├── bebida.py                 # Clase Bebida (hereda de Producto)
│   └── cliente.py                # Clase Cliente
├── servicios/
│   ├── __init__.py               # Inicializador del paquete servicios
│   └── restaurante.py            # Clase Restaurante (servicio)
├── main.py                       # Punto de entrada: menú interactivo
└── README.md                     # Esta documentación
```

## 📊 Clases y Relaciones

### Clase Producto (Base)

**Responsabilidad**: Representar un producto general del restaurante.

**Atributos**:
- `codigo: str` - Identificador único
- `nombre: str` - Nombre del producto
- `categoria: str` - Categoría
- `precio: float` - Precio en moneda

**Métodos**:
- `__init__(codigo, nombre, categoria, precio)` - Constructor con validaciones
- `mostrar_informacion()` - Retorna información formateada
- `__repr__()` - Representación en string

**Validaciones**:
- Código no vacío
- Nombre no vacío
- Categoría no vacía
- Precio > 0

### Clase Bebida (Subclase)

**Responsabilidad**: Representar una bebida con atributos específicos.

**Hereda de**: `Producto`

**Atributos Adicionales**:
- `tamaño_ml: int` - Tamaño en mililitros
- `tipo_envase: str` - Tipo de envase (Lata, Botella, etc.)

**Métodos**:
- `__init__(...)` - Constructor que llama a `super().__init__(...)`
- `mostrar_informacion()` - Sobrescribe el método padre
- `__repr__()` - Representación específica

**Validaciones**:
- Hereda validaciones de Producto
- Tamaño > 0
- Tipo de envase no vacío

### Clase Cliente

**Responsabilidad**: Encapsular información de un cliente.

**Atributos**:
- `identificacion: str` - Cédula, pasaporte, etc.
- `nombre: str` - Nombre completo
- `correo: str` - Correo electrónico

**Métodos**:
- `__init__(identificacion, nombre, correo)` - Constructor
- `mostrar_informacion()` - Información formateada
- `__repr__()` - Representación en string

### Clase Restaurante (Servicio)

**Responsabilidad**: Administrar colecciones y garantizar integridad de datos.

**Atributos**:
- `nombre: str` - Nombre del restaurante
- `productos: List[Producto]` - Lista única para Producto y Bebida
- `clientes: List[Cliente]` - Lista de clientes

**Métodos de Productos**:
- `registrar_producto(producto)` - Agrega Producto o Bebida
- `listar_productos()` - Muestra todos con polimorfismo
- `buscar_producto_por_codigo(codigo)` - Busca por código
- `_codigo_existe(codigo)` - Valida unicidad

**Métodos de Clientes**:
- `registrar_cliente(cliente)` - Agrega cliente
- `listar_clientes()` - Muestra todos
- `buscar_cliente_por_identificacion(id)` - Busca por identificación
- `_identificacion_existe(id)` - Valida unicidad

**Métodos de Utilidad**:
- `obtener_estadisticas()` - Retorna diccionario con conteos

## 🖥️ Menú Interactivo

```
========================================
        SISTEMA DE RESTAURANTE
========================================
1. Registrar producto
2. Registrar bebida
3. Registrar cliente
----------------------------------------
4. Listar productos
5. Listar clientes
----------------------------------------
6. Salir
```

## 🔄 Flujo de Ejecución

```
Usuario selecciona opción
        ↓
main.py solicita datos
        ↓
Se crea objeto (Producto, Bebida o Cliente)
        ↓
Restaurante valida unicidad de identificador
        ↓
Objeto se almacena en colección
        ↓
Resultado se muestra al usuario
```

### Durante Listado (Polimorfismo):

```
Iteración en lista de productos
        ↓
Para cada elemento, llamar mostrar_informacion()
        ↓
[PRODUCTO] ... (si es Producto)
[BEBIDA] ...   (si es Bebida con sus atributos)
        ↓
Usuario ve información correcta según tipo
```

## 🚀 Cómo Ejecutar

```bash
# Navegar a la carpeta
cd "Parcial 1\Semana 8"

# Ejecutar el programa
python main.py
```

## 📝 Ejemplo de Uso Completo

**Paso 1: Registrar Producto**
```
Opción: 1
Código del producto: P001
Nombre del producto: Pasta Alfredo
Categoría del producto: Plato Fuerte
Precio del producto: $14.99
✓ Producto 'Pasta Alfredo' registrado exitosamente.
```

**Paso 2: Registrar Bebida**
```
Opción: 2
Código de la bebida: B001
Nombre de la bebida: Coca Cola
Categoría de la bebida: Bebida Fría
Precio de la bebida: $2.50
Tamaño en mililitros (ml): 355
Tipo de envase (Lata, Botella, Vaso, etc.): Lata
✓ Bebida 'Coca Cola' registrado exitosamente.
```

**Paso 3: Registrar Cliente**
```
Opción: 3
Identificación del cliente: 1234567890
Nombre del cliente: Carlos López
Correo del cliente: carlos@email.com
✓ Cliente 'Carlos López' registrado exitosamente.
```

**Paso 4: Listar Productos (Demuestra Polimorfismo)**
```
Opción: 4
================================================================================
  PRODUCTOS REGISTRADOS EN LA BUENA MESA
================================================================================
1. [PRODUCTO] Código: P001 | Nombre: Pasta Alfredo | Categoría: Plato Fuerte | Precio: $14.99
2. [BEBIDA] Código: B001 | Nombre: Coca Cola | Categoría: Bebida Fría | Precio: $2.50 | Tamaño: 355ml | Envase: Lata
================================================================================
```

**Paso 5: Listar Clientes**
```
Opción: 5
================================================================================
  CLIENTES REGISTRADOS EN LA BUENA MESA
================================================================================
1. [CLIENTE] Identificación: 1234567890 | Nombre: Carlos López | Correo: carlos@email.com
================================================================================
```

## ✅ Requisitos Cumplidos

### Estructura y Archivos
- ✅ Estructura modular respetada (modelos/, servicios/, main.py)
- ✅ Archivos `__init__.py` en ambas carpetas
- ✅ Archivos: producto.py, bebida.py, cliente.py, restaurante.py

### Clase Producto
- ✅ Constructor con validaciones
- ✅ Atributos: código, nombre, categoría, precio
- ✅ Método `mostrar_informacion()` implementado
- ✅ Métodos `__repr__()` para representación

### Clase Bebida
- ✅ Herencia de Producto implementada
- ✅ Atributos adicionales: tamaño_ml, tipo_envase
- ✅ Sobrescritura del método `mostrar_informacion()`
- ✅ Constructor con `super().__init__()`
- ✅ Validaciones propias

### Clase Cliente
- ✅ Atributos: identificación, nombre, correo
- ✅ Método `mostrar_informacion()` implementado
- ✅ Constructor con validaciones

### Clase Restaurante
- ✅ Una sola lista para Producto y Bebida
- ✅ Métodos: registrar_producto, listar_productos, buscar_producto_por_codigo
- ✅ Métodos: registrar_cliente, listar_clientes, buscar_cliente_por_identificacion
- ✅ Validación de códigos únicos de productos
- ✅ Validación de identificaciones únicas de clientes
- ✅ Polimorfismo en listado usando mostrar_informacion()

### Menú Interactivo
- ✅ 6 opciones de menú
- ✅ Opción 1: Registrar producto
- ✅ Opción 2: Registrar bebida
- ✅ Opción 3: Registrar cliente
- ✅ Opción 4: Listar productos
- ✅ Opción 5: Listar clientes
- ✅ Opción 6: Salir
- ✅ Ciclo infinito hasta seleccionar salir

### Programación
- ✅ Anotaciones de tipos en constructores y métodos
- ✅ Objetos creados dinámicamente desde `input()`
- ✅ Sin objetos quemados en código
- ✅ Importaciones correctas entre módulos
- ✅ Nombres descriptivos (snake_case)
- ✅ Comentarios explicativos
- ✅ README.md completo

## 🚫 Restricciones Respetadas

- ✅ No se copió el código docente de Biblioteca
- ✅ Sin interfaces gráficas ni frameworks
- ✅ Sin bases de datos ni archivos externos
- ✅ No todo el código en un archivo
- ✅ Archivos `__init__.py` incluidos
- ✅ Una sola lista para Producto y Bebida
- ✅ Sin condiciones repetidas para tipos (uso de polimorfismo)
- ✅ Lógica de registro en Restaurante, no en main.py
- ✅ Herencia válida (Bebida es un Producto)
- ✅ Nombres descriptivos
- ✅ Código completo entregado

## 🔍 Demostración de Conceptos

### 1. Herencia
```python
class Bebida(Producto):
    def __init__(self, codigo, nombre, categoria, precio, tamaño_ml, tipo_envase):
        super().__init__(codigo, nombre, categoria, precio)
        self.tamaño_ml = tamaño_ml
        self.tipo_envase = tipo_envase
```

### 2. Polimorfismo
```python
def listar_productos(self):
    for producto in self.productos:
        # Cada objeto ejecuta su propia versión
        print(producto.mostrar_informacion())
```

### 3. Sustitución de Liskov
```python
# Ambas funcionan igual en la lista
productos: List[Producto] = []
productos.append(Producto(...))  # Funciona
productos.append(Bebida(...))     # También funciona
```

### 4. Responsabilidad Única
- Producto: define estructura base
- Bebida: extiende con datos específicos
- Cliente: solo cliente
- Restaurante: administra colecciones
- main.py: interfaz usuario

## 📚 Patrones Aplicados

- **Herencia**: Bebida extiende Producto
- **Polimorfismo**: Sobrescritura de `mostrar_informacion()`
- **Encapsulación**: Atributos privados, métodos públicos
- **Arquitectura por Capas**: Modelos, Servicios, Presentación
- **Principios SOLID**: Especialmente SRP, OCP y LSP

## ✨ Conclusión

El sistema **restaurante_app** de Semana 8 demuestra:
- Aplicación correcta de **herencia y polimorfismo**
- Adherencia a **principios SOLID**
- **Arquitectura modular y escalable**
- **Mantenibilidad del código**
- **Buenas prácticas de Python**

El proyecto cumple todos los requisitos y está listo para evaluación.
