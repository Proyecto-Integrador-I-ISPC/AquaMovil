class Direcciones_empleado:
    def __init__(self, id_direccion, provincia, localidad, barrio, calle, altura, piso='no_especificado'):
        self.id_direccion = id_direccion
        self.provincia = provincia
        self.localidad = localidad
        self.barrio = barrio
        self.calle = calle
        self.altura = altura
        self.piso = piso