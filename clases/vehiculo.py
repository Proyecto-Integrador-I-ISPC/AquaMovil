from usuarios.cliente import Cliente

class Vehiculo:
    def __init__(self, patente, cliente: Cliente, marca, nombre, modelo, color, tipo):
        self.patente = patente
        self.dni_cliente = cliente.dni_cliente
        self.marca = marca
        self.nombre = nombre
        self.modelo = modelo
        self.color = color
        self.tipo = tipo