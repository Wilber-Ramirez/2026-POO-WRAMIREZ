
class Cliente:

    def __init__(self, id_cliente, nombre, telefono):
        self.id_cliente = id_cliente
        self.nombre = nombre
        self.telefono = telefono
        self.pedidos = []

    def agregar_pedido(self, producto):
        self.pedidos.append(producto)

    def calcular_total(self):
        total = sum(prod.precio for prod in self.pedidos)
        return total

    def __str__(self):
        return f"ID: {self.id_cliente} | Nombre: {self.nombre} | Teléfono: {self.telefono}"
