from modelos.producto import Producto
from modelos.cliente import Cliente
from servicios.restaurante import Restaurante

# Punto de arranque del programa: crea objetos, los registra en el servicio y muestra la información
if __name__ == "__main__":

    mi_restaurante = Restaurante("Sushi Bar", "Guayaquil", "Mall del Sol")

    # Crear productos (al menos dos)
    prod1 = Producto("S001", "Sushi Especial Langostino Tempura", 24.50, "Especialidad")
    prod2 = Producto("S002", "Rollos de Salmón Ahumado con Queso Crema", 22.75, "Plato Fuerte")

    # Registrar productos en el servicio
    mi_restaurante.registrar_producto(prod1)
    mi_restaurante.registrar_producto(prod2)

    # Crear clientes (al menos dos)
    cli1 = Cliente("CL01", "Wilber Ramírez", "0998765432")
    cli2 = Cliente("CL02", "Luiggi Calero", "0987654321")

    # Registrar clientes en el servicio
    mi_restaurante.registrar_cliente(cli1)
    mi_restaurante.registrar_cliente(cli2)

    # Simular pedidos
    cli1.agregar_pedido(prod1)
    cli1.agregar_pedido(prod2)

    cli2.agregar_pedido(prod2)

    # Mostrar información organizada en consola
    mi_restaurante.mostrar_menu()
    mi_restaurante.mostrar_clientes()
    mi_restaurante.mostrar_consumo_cliente("CL01")
    mi_restaurante.mostrar_consumo_cliente("CL02")
