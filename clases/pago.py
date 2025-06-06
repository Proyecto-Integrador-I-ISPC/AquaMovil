from clases.pedido import Pedidos

class Pago:
    def __init__(self, id_pago, pedido:Pedidos, tipo_pago, monto, fecha_pago, estado_pago):
        self.id_pago = id_pago
        self.id_pedido = pedido.id_pedido
        self.tipo_pago = tipo_pago
        self.monto = monto
        self.fecha_pago = fecha_pago
        self.estado_pago = estado_pago