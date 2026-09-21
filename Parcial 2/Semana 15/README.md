# Restaurante App - Semana 15

Esta versión evoluciona el proyecto de la Semana 14 sin reconstruir su arquitectura. Conserva el inicio de sesión, la consulta de usuarios y la gestión de productos, y agrega el módulo de ventas para demostrar el manejo básico de eventos con Tkinter.

## Estructura

- `restaurante_app/datos`: archivos `productos.json`, `usuarios.json` y `ventas.json`.
- `restaurante_app/modelos`: `Producto`, `Usuario` y `Venta`.
- `restaurante_app/servicios`: persistencia en `ArchivoServicio` y reglas de negocio en `RestauranteServicio`.
- `restaurante_app/ui`: `LoginView` y `MainView`.
- `restaurante_app/assets`: logotipo e icono PPM utilizados en la cabecera y el login.

## Flujo de ventas

En la sección **Ventas**, dos `ttk.Combobox` permiten seleccionar un usuario y un producto existentes. El botón `Registrar venta` usa `command=self.registrar_venta`; el callback obtiene las selecciones y delega la validación y el registro a `RestauranteServicio`. El servicio crea una `Venta`, la persiste mediante `ArchivoServicio` en `datos/ventas.json` y la vista actualiza el `Treeview` para mostrar inmediatamente la respuesta.

La interfaz no lee ni escribe JSON directamente. Las validaciones de existencia de usuario y producto permanecen en la capa de servicios.

## Ejecución

Desde la raíz del repositorio:

```bash
python "Parcial 2/Semana 15/restaurante_app/main.py"
```

Credenciales de demostración: `admin / admin123`.
