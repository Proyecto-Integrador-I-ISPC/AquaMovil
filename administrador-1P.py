''' PRIMERA PARTE DE ADMINISTRADOR '''

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

    # Función para designar como administrador
    def cambiar_rol_administrador(self, diccionario_clientes, diccionario_empleados, diccionario_administradores):
        email_clientes = list(diccionario_clientes.keys())
        email_empleados = list(diccionario_empleados.keys())

        for email in email_clientes:
            cliente = diccionario_clientes[email]
            
            nuevo_id = len(diccionario_administradores) + 1
            
            while (True):

                cvu = input(f'Ingrese el CVU para {cliente.nombre} {cliente.apellido}:\n')
                alias = input(f'Ingrese el alias para {cliente.nombre} {cliente.apellido}:\n')
                cvu = cvu.replace(" ", "")  
                alias = alias.replace(" ", "")

                if not cvu or not alias:
                    print('¡Error! Campo/s inválido/s. Pruebe nuevamente...')
                else:
                    if len(cvu) != 22:
                        print('¡Error! El CVU debe contener 22 dígitos. Pruebe nuevamente...')
                    elif len(alias) < 6 or len(alias) > 20:
                        print('¡Error! El alias debe contener entre 6 y 20 carácteres. Pruebe nuevamente...')
                    else:
                        print('¡Éxito! CVU y alias creado correctamente.')
                        break
                        
            nuevo_admin = Administrador(
                id_administrador=nuevo_id,
                nombre=cliente.nombre,
                apellido=cliente.apellido,
                email=cliente.email,
                clave=cliente.clave,
                cvu_administrador=cvu,
                alias_administrador=alias
            )

            diccionario_administradores[email] = nuevo_admin
            del diccionario_clientes[email]

            print(f'¡Éxito! El cliente "{cliente.nombre} {cliente.apellido}" ahora es administrador.')


        for email in email_empleados:
            empleado = diccionario_empleados[email]

            nuevo_id = len(diccionario_administradores) + 1
                
            nuevo_admin = Administrador(
                id_administrador=nuevo_id,
                nombre=empleado.nombre,
                apellido=empleado.apellido,
                email=empleado.email,
                clave=empleado.clave,
                cvu_administrador=empleado.cvu_empleado,
                alias_administrador=empleado.alias_empleado
            )
            del diccionario_empleados[email]
            diccionario_administradores[email] = nuevo_admin
            print(f'¡Éxito! El empleado "{empleado.nombre} {empleado.apellido}" ahora es administrador.')

    # Función para designar como empleado
    def cambiar_rol_empleado(self, diccionario_clientes, diccionario_empleados, diccionario_administradores):
        email_clientes = list(diccionario_clientes.keys())
        email_administradores = list(diccionario_administradores.keys())

        for email in email_clientes:
            cliente = diccionario_clientes[email]
            
            while (True):

                cvu = input(f'Ingrese el CVU para {cliente.nombre} {cliente.apellido}:\n')
                alias = input(f'Ingrese el alias para {cliente.nombre} {cliente.apellido}:\n')
                cvu = cvu.replace(" ", "")  
                alias = alias.replace(" ", "")

                if not cvu or not alias:
                    print('¡Error! Campo/s inválido/s. Pruebe nuevamente...')
                else:
                    if len(cvu) != 22:
                        print('¡Error! El CVU debe contener 22 dígitos. Pruebe nuevamente...')
                    elif len(alias) < 6 or len(alias) > 20:
                        print('¡Error! El alias debe contener entre 6 y 20 carácteres. Pruebe nuevamente...')
                    else:
                        print('¡Éxito! CVU y alias creado correctamente.')
                        break