# Restaurante App - Semana 14

Aplicación gráfica de gestión de un restaurante desarrollada con Python y Tkinter. Esta versión conserva la arquitectura modular y aplica componentes y contenedores para organizar el login, la navegación, los formularios y las tablas.

## Estructura

`restaurante_app/datos` contiene `productos.json` y `usuarios.json`; `modelos` define `Producto` y `Usuario`; `servicios` concentra la persistencia y las reglas de negocio; `ui` contiene `LoginView` y `MainView`; `main.py` inicia la aplicación.

## Funcionalidades

- Inicio de sesión con el usuario de demostración `admin` y contraseña `admin123`.
- Consulta de usuarios en una tabla `ttk.Treeview`.
- Registro, carga/consulta, actualización y eliminación de productos.
- Persistencia de productos mediante `ArchivoServicio` en `datos/productos.json`.
- Validaciones de campos, precio, stock y códigos duplicados dentro de `RestauranteServicio`.

## Componentes y contenedores

Se utilizan `Frame`, `LabelFrame`, `Label`, `Entry`, `Button` y `Treeview` de `tkinter.ttk`. La navegación separa el menú lateral de la zona de contenido; el formulario y sus acciones están separados de la tabla mediante contenedores. Los botones usan `command=` y no se emplean eventos avanzados.

## Ejecución

Desde la raíz del repositorio:

```bash
python "Parcial 2/Semana 14/restaurante_app/main.py"
```

También puede ejecutarse entrando a `Parcial 2/Semana 14/restaurante_app` y usando `python main.py`.
