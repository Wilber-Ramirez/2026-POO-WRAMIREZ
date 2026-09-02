from __future__ import annotations

import sys
from pathlib import Path

if __package__ is None or __package__ == "":
    sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from restaurante_app.servicios.restaurante import Restaurante
from restaurante_app.modelos.producto import Producto
from restaurante_app.modelos.usuario import Usuario


def run_test():
    print('INICIO DE PRUEBA')
    r = Restaurante()

    # Limpiar archivos de datos para prueba
    r._archivo_servicio.guardar_productos([])
    r._archivo_servicio.guardar_usuarios([])
    r._archivo_servicio.guardar_ventas([])

    # Reconstruir restaurante para cargar listas vacías e índices vacíos
    r = Restaurante()
    print('Productos iniciales:', r.listar_productos())
    print('Usuarios iniciales:', r.listar_usuarios())
    print('Ventas iniciales:', r.listar_ventas())

    # Registrar usuario y producto
    u = Usuario('123', 'Test User', 'test@example.com')
    ok_u = r.registrar_usuario(u)
    print('Registrar usuario OK:', ok_u)

    p = Producto('P001', 'Pizza', 'Comida', 10.5, stock=5)
    ok_p = r.registrar_producto(p)
    print('Registrar producto OK:', ok_p)

    # Búsquedas optimizadas
    found_p = r.buscar_producto('P001')
    found_u = r.buscar_usuario('123')
    print('Buscar producto P001:', 'Encontrado' if found_p else 'No encontrado')
    print('Buscar usuario 123:', 'Encontrado' if found_u else 'No encontrado')

    # Realizar venta
    ok_v = r.vender_producto('P001', '123', 2)
    print('Venta realizada OK:', ok_v)

    # Comprobar stock y ventas por usuario
    prod_after = r.buscar_producto('P001')
    print('Stock después de venta (esperado 3):', prod_after.stock if prod_after else 'N/D')

    ventas_user = r.ventas_por_usuario('123')
    print('Ventas para usuario 123 (len):', len(ventas_user))
    for v in ventas_user:
        print('-', v.usuario_id, v.producto_codigo, v.cantidad)

    # Reiniciar aplicación para comprobar reconstrucción de índices
    r2 = Restaurante()
    print('--- Después de reinicio ---')
    found_p2 = r2.buscar_producto('P001')
    print('Buscar producto P001 tras reinicio:', 'Encontrado' if found_p2 else 'No encontrado')
    ventas_user2 = r2.ventas_por_usuario('123')
    print('Ventas para usuario 123 tras reinicio (len):', len(ventas_user2))

    print('FIN DE PRUEBA')


if __name__ == '__main__':
    run_test()
