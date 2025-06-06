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
                        
            nuevo_empleado = cliente(
                dni_empleado = cliente.dni_cliente,
                id_direccion = len(diccionario_empleados) + 1,
                nombre = cliente.nombre,
                apellido = cliente.apellido,
                email = cliente.email,
                clave = cliente.clave,
                telefono = cliente.telefono,
                fecha_ingreso = cliente.fecha_ingreso,
                estado = 'libre',
                cvu_empleado = cvu,
                alias_empleado = alias
            )

            diccionario_empleados[email] = nuevo_empleado
            del diccionario_clientes[email]

            print(f'¡Éxito! El cliente "{cliente.nombre} {cliente.apellido}" ahora es empleado.')


        for email in email_administradores:
            administrador = diccionario_empleados[email]

            while (True):
                dni_administrador = input('Ingrese por favor su DNI:\n')
                dni_administrador = dni_administrador.replace(" ", "")
                dni_administrador = dni_administrador.replace(".", "")
                telefono_administrador = input('Ingrese por favor su número de teléfono (incluyendo característica):\n')
                telefono_administrador = telefono_administrador.replace(" ", "")
                telefono_administrador = telefono_administrador.replace("+", "")

                if not dni_administrador or not telefono_administrador:
                    print('¡Error! Campo/s vacío/s no permitido/s. Pruebe nuevamente...')
                else:
                    if len(dni_administrador) < 6:
                        print('¡Error! El DNI debe contener al menos 7 dígitos')
                    else:
                        try:
                            dni_administrador = int(dni_administrador)
                            break
                        except ValueError:
                            print('¡Error! Digitos no válidos. Pruebe nuevamente')
                    if len(telefono_administrador) < 10 or len(telefono_administrador) > 15:
                        print('¡Error! El teléfono debe tener más de 10 dígitos y menos de 15')
                    else:
                        try:
                            telefono_administrador = int(telefono_administrador)
                            break
                        except ValueError:
                            print('¡Error! Digitos no válidos. Pruebe nuevamente')

            nuevo_empleado = Administrador(
                dni_empleado = dni_administrador,
                id_direccion = len(diccionario_empleados) + 1,
                nombre = administrador.nombre,
                apellido = administrador.apellido,
                email = administrador.email,
                clave = administrador.clave,
                telefono = telefono_administrador,
                fecha_ingreso = datetime.now(),
                estado = 'libre',
                cvu_empleado = administrador.cvu_administrador,
                alias_empleado = administrador.alias_administrador
            )

            diccionario_empleados[email] = nuevo_empleado
            del diccionario_administradores[email]

            print(f'¡Éxito! El administrador "{administrador.nombre} {administrador.apellido}" ahora es empleado.')
    
    # Función para designar como cliente
    def cambiar_rol_cliente(self, diccionario_clientes, diccionario_empleados, diccionario_administradores):
        email_empleados = list(diccionario_empleados.keys())
        email_administradores = list(diccionario_administradores.keys())

        for email in email_empleados:

            empleado = diccionario_empleados[email]
            
            nuevo_cliente = empleado(
                dni_cliente = empleado.dni_empleado,
                nombre = empleado.nombre,
                apellido = empleado.apellido,
                email = empleado.email,
                telefono = empleado.telefono,
                clave = empleado.clave,
                fecha_registro = empleado.fecha_ingreso
            )

            diccionario_clientes[email] = nuevo_cliente
            del diccionario_empleados[email]

            print(f'¡Éxito! El empleado "{empleado.nombre} {empleado.apellido}" ahora es cliente.')


        for email in email_administradores:
            administrador = diccionario_empleados[email]

            while (True):
                
                dni_administrador = input('Ingrese por favor su DNI:\n')
                dni_administrador = dni_administrador.replace(" ", "")
                dni_administrador = dni_administrador.replace(".", "")
                telefono_administrador = input('Ingrese por favor su número de teléfono (incluyendo característica):\n')
                telefono_administrador = telefono_administrador.replace(" ", "")
                telefono_administrador = telefono_administrador.replace("+", "")

                if not dni_administrador or not telefono_administrador:
                    print('¡Error! Campo/s vacío/s no permitido/s. Pruebe nuevamente...')
                else:
                    if len(dni_administrador) < 6:
                        print('¡Error! El DNI debe contener al menos 7 dígitos')
                    else:
                        try:
                            dni_administrador = int(dni_administrador)
                            break
                        except ValueError:
                            print('¡Error! Digitos no válidos. Pruebe nuevamente')
                    if len(telefono_administrador) < 10 or len(telefono_administrador) > 15:
                        print('¡Error! El teléfono debe tener más de 10 dígitos y menos de 15')
                    else:
                        try:
                            telefono_administrador = int(telefono_administrador)
                            break
                        except ValueError:
                            print('¡Error! Digitos no válidos. Pruebe nuevamente')

            nuevo_cliente = Administrador(
                dni_cliente = dni_administrador,
                nombre = administrador.nombre,
                apellido = administrador.apellido,
                email = administrador.email,
                telefono = telefono_administrador,
                clave = administrador.clave,
                fecha_registro = datetime.now()
            )

            diccionario_clientes[email] = nuevo_cliente
            del diccionario_administradores[email]

            print(f'¡Éxito! El administrador "{administrador.nombre} {administrador.apellido}" ahora es cliente.')
    
    # Función para eliminar un cliente
    def eliminar_cliente(self, diccionario_clientes):

        while (True):

            email_a_eliminar = input('Ingresa el email del cliente que deseas eliminar:\n')
            email_a_eliminar = email_a_eliminar.replace(" ", "")
            
            if not email_a_eliminar:
                print("¡Error! Email inválido. Pruebe nuevamente...")
            else:
                break
        
        if email_a_eliminar in diccionario_clientes:
            del diccionario_clientes[email_a_eliminar]
            print('¡Éxito! El cliente ha sido eliminado correctamente.')
        else:
            print('¡Error! El email no se encuentra entre los clientes.')

    # Función para eliminar un empleado
    def eliminar_empleado(self, diccionario_empleados):

        while (True):

            email_a_eliminar = input('Ingresa el email del cliente que deseas eliminar:\n')
            email_a_eliminar = email_a_eliminar.replace(" ", "")
            
            if not email_a_eliminar:
                print("¡Error! Email inválido. Pruebe nuevamente...")
            else:
                break

        if email_a_eliminar in diccionario_empleados:
            del diccionario_empleados[email_a_eliminar]
            print('¡Éxito! El empleado ha sido eliminado correctamente.')
        else:
            print('¡Error! El email no se encuentra entre los empleados.')

    # Función para eliminar un administrador
    def eliminar_administrador(self, diccionario_administradores, administrador):

        while (True):

            email_a_eliminar = input('Ingresa el email del cliente que deseas eliminar:\n')
            email_a_eliminar = email_a_eliminar.replace(" ", "")
            
            if not email_a_eliminar:
                print("¡Error! Email inválido. Pruebe nuevamente...")
            else:
                break

        primer_admin = list(diccionario_administradores.keys())[0]
        
        if email_a_eliminar in diccionario_administradores:
            if email_a_eliminar == primer_admin:
                print('¡Error! No tienes permisos para eliminar este administrador.')
            elif administrador != primer_admin:
                print('¡Error! No tienes permisos para eliminar este administrador.')
            else:
                del diccionario_administradores[email_a_eliminar]
                print('¡Éxito! El administrador ha sido eliminado correctamente.')
        else:
            print('¡Error! El email no se encuentra entre los administradores.')