# Creación de clase
class Cliente:

    # Función inicial: INIT
    def __init__(self, dni_cliente, nombre, apellido, email, telefono, clave, fecha_registro):
        self.dni_cliente = dni_cliente
        self.nombre = nombre
        self.apellido = apellido
        self.email = email
        self.telefono = telefono
        self.clave = clave
        self.fecha_registro = fecha_registro

    # Función para mostrar nombre completo
    def nombre_completo(self):
        print(f'Nombre: {self.nombre} Apellido: {self.apellido}')
    
    # Función para mostrar datos personales
    def mostrar_datos_personales(self):
        print('Mis datos personales son:')
        print(f'1. Nombre y Apellido: {self.nombre} {self.apellido}')
        print(f'2. DNI: {self.dni_cliente}')
        print(f'3. Email: {self.email}')
        print(f'4. Clave: {self.clave}')
        print(f'5. Teléfono: {self.clave}')
        print(f'6. Fecha de registro: {self.fecha_registro}')
