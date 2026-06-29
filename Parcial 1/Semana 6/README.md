# Sistema Restaurante App - Programación Orientada a Objetos

## Descripción
Sistema mejorado de gestión de productos de restaurante implementado con Programación Orientada a Objetos (POO) en Python. Demuestra conceptos fundamentales como **herencia**, **encapsulación** y **polimorfismo**.

## Estructura del Proyecto

```
restaurante_app/
├── modelos/
│   ├── __init__.py           # Inicializador del paquete modelos
│   ├── producto.py           # Clase padre Producto
│   ├── platillo.py           # Clase hija Platillo
│   └── bebida.py             # Clase hija Bebida
├── servicios/
│   ├── __init__.py           # Inicializador del paquete servicios
│   └── restaurante.py        # Clase Restaurante (servicio)
└── main.py                   # Punto de entrada del programa
```

## Principios de POO Aplicados

### 1. **Herencia**
- Clase padre `Producto` define atributos y métodos comunes
- Clases hijas `Platillo` y `Bebida` heredan de `Producto`
- Uso de `super()` para reutilizar el constructor de la clase padre

### 2. **Encapsulación**
- Atributo `__precio` privado en la clase `Producto`
- Métodos `obtener_precio()` y `cambiar_precio()` para acceso controlado
- Validación: el precio debe ser mayor a cero

### 3. **Polimorfismo**
- Método `mostrar_informacion()` sobrescrito en `Platillo` y `Bebida`
- Recorrido de lista de productos ejecutando el método según su tipo específico
- Cada clase muestra información diferente según su tipo

## Responsabilidades de cada clase

### Clase Producto (Padre)
- **Atributos**: nombre, precio (privado), disponibilidad
- **Métodos**: getters/setters, validación de precio, mostrar_informacion()

### Clase Platillo (Hija)
- **Atributos adicionales**: tipo_platillo, calorías, tiempo_preparación
- **Métodos**: getters específicos, mostrar_informacion() sobrescrito

### Clase Bebida (Hija)
- **Atributos adicionales**: tipo_bebida, volumen_ml, es_fria
- **Métodos**: getters específicos, mostrar_informacion() sobrescrito

### Clase Restaurante (Servicio)
- **Responsabilidad**: administrar lista de productos
- **Métodos**: agregar_producto(), eliminar_producto(), mostrar_menu(), mostrar_platillos(), mostrar_bebidas()

## Características del Programa

✓ **Herencia**: Producto ← Platillo, Bebida  
✓ **Encapsulación**: Precio privado con validación  
✓ **Polimorfismo**: Diferentes representaciones según tipo de objeto  
✓ **Constructor con super()**: Reutilización de atributos padre  
✓ **Validación de datos**: Precio > 0  
✓ **Estructura modular**: Separación en paquetes modelos y servicios  
✓ **Nomenclatura descriptiva**: Nombres claros y convencionesde Python (snake_case)  
✓ **Documentación**: Docstrings y comentarios explícitosRealización: Al ejecutar `main.py`:
1. Se crean 3 platillos (Entrada, Plato Fuerte, Postre)
2. Se crean 3 bebidas (Gaseosa, Café, Jugo)
3. Se agregan todos al restaurante
4. Se muestra el menú completo (polimorfismo en acción)
5. Se demuestra encapsulación y validación de precios
6. Se muestran platillos y bebidas por separado

## Cómo ejecutar

```bash
cd "Parcial 1\Semana 6"
python main.py
```

## Requisitos cumplidos

- ✓ Proyecto con estructura modular solicitada
- ✓ Clase padre Producto implementada
- ✓ Clases hijas Platillo y Bebida implementadas
- ✓ Herencia lógica entre clases
- ✓ Constructor __init__() en clases principales
- ✓ super() utilizado en clases hijas
- ✓ Encapsulación de atributo __precio
- ✓ Métodos de acceso/modificación con validación
- ✓ Validación de precio (> 0)
- ✓ Polimorfismo en mostrar_informacion()
- ✓ Clase Restaurante administra productos
- ✓ 3 Platillos y 3 Bebidas creados
- ✓ Información mostrada organizadamente en consola
- ✓ Nomenclatura descriptiva y Python conventions
- ✓ Comentarios explicativos en código

## Restricciones respetadas

✓ No se copió literalmente el ejemplo de biblioteca  
✓ Código comprensible y documentado  
✓ Sin interfaces gráficas ni frameworks  
✓ Sin bases de datos ni archivos externos  
✓ Nombres descriptivos (sin x, dato, objeto, clase1)  
✓ Herencia implementada (no clases independientes)
