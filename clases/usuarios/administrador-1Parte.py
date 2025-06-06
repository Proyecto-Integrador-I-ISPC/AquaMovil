# Módulos necesarios
from datetime import datetime

# Creación de clase
class Administrador:

    # Función inicial: INIT
    def __init__(self, id_administrador, nombre, apellido, email, clave, cvu_administrador, alias_administrador):
        self.id_administrador = id_administrador
        self.nombre = nombre
        self.apellido = apellido
        self.email = email
        self.clave = clave
        self.cvu_administrador = cvu_administrador
        self.alias_administrador = alias_administrador
    
    # Función para mostrar datos personales
    def mostrar_datos_personales(self):
        print('Mis datos personales son:')
        print(f'1. ID: {self.id_administrador}')
        print(f'2. Nombre y Apellido: {self.nombre} {self.apellido}')
        print(f'3. Email: {self.email}')
        print(f'4. Clave: {self.clave}')
        print(f'5. CVU: {self.cvu_administrador}')
        print(f'6. Alias: {self.alias_administrador}')

    # Función para mostrar los clientes
    def mostrar_clientes(self, diccionario_clientes):
        if not diccionario_clientes:
            print('¡No hay clientes registrados!')
        else:
            print('Los clientes registrados son:')
            for cliente in diccionario_clientes.keys():
                print(f'- {cliente}')

    # Función para mostrar los empleados
    def mostrar_empleados(self, diccionario_empleados):
        if not diccionario_empleados:
            print('¡No hay empleados registrados!')
        else:
            print('Los empleados registrados son:')
            for empleado in diccionario_empleados.keys():
                print(f'- {empleado}')

    # Función para mostrar los administradores
    def mostrar_administradores(self, diccionario_administradores):
        if not diccionario_administradores:
            print('¡No hay administradores registrados!')
        else:
            print('Los administradores registrados son:')
            for administrador in diccionario_administradores.keys():
                print(f'- {administrador}')

    

        while (True):

            email_a_eliminar = input('Ingresa el email del cliente que deseas eliminar:\n')
            email_a_eliminar = email_a_eliminar.replace(" ", "")
            
            if not email_a_eliminar:
                print("¡Error! Email inválido. Pruebe nuevamente...")
            else:
                break