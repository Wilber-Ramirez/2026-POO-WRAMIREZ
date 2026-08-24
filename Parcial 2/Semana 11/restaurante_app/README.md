# Restaurante App - Semana 11

## Descripción
Este proyecto evoluciona la aplicación de restaurante para administrar productos, usuarios y ventas con persistencia en JSON. El sistema conserva la lógica de negocio en `Restaurante`, con modelos separados para cada entidad y un servicio responsable de la lectura y escritura de archivos.

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

## Características
- Registro de productos con atributos `codigo`, `nombre`, `categoria`, `precio` y `stock`.
- Registro de usuarios con `identificacion`, `nombre` y `correo`.
- Registro de ventas como relación entre usuario y producto.
- Validación de stock y cantidades antes de vender.
- Persistencia en archivos JSON con `json.dump()` y `json.load()`.
- Recuperación automática de productos, usuarios y ventas al iniciar la aplicación.
- Consulta de ventas por usuario mediante recorrido y filtrado de la colección de ventas.

## Reglas de negocio
- No se permiten productos con precio negativo.
- No se permite stock negativo.
- No se pueden vender cantidades menores o iguales a cero.
- No se puede vender más de lo que hay en stock.
- Una venta solo se registra si existen el usuario y el producto asociados.

## Ejecución
Desde la raíz del repositorio, ejecute:

```bash
python "Parcial 2/Semana 11/restaurante_app/main.py"
```

También puede ejecutarse desde la carpeta del proyecto:

```bash
cd "Parcial 2/Semana 11/restaurante_app"
python main.py
```

## Flujo principal
1. Registrar un usuario.
2. Registrar un producto con stock disponible.
3. Realizar una venta indicando usuario, producto y cantidad.
4. Verificar que el stock disminuye.
5. Consultar ventas por usuario.
6. Cerrar y volver a ejecutar para comprobar la persistencia JSON.

## Persistencia
La aplicación guarda automáticamente los cambios en:
- `datos/productos.json`
- `datos/usuarios.json`
- `datos/ventas.json`

Si alguno de los archivos no existe, el sistema inicia con colecciones vacías. Si el contenido del JSON es inválido, la aplicación informa el problema y continúa de forma segura.
