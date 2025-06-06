


# Creación de clase
class Empleado:

    # Función inicial: INIT
    def __init__(self, dni_empleado, direccion, nombre, apellido, email, clave, telefono, fecha_ingreso, cvu_empleado, alias_empleado, estado='libre'):
        self.dni_empleado = dni_empleado
        self.id_direccion = direccion
        self.nombre = nombre
        self.apellido = apellido
        self.email = email
        self.clave = clave
        self.telefono = telefono
        self.fecha_ingreso = fecha_ingreso
        self.estado = estado
        self.cvu_empleado = cvu_empleado
        self.alias_empleado = alias_empleado

    # Función para mostrar nombre completo
    def nombre_completo(self):
        print(f'Nombre: {self.nombre} Apellido: {self.apellido}')
    
    # Función para mostrar datos personales
    def mostrar_datos_personales(self):
        print('Mis datos personales son:')
        print(f'1. Nombre y Apellido: {self.nombre} {self.apellido}')
        print(f'2. DNI: {self.dni_empleado}')
        print(f'3. Email: {self.email}')
        print(f'4. Clave: {self.clave}')
        print(f'5. Teléfono: {self.clave}')
        print(f'6. Fecha de ingreso: {self.fecha_ingreso}')
        print(f'7. Estado: {self.estado}')
        print(f'8. CVU: {self.cvu_empleado}')
        print(f'9. Alias: {self.alias_empleado}')
        