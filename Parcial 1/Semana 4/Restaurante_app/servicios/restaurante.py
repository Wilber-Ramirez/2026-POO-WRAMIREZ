
from modelos.producto import Producto
from modelos.cliente import Cliente


class Restaurante:

    def __init__(self, nombre_restaurante, ciudad, ubicacion):
        self.nombre = nombre_restaurante
        self.ciudad = ciudad
        self.ubicacion = ubicacion
        self.lista_productos = []
        self.lista_clientes = []

    def registrar_producto(self, producto: Producto):
        self.lista_productos.append(producto)

    def registrar_cliente(self, cliente: Cliente):
        self.lista_clientes.append(cliente)

    def mostrar_menu(self):
        print(f"\n--- MENÚ DE {self.nombre.upper()}")
        print(f"Ubicación: {self.ubicacion}, {self.ciudad} ---")
        if not self.lista_productos:
            print("Aún no hay productos registrados.")
        else:
            for producto in self.lista_productos:
                print(producto)

    def mostrar_clientes(self):
        print(f"\n--- CLIENTES REGISTRADOS ---")
        if not self.lista_clientes:
            print("Aún no hay clientes registrados.")
        else:
            for cliente in self.lista_clientes:
                print(cliente)

    def mostrar_consumo_cliente(self, id_cliente):

        cliente_encontrado = next((c for c in self.lista_clientes if c.id_cliente == id_cliente), None)

        if cliente_encontrado:
            print(f"\n--- CONSUMO DE {cliente_encontrado.nombre.upper()} ---")
            if not cliente_encontrado.pedidos:
                print("El cliente no ha realizado pedidos aún.")
            else:
                for item in cliente_encontrado.pedidos:
                    print(f"- {item.nombre} : ${item.precio:.2f}")
                print(f"** TOTAL A PAGAR: ${cliente_encontrado.calcular_total():.2f} **")
        else:
            print("\nCliente no encontrado en el sistema.")
