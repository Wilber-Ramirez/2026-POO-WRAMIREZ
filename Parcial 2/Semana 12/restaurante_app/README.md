# Restaurante App - Semana 11 (mejorada para Semana 12)

## Descripción
Este proyecto administra productos, usuarios y ventas con persistencia en JSON. La lógica de negocio reside en `Restaurante`, con modelos separados y un servicio de archivos. En esta entrega se incorporaron índices en memoria para optimizar búsquedas frecuentes sin reemplazar las colecciones principales.

## Estructura

```text
restaurante_app/
├── datos/
│   ├── productos.json
│   ├── usuarios.json
│   └── ventas.json
├── modelos/
│   ├── __init__.py
│   ├── producto.py
│   ├── usuario.py
│   └── venta.py
├── servicios/
│   ├── __init__.py
│   ├── archivo_servicio.py
│   └── restaurante.py
├── __init__.py
├── main.py
└── README.md
```

## Mejoras de rendimiento (Semana 12)
- Se mantienen las listas principales `_productos`, `_usuarios` y `_ventas` para almacenamiento, recorrido y persistencia.
- Se añadieron índices en memoria:
  - `_indice_productos`: dict que mapea `codigo` -> instancia de Producto (búsqueda O(1) por código).
  - `_indice_usuarios`: dict que mapea `identificacion` -> instancia de Usuario (búsqueda O(1) por identificación).
  - `_ventas_por_usuario`: dict que mapea `usuario_id` -> lista de Venta, evitando recorrer todas las ventas para consultar por usuario.
- Los índices se reconstruyen al iniciar la aplicación a partir de los objetos leídos desde JSON.
- Al registrar, modificar o eliminar objetos, los índices se mantienen sincronizados con las listas principales.
- No se reemplazaron los modelos por diccionarios: los objetos siguen siendo instancias de las clases en `modelos/`.

## Características
- Registro de productos con atributos `codigo`, `nombre`, `categoria`, `precio` y `stock`.
- Registro de usuarios con `identificacion`, `nombre` y `correo`.
- Registro de ventas como relación entre usuario y producto.
- Validación de stock y cantidades antes de vender.
- Persistencia en archivos JSON con `json.dump()` y `json.load()`.
- Recuperación automática de productos, usuarios y ventas al iniciar la aplicación.
- Consulta de ventas por usuario optimizada mediante `_ventas_por_usuario`.

## Reglas de negocio
- No se permiten productos con precio negativo.
- No se permite stock negativo.
- No se pueden vender cantidades menores o iguales a cero.
- No se puede vender más de lo que hay en stock.
- Una venta solo se registra si existen el usuario y el producto asociados.

## Comprobación mínima de funcionamiento
- Ejecutar `main.py` y comprobar que las funcionalidades siguen operativas.
- Registrar o cargar usuarios, productos y ventas existentes.
- Buscar un producto por su `codigo` (búsqueda optimizada).
- Buscar un usuario por su `identificacion` (búsqueda optimizada).
- Consultar las ventas relacionadas con un usuario (usa índice en memoria).
- Realizar una venta y confirmar que el `stock` se actualiza correctamente y que `_ventas_por_usuario` se actualiza.
- Cerrar y volver a ejecutar: los índices se reconstruyen a partir de los JSON.

## Ejecución
Desde la raíz del repositorio, ejecute:

```bash
python "Parcial 2/Semana 11/restaurante_app/main.py"
```

## Persistencia
La aplicación guarda automáticamente los cambios en:
- `datos/productos.json`
- `datos/usuarios.json`
- `datos/ventas.json`

Si alguno de los archivos no existe, el sistema inicia con colecciones vacías. Si el contenido del JSON es inválido, la aplicación informa el problema y continúa de forma segura.
