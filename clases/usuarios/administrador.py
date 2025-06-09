# Módulos necesarios
from clases.usuarios.cliente import Cliente
from clases.usuarios.empleado import Empleado
from clases.direccion import Direcciones_empleado
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
        print('\nMis datos personales son:')
        print(f'1. ID: {self.id_administrador}')
        print(f'2. Nombre y Apellido: {self.nombre} {self.apellido}')
        print(f'3. Email: {self.email}')
        print(f'4. Clave: {self.clave}')
        print(f'5. CVU: {self.cvu_administrador}')
        print(f'6. Alias: {self.alias_administrador}')

    # Función para mostrar los clientes
    def mostrar_clientes(self, diccionario_clientes):
        if not diccionario_clientes:
            print('\n¡No hay clientes registrados!')
        else:
            print('\nLos clientes registrados son:')
            for cliente in diccionario_clientes.keys():
                print(f'- {cliente}')

    # Función para mostrar los empleados
    def mostrar_empleados(self, diccionario_empleados):
        if not diccionario_empleados:
            print('\n¡No hay empleados registrados!')
        else:
            print('\nLos empleados registrados son:')
            for empleado in diccionario_empleados.keys():
                print(f'- {empleado}')

    # Función para mostrar los administradores
    def mostrar_administradores(self, diccionario_administradores):
        if not diccionario_administradores:
            print('\n¡No hay administradores registrados!')
        else:
            print('\nLos administradores registrados son:')
            for administrador in diccionario_administradores.keys():
                print(f'- {administrador}')

    # Función para designar como administrador
    def cambiar_rol_administrador(self, diccionario_clientes, diccionario_empleados, diccionario_administradores, usuario_a_cambiar):

        # Proceso para convertir cliente en administrador
        if usuario_a_cambiar in diccionario_clientes:
            cliente = diccionario_clientes[usuario_a_cambiar]

            while True:
                cvu = input(f'\nIngrese el CVU para {cliente.nombre} {cliente.apellido}: ').replace(" ", "")
                alias = input(f'Ingrese el alias para {cliente.nombre} {cliente.apellido}: ').replace(" ", "")

                if not cvu or not alias:
                    print('¡Error! Campo/s inválido/s. Pruebe nuevamente...')
                    continue
                if len(cvu) != 22:
                    print('¡Error! El CVU debe contener 22 dígitos. Pruebe nuevamente...')
                    continue
                if len(alias) < 6 or len(alias) > 20:
                    print('¡Error! El alias debe contener entre 6 y 20 caracteres. Pruebe nuevamente...')
                    continue
                break

            nuevo_id = len(diccionario_administradores) + 1
            nuevo_admin = Administrador(
                id_administrador=nuevo_id,
                nombre=cliente.nombre,
                apellido=cliente.apellido,
                email=cliente.email,
                clave=cliente.clave,
                cvu_administrador=cvu,
                alias_administrador=alias
            )

            diccionario_administradores[usuario_a_cambiar] = nuevo_admin
            del diccionario_clientes[usuario_a_cambiar]

            print(f'\n¡Éxito! El cliente "{cliente.nombre} {cliente.apellido}" ahora es administrador.')
        # Proceso para convertir empleado en administrador
        elif usuario_a_cambiar in diccionario_empleados:
            empleado = diccionario_empleados[usuario_a_cambiar]

            if not hasattr(empleado, 'cvu_empleado') or not hasattr(empleado, 'alias_empleado'):
                print(f'\nError: El empleado "{empleado.nombre} {empleado.apellido}" no tiene CVU o alias asignado. No se puede convertir.')
                return

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

            diccionario_administradores[usuario_a_cambiar] = nuevo_admin
            del diccionario_empleados[usuario_a_cambiar]

            print(f'\n¡Éxito! El empleado "{empleado.nombre} {empleado.apellido}" ahora es administrador.')
        # Si no existe
        else:
            print('\nNo existe ningún usuario con esos datos.')

    # Función para designar como empleado
    def cambiar_rol_empleado(self, diccionario_clientes, diccionario_empleados, diccionario_administradores, usuario_a_cambiar):
        email_clientes = diccionario_clientes.keys()
        email_administradores = diccionario_administradores.keys()

        primer_admin = list(diccionario_administradores.keys())[0]

        # Proceso para convertir cliente en empleado
        if usuario_a_cambiar in email_clientes:
            cliente = diccionario_clientes[usuario_a_cambiar]

            while True:
                cvu = input(f'\nIngrese el CVU para {cliente.nombre} {cliente.apellido}: ').replace(" ", "")  
                alias = input(f'Ingrese el alias para {cliente.nombre} {cliente.apellido}: ').replace(" ", "")

                if not cvu or not alias:
                    print('¡Error! Campo/s inválido/s. Pruebe nuevamente...')
                    continue
                if len(cvu) != 22 or not cvu.isdigit():
                    print('¡Error! El CVU debe contener exactamente 22 dígitos numéricos.')
                    continue
                if len(alias) < 6 or len(alias) > 20:
                    print('¡Error! El alias debe contener entre 6 y 20 caracteres.')
                    continue
                break

            direccion_default = Direcciones_empleado(
                id_direccion=len(diccionario_empleados) + 1,
                provincia="Provincia sin definir",
                localidad="Localidad sin definir",
                barrio="Barrio sin definir",
                calle="Calle sin definir",
                altura=0,
                piso=0
            )

            nuevo_empleado = Empleado(
                dni_empleado=cliente.dni_cliente,
                direccion=direccion_default,
                nombre=cliente.nombre,
                apellido=cliente.apellido,
                email=cliente.email,
                clave=cliente.clave,
                telefono=cliente.telefono,
                fecha_ingreso=cliente.fecha_registro,
                estado='libre',
                cvu_empleado=cvu,
                alias_empleado=alias
            )

            diccionario_empleados[usuario_a_cambiar] = nuevo_empleado
            del diccionario_clientes[usuario_a_cambiar]

            print(f'\n¡Éxito! El cliente "{cliente.nombre} {cliente.apellido}" ahora es empleado.')
        # Proceso para convertir administrador en empleado
        elif usuario_a_cambiar in email_administradores:

            if usuario_a_cambiar != primer_admin:
                administrador = diccionario_administradores[usuario_a_cambiar]

                while True:
                    dni = input('Ingrese por favor su DNI: ').replace(" ", "").replace(".", "")
                    telefono = input('Ingrese por favor su número de teléfono (incluyendo característica): ').replace(" ", "").replace("+", "")

                    if not dni or not telefono:
                        print('¡Error! Campo/s vacío/s no permitido/s. Pruebe nuevamente...')
                        continue

                    if len(dni) < 7 or not dni.isdigit():
                        print('¡Error! El DNI debe contener al menos 7 dígitos numéricos')
                        continue

                    if len(telefono) < 10 or len(telefono) > 15 or not telefono.isdigit():
                        print('¡Error! El teléfono debe tener entre 10 y 15 dígitos numéricos')
                        continue

                    dni = int(dni)
                    telefono = int(telefono)
                    break

                direccion_default = Direcciones_empleado(
                    id_direccion=len(diccionario_empleados) + 1,
                    provincia="Provincia sin definir",
                    localidad="Localidad sin definir",
                    barrio="Barrio sin definir",
                    calle="Calle sin definir",
                    altura=0,
                    piso=0
                )

                nuevo_empleado = Empleado(
                    dni_empleado=dni,
                    direccion=direccion_default,
                    nombre=administrador.nombre,
                    apellido=administrador.apellido,
                    email=administrador.email,
                    clave=administrador.clave,
                    telefono=telefono,
                    fecha_ingreso=datetime.now(),
                    estado='libre',
                    cvu_empleado=administrador.cvu_administrador,
                    alias_empleado=administrador.alias_administrador
                )

                diccionario_empleados[usuario_a_cambiar] = nuevo_empleado
                del diccionario_administradores[usuario_a_cambiar]

                print(f'\n¡Éxito! El administrador "{administrador.nombre} {administrador.apellido}" ahora es empleado.')
            else:
                print('\n¡Error! No tienes permisos para cambiar el rol del primer administrador')
        # Si no existe
        else:
            print('No existe ningún usuario con esos datos.')
    
    # Función para designar como cliente
    def cambiar_rol_cliente(self, diccionario_clientes, diccionario_empleados, diccionario_administradores, usuario_a_cambiar):
        
        primer_admin = list(diccionario_administradores.keys())[0]

        # Proceso para convertir empleado en cliente
        if usuario_a_cambiar in diccionario_empleados:
            empleado = diccionario_empleados[usuario_a_cambiar]

            nuevo_cliente = Cliente(
                dni_cliente=empleado.dni_empleado,
                nombre=empleado.nombre,
                apellido=empleado.apellido,
                email=empleado.email,
                telefono=empleado.telefono,
                clave=empleado.clave,
                fecha_registro=empleado.fecha_ingreso
            )

            diccionario_clientes[usuario_a_cambiar] = nuevo_cliente
            del diccionario_empleados[usuario_a_cambiar]
            print(f'\n¡Éxito! El empleado "{empleado.nombre} {empleado.apellido}" ahora es cliente.')
        #Proceso para convertir administrador en cliente
        elif usuario_a_cambiar in diccionario_administradores:

            if usuario_a_cambiar != primer_admin:
                administrador = diccionario_administradores[usuario_a_cambiar]

                while True:
                    dni_administrador = input('\nIngrese por favor su DNI: ').replace(" ", "").replace(".", "")
                    telefono_administrador = input('Ingrese su número de teléfono: ').replace(" ", "").replace("+", "")

                    if not dni_administrador or not telefono_administrador:
                        print('¡Error! Campo/s vacío/s no permitido/s.')
                        continue

                    if len(dni_administrador) < 6 or not dni_administrador.isdigit():
                        print('¡Error! DNI inválido.')
                        continue

                    if not (10 <= len(telefono_administrador) <= 15) or not telefono_administrador.isdigit():
                        print('¡Error! Teléfono inválido.')
                        continue

                    dni_administrador = int(dni_administrador)
                    telefono_administrador = int(telefono_administrador)
                    break

                nuevo_cliente = Cliente(
                    dni_cliente=dni_administrador,
                    nombre=administrador.nombre,
                    apellido=administrador.apellido,
                    email=administrador.email,
                    telefono=telefono_administrador,
                    clave=administrador.clave,
                    fecha_registro=datetime.now()
                )

                diccionario_clientes[usuario_a_cambiar] = nuevo_cliente
                del diccionario_administradores[usuario_a_cambiar]
                print(f'\n¡Éxito! El administrador "{administrador.nombre} {administrador.apellido}" ahora es cliente.')
            else:
                print('\n¡Error! No tienes permisos para cambiar el rol del primer administrador')
        # Si no existe
        else:
            print('No existe ningún usuario con esos datos')

    # Función para eliminar un cliente
    def eliminar_cliente(self, diccionario_clientes, email_a_eliminar):
        email_a_eliminar = email_a_eliminar.replace(" ", "")
        
        if not email_a_eliminar:
            print("\n¡Error! Email inválido.")
            return
        
        if email_a_eliminar in diccionario_clientes:
            del diccionario_clientes[email_a_eliminar]
            print('\n¡Éxito! El cliente ha sido eliminado correctamente.')
        else:
            print('\n¡Error! El email no se encuentra entre los clientes.')

    # Función para eliminar un empleado
    def eliminar_empleado(self, diccionario_empleados, email_a_eliminar):

        email_a_eliminar = email_a_eliminar.replace(" ", "")
        
        if not email_a_eliminar:
            print("\n¡Error! Email inválido.")
            return

        if email_a_eliminar in diccionario_empleados:
            del diccionario_empleados[email_a_eliminar]
            print('\n¡Éxito! El empleado ha sido eliminado correctamente.')
        else:
            print('\n¡Error! El email no se encuentra entre los empleados.')

    # Función para eliminar un administrador
    def eliminar_administrador(self, diccionario_administradores, email_ejecutor, email_a_eliminar):

        email_a_eliminar = email_a_eliminar.replace(" ", "")

        primer_admin = list(diccionario_administradores.keys())[0]

        if email_a_eliminar not in diccionario_administradores:
            print('\n¡Error! El email no se encuentra entre los administradores.')
            return

        if email_a_eliminar == primer_admin:
            print('\n¡Error! No tienes permisos para eliminar este administrador (primer administrador protegido).')
            return

        if email_ejecutor != primer_admin:
            print('\n¡Error! Solo el primer administrador puede eliminar otros administradores.')
            return

        del diccionario_administradores[email_a_eliminar]
        print('\n¡Éxito! El administrador ha sido eliminado correctamente.')