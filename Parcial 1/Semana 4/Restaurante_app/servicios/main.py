
from modelos.producto import Producto
from modelos.cliente import Cliente
from servicios.restaurante import Restaurante

if __name__ == "__main__":

    mi_restaurante = Restaurante("Sushi Bar", "Guayaquil", "Mall del Sol")

    prod1 = Producto("S001", "Sushi Especial Langostino Tempura", 24.50, "Especialidad")
    prod2 = Producto("S002", "Rollos de Salmón Ahumado con Queso Crema", 22.75, "Plato Fuerte")
    prod3 = Producto("S003", "Sashimi de Atún Rojo (12 cortes)", 28.30, "Especialidad")
    prod4 = Producto("S004", "Rollos Dragón con Anguila y Aguacate", 26.90, "Especialidad")
    prod5 = Producto("B001", "Jugo de Fruta de la Pasión Premium", 7.50, "Bebida")
    prod6 = Producto("B002", "Vino Blanco Sauvignon Blanc (Copa)", 12.00, "Bebida")

    mi_restaurante.registrar_producto(prod1)
    mi_restaurante.registrar_producto(prod2)
    mi_restaurante.registrar_producto(prod3)
    mi_restaurante.registrar_producto(prod4)
    mi_restaurante.registrar_producto(prod5)
    mi_restaurante.registrar_producto(prod6)

    cli1 = Cliente("CL01", "Wilber Ramírez", "0998765432")
    cli2 = Cliente("CL02", "Luiggi Calero", "0987654321")
    cli3 = Cliente("CL03", "Miguel Rivera", "0976543210")

    mi_restaurante.registrar_cliente(cli1)
    mi_restaurante.registrar_cliente(cli2)
    mi_restaurante.registrar_cliente(cli3)

    cli1.agregar_pedido(prod1)
    cli1.agregar_pedido(prod6)

    cli2.agregar_pedido(prod3)
    cli2.agregar_pedido(prod5)

    cli3.agregar_pedido(prod2)
    cli3.agregar_pedido(prod4)
    cli3.agregar_pedido(prod6)

    mi_restaurante.mostrar_menu()
    mi_restaurante.mostrar_clientes()
    mi_restaurante.mostrar_consumo_cliente("CL01")
    mi_restaurante.mostrar_consumo_cliente("CL02")
    mi_restaurante.mostrar_consumo_cliente("CL03")
