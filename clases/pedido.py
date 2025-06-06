

class Pedidos:
    def __init__(self, id_pedido, cliente: Cliente, empleado: Empleado, servicio: Servicio, vehiculo: Vehiculo, fecha_pedido, provincia, localidad, barrio, calle, altura, estado, piso =   'no_especificado', observaciones = 'sin_observaciones'):
        self.id_pedido = id_pedido
        self.dni_cliente = cliente.dni_cliente
        self.dni_empleado = empleado.dni_empleado
        self.id_servicio = servicio.id_servicio
        self.patente = vehiculo.patente
        self.fecha_pedido = fecha_pedido
        self.provincia = provincia
        self.localidad = localidad
        self.barrio = barrio
        self.calle = calle
        self.altura = altura
        self.piso = piso
        self.estado = estado
        self.observaciones = observaciones
        