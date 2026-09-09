Restaurante App - Semana 13

Base gráfica inicial usando Tkinter.

Estructura principal:
restaurante_app/
├── datos/ (productos.json, usuarios.json)
├── modelos/ (producto.py, usuario.py)
├── servicios/ (archivo_servicio.py, restaurante_servicio.py)
├── ui/ (login_view.py, main_view.py)
└── main.py

Propósito
Adaptar la estructura del repositorio docente para comenzar la versión gráfica del proyecto restaurante_app.

Ejecución
Desde la carpeta "Semana 13" (carpeta padre) ejecutar:

python .\restaurante_app\main.py

O también:

python -m restaurante_app.main

Flujo
1) Se muestra LoginView (identificación + contraseña). La comprobación es pedagógica: la contraseña se compara con el campo "correo" del usuario.
2) Al ingresar credenciales válidas se muestra MainView en la misma ventana.
3) MainView permite visualizar Usuarios y Productos cargados desde datos/*.json.
4) Cerrar sesión regresa a LoginView.

Notas
- La autenticación no es real, solo una simulación para la actividad.
- Las operaciones de lectura se realizan mediante los servicios, las vistas no leen directamente los archivos JSON.
