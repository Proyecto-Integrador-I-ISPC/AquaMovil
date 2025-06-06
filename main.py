# Importamos los módulos necesarios
from clases.usuarios.cliente import Cliente
from clases.usuarios.empleado import Empleado
from clases.usuarios.administrador import Administrador
from clases.direccion import Direcciones_empleado
from datetime import datetime

# Definimos una instancia para cada clase
cliente_uno = Cliente(
    dni_cliente='47255789',
    nombre='Magdalena',
    apellido='Cruz',
    email='magdalenacruz@gmail.com',
    telefono='549351667788',
    clave='MAgda11??',
    fecha_registro=datetime.now()
)

direccion_empleado_uno = Direcciones_empleado(
    id_direccion=1,
    provincia='Córdoba',
    localidad='Villa Animi',
    barrio='Los Palomares',
    calle='Independencia',
    altura=1504
)

empleado_uno = Empleado(
    dni_empleado='45897256',
    direccion=direccion_empleado_uno,
    nombre='Ernesto',
    apellido='Videla',
    email='ernestovidela@gmail.com',
    clave='ERnesto11??',
    telefono='549351664422',
    fecha_ingreso=datetime.now(),
    cvu_empleado='123456789101112879215',
    alias_empleado='espia.batea.cruz.mp'
)

administrador_uno = Administrador(
    id_administrador=1,
    nombre='Rafael',
    apellido='Caceres',
    email='rafaelcaceres@gmail.com',
    clave='RAfael11??',
    cvu_administrador='123456789101112878879',
    alias_administrador='monitor.cable.webcam.nx'
)

# Diccionarios
diccionario_clientes = {}
diccionario_empleados = {}
diccionario_administradores = {}

# Mensaje bienvenida
print('¡Bienvenido a AquaMóvil!')

while (True):

    print('Por favor, seleccione una opción:')
    print('1. Iniciar Sesión')
    print('2. Registrarse')
    print('3. Salir')

    respuesta = input()
    respuesta = respuesta.replace(" ", "")

    if not respuesta:
        print('¡Error! Campo vacío no permitido. Pruebe nuevamente...')
    else:
        try:
            respuesta = int(respuesta)
            match respuesta:
                case 1:
                    while (True):

                        intentos = 0

                        usuario = input('Ingrese su usuario:\n')
                        contraseña = input('Ingrese su contraseña:\n')

                        usuario = usuario.replace(" ", "")
                        contraseña = contraseña.replace(" ", "")

                        if not usuario or not contraseña:
                            print('¡Error! Campo/s vacío/s no permitido/s. Pruebe nuevamente...')
                        else: 
                            if usuario in diccionario_clientes.keys() and contraseña in diccionario_clientes.values():
                                print('¡Ingreso exitoso! Haz iniciado sesión como cliente')
                                print('Tus opciones son:')
                                while (True):
                                    print('1. Ver datos personales')
                                    print('2. Salir')
                                    respuesta_cliente = input()
                                    respuesta_cliente = respuesta_cliente.replace(" ", "")

                                    if not respuesta_cliente:
                                        print('¡Error! Campo vacío no permitido')
                                    else:
                                        try:
                                            respuesta_cliente = int(respuesta_cliente)
                                            match respuesta_cliente:
                                                case 1:
                                                    Cliente.mostrar_datos_personales()
                                                case 2:
                                                    print('Saliendo...')
                                                    break
                                                case _:
                                                    print('¡Ops! Parece que haz selecciona una opción no válida. Pruebe nuevamente...')
                                        except ValueError:
                                            print('¡Error! Ingrese un número de opción válida')
                                break
                            elif usuario in diccionario_empleados.keys() and contraseña in diccionario_empleados.values():
                                print('¡Ingreso exitoso! Haz iniciado sesión como empleado')
                                print('Tus opciones son:')
                                while (True):
                                    print('1. Ver datos personales')
                                    print('2. Salir')
                                    respuesta_empleado = input()
                                    respuesta_empleado = respuesta_empleado.replace(" ", "")

                                    if not respuesta_empleado:
                                        print('¡Error! Campo vacío no permitido')
                                    else:
                                        try:
                                            respuesta_empleado = int(respuesta_empleado)
                                            match respuesta_empleado:
                                                case 1:
                                                    Empleado.mostrar_datos_personales()
                                                case 2:
                                                    print('Saliendo...')
                                                    break
                                                case _:
                                                    print('¡Ops! Parece que haz selecciona una opción no válida. Pruebe nuevamente...')
                                        except ValueError:
                                            print('¡Error! Ingrese un número de opción válida')
                                break
                            elif usuario in diccionario_administradores.keys() and contraseña in diccionario_administradores.values():
                                print('¡Ingreso exitoso! Haz iniciado sesión como administrador')
                                while (True):
                                    print('Tus opciones son:')
                                    print('1. Ver datos personales')
                                    print('2. Ver clientes')
                                    print('3. Ver empleados')
                                    print('4. Ver administradores')
                                    print('5. Cambiar un rol')
                                    print('6. Eliminar un usuario')
                                    print('7. Salir')
                                    respuesta_administrador = input()
                                    respuesta_administrador = respuesta_administrador.replace(" ", "")

                                    if not respuesta_administrador:
                                        print('¡Error! Campo vacío no permitido')
                                    else:
                                        try:
                                            respuesta_administrador = int(respuesta_administrador)
                                            match respuesta_administrador:
                                                case 1:
                                                    Administrador.mostrar_datos_personales()
                                                case 2:
                                                    Administrador.mostrar_clientes()
                                                case 3:
                                                    Administrador.mostrar_empleados()
                                                case 4:
                                                    Administrador.mostrar_administradores()
                                                case 5:
                                                    while (True):
                                                        print('Opciones Disponibles:')
                                                        print('1. Ingrese el email del usuario que desea cambiar de rol')
                                                        print('2. Salir')
                                                        opcion_seleccionada = input()
                                                        opcion_seleccionada = opcion_seleccionada.replace(" ", "")
                                                        if not opcion_seleccionada:
                                                            print('¡Error! Campo vacío no permitido. Pruebe nuevamente...')
                                                        else:
                                                            try:
                                                                opcion_seleccionada = int(opcion_seleccionada)
                                                                match opcion_seleccionada:
                                                                    case 1:
                                                                        print('Ingrese el email:')
                                                                        usuario_a_cambiar = input()
                                                                        usuario_a_cambiar = usuario_a_cambiar.replace(" ", "")

                                                                        if not usuario_a_cambiar:
                                                                            print('¡Error! Campo vacío no permitido. Pruebe nuevamente...')
                                                                        else:
                                                                            if usuario_a_cambiar in diccionario_clientes.keys():
                                                                                print(f'El usuario con correo "{usuario_a_cambiar}" es un cliente')
                                                                                print('¿Qué rol desea asignarle?')
                                                                                while(True):
                                                                                    print('1. Empleado') 
                                                                                    print('2. Administrador')
                                                                                    print('3. Salir')
                                                                                    opcion_rol = input()
                                                                                    opcion_rol = opcion_rol.replace(" ", "")

                                                                                    if not opcion_rol:
                                                                                        print('¡Error! Campo vacío no permitido. Pruebe nuevamente...')
                                                                                    else:
                                                                                        try:
                                                                                            opcion_rol = int(opcion_rol)
                                                                                            match opcion_rol:
                                                                                                case 1:
                                                                                                    Administrador.cambiar_rol_empleado()
                                                                                                    print(f'¡Éxito! El cliente con correo "{usuario_a_cambiar}" ahora es empleado')
                                                                                                case 2:
                                                                                                    Administrador.cambiar_rol_administrador()
                                                                                                    print(f'¡Éxito! El cliente con correo "{usuario_a_cambiar}" ahora es administrador')
                                                                                                case 3:
                                                                                                    print('Saliendo...')
                                                                                                    break
                                                                                                case _:
                                                                                                    print('¡Ops! Parece que haz seleccionado una opción no válida. Pruebe nuevamente...')
                                                                                        except ValueError:
                                                                                            print('¡Error! Ingrese un número de opción válida')
                                                                            elif usuario_a_cambiar in diccionario_empleados.keys():
                                                                                print(f'El usuario con correo "{usuario_a_cambiar}" es un empleado')
                                                                                print('¿Qué rol desea asignarle?')
                                                                                while(True):
                                                                                    print('1. Cliente') 
                                                                                    print('2. Administrador')
                                                                                    print('3. Salir')
                                                                                    opcion_rol = input()
                                                                                    opcion_rol = opcion_rol.replace(" ", "")

                                                                                    if not opcion_rol:
                                                                                        print('¡Error! Campo vacío no permitido. Pruebe nuevamente...')
                                                                                    else:
                                                                                        try:
                                                                                            opcion_rol = int(opcion_rol)
                                                                                            match opcion_rol:
                                                                                                case 1:
                                                                                                    Administrador.cambiar_rol_cliente()
                                                                                                    print(f'¡Éxito! El empleado con correo "{usuario_a_cambiar}" ahora es cliente')
                                                                                                case 2:
                                                                                                    Administrador.cambiar_rol_administrador()
                                                                                                    print(f'¡Éxito! El empleado con correo "{usuario_a_cambiar}" ahora es administrador')
                                                                                                case 3:
                                                                                                    print('Saliendo...')
                                                                                                    break
                                                                                                case _:
                                                                                                    print('¡Ops! Parece que haz seleccionado una opción no válida. Pruebe nuevamente...')
                                                                                        except ValueError:
                                                                                            print('¡Error! Ingrese un número de opción válida')
                                                                            elif usuario_a_cambiar in diccionario_administradores.keys():
                                                                                print(f'El usuario con correo "{usuario_a_cambiar}" es un administrador')
                                                                                print('¿Qué rol desea asignarle?')
                                                                                while(True):
                                                                                    print('1. Cliente') 
                                                                                    print('2. Empleado')
                                                                                    print('3. Salir')
                                                                                    opcion_rol = input()
                                                                                    opcion_rol = opcion_rol.replace(" ", "")

                                                                                    if not opcion_rol:
                                                                                        print('¡Error! Campo vacío no permitido. Pruebe nuevamente...')
                                                                                    else:
                                                                                        try:
                                                                                            opcion_rol = int(opcion_rol)
                                                                                            match opcion_rol:
                                                                                                case 1:
                                                                                                    Administrador.cambiar_rol_cliente()
                                                                                                    print(f'¡Éxito! El administrador con correo "{usuario_a_cambiar}" ahora es cliente')
                                                                                                case 2:
                                                                                                    Administrador.cambiar_rol_empleado()
                                                                                                    print(f'¡Éxito! El administrador con correo "{usuario_a_cambiar}" ahora es empleado')
                                                                                                case 3:
                                                                                                    print('Saliendo...')
                                                                                                    break
                                                                                                case _:
                                                                                                    print('¡Ops! Parece que haz seleccionado una opción no válida. Pruebe nuevamente...')
                                                                                        except ValueError:
                                                                                            print('¡Error! Ingrese un número de opción válida')
                                                                            else:
                                                                                print('¡Error! El email ingresado no existe')
                                                                    case 2:
                                                                        print('Saliendo...')
                                                                        break
                                                                    case _:
                                                                        print('¡Ops! Parece que haz seleccionado una opción no válida. Pruebe nuevamente...')
                                                            except ValueError:
                                                                print('¡Error! Ingrese un número de opción válida') 
                                                case 6:
                                                    while (True):
                                                        print('Opciones Disponibles:')
                                                        print('1. Ingrese el email del usuario que desea eliminar')
                                                        print('2. Salir')
                                                        opcion_seleccionada = input()
                                                        opcion_seleccionada = opcion_seleccionada.replace(" ", "")
                                                        if not opcion_seleccionada:
                                                            print('¡Error! Campo vacío no permitido. Pruebe nuevamente...') 
                                                        else:
                                                            try:
                                                                opcion_seleccionada = int(opcion_seleccionada)
                                                                match opcion_seleccionada:
                                                                    case 1:
                                                                        print('Ingrese el email:')
                                                                        usuario_a_eliminar = input()
                                                                        usuario_a_eliminar = usuario_a_eliminar.replace(" ", "")

                                                                        if not usuario_a_eliminar:
                                                                            print('¡Error! Campo vacío no permitido. Pruebe nuevamente...')
                                                                        else:
                                                                            if usuario_a_eliminar in diccionario_clientes.keys():
                                                                                Administrador.eliminar_cliente()
                                                                                print(f'¡Éxito! El cliente "{usuario_a_eliminar}" ha sido eliminado correctamente')
                                                                            elif usuario_a_eliminar in diccionario_empleados.keys():
                                                                                Administrador.eliminar_empleado()
                                                                                print(f'¡Éxito! El empleado "{usuario_a_eliminar}" ha sido eliminado correctamente')
                                                                            elif usuario_a_eliminar in diccionario_administradores.keys() and usuario_a_eliminar != administrador_uno:
                                                                                Administrador.eliminar_administrador()
                                                                                print(f'¡Éxito! El administrador "{usuario_a_eliminar}" ha sido eliminado correctamente')
                                                                            else:
                                                                                print('¡Error! El usuario que deseas eliminar no existe')
                                                                    case 2:
                                                                        print('Saliendo...')
                                                                        break
                                                                    case _:
                                                                        print('¡Ops! Parece que haz seleccionado una opción no válida. Pruebe nuevamente...')
                                                            except ValueError:
                                                                print('¡Error! Ingrese un número de opción válida')
                                                case 7:
                                                    print('Saliendo...')
                                                    break
                                                case _:
                                                    print('¡Ops! Parece que haz seleccionado una opción no válida. Pruebe nuevamente...')
                                        except ValueError:
                                            print('¡Error! Ingrese un número de opción válida')
                                break
                            else:
                                if intentos < 3:
                                    print('No se ha encontrando ninguna cuenta asociada a esos datos')
                                    intentos = intentos + 1
                                else:
                                    print('¡Error! Vuelve a intentarlo más tarde...')
                                    break
                case 2:

                    intentos = 0

                    while(intentos < 9):

                        print('Complete el siguiente formulario para registrarse en el sistema:')


                        dni_usuario = input('DNI (sin guiones ni puntos):\n')
                        nombre_usuario = input('Nombre:\n')
                        apellido_usuario = input('Apellido:\n')
                        email_usuario = input('Email:\n')
                        telefono_usuario = input('Teléfono:\n')
                        clave_usuario = input('Genere una clave:\n')
                        fecha_registro_usuario = datetime.now()

                        dni_usuario = dni_usuario.replace(" ", "")
                        nombre_usuario = nombre_usuario.replace(" ", "")
                        apellido_usuario = apellido_usuario.replace(" ", "")
                        email_usuario = email_usuario.replace(" ","")
                        telefono_usuario = telefono_usuario.replace(" ", "")
                        clave_usuario = clave_usuario.replace(" ", "")

                        if not dni_usuario or not nombre_usuario or not apellido_usuario or not email_usuario or not telefono_usuario or not clave_usuario:
                            print('¡Error! Campo/s vacío/s no permitido/s. Pruebe nuevamente...')
                            intentos = intentos + 1
                        elif intentos == 8:
                            print('¡Error! Haz alcanzado el límite máximo de intentos... Vuelve a intentarlo más tarde')
                            break
                        else:
                            try:

                                if len(dni_usuario) < 7:
                                    while (intentos < 9):
                                        print('¡Error! El DNI debe contener al menos 7 dígitos')
                                        dni_usuario = input('Ingrese nuevamente su DNI:\n')

                                        if len(dni_usuario) < 7:
                                            intentos = intentos + 1
                                        else:
                                            break                               

                                if len(telefono_usuario) < 10 or len(telefono_usuario) > 15:
                                    while (intentos < 9):
                                        print('¡Error! El teléfono debe contener entre 10 y 15 carácteres')
                                        telefono_usuario = input('Ingrese nuevamente su teléfono:\n')

                                        if len(telefono_usuario) < 10 or len(telefono_usuario) > 15:
                                            intentos = intentos + 1
                                        else:
                                            break

                                if len(clave_usuario) < 8:
                                    while (intentos < 9):
                                        print('¡Error! La clave debe contener 8 o más carácteres')
                                        clave_usuario = input('Ingrese nuevamente su clave')

                                        if len(clave_usuario) < 8:
                                            intentos = intentos + 1
                                        else:
                                            break
                                
                                if (intentos < 9):

                                    try:
                                        dni_usuario = int(dni_usuario)
                                        telefono_usuario = int(telefono_usuario)

                                        cliente = Cliente(
                                            dni_cliente= dni_usuario,
                                            nombre=nombre_usuario,
                                            apellido=apellido_usuario,
                                            email=email_usuario,
                                            telefono=telefono_usuario,
                                            clave=clave_usuario,
                                            fecha_registro=datetime.now()
                                        )

                                        diccionario_clientes[cliente.email] = cliente

                                        print(f'¡Éxito! El usuario "{cliente.nombre} {cliente.apellido}" ha sido registrado como cliente correctamente')
                                        break
                                    except ValueError:
                                        print('¡Error! No se ha podido registrar en el sistema. Pruebe nuevamente')
                                else:
                                    print('¡Error! Haz alcanzado el límite máximo de intentos... Vuelve a intentarlo más tarde')
                                    break
                            except ValueError:
                                print('¡Error! No se ha podido registrar en el sistema. Pruebe nuevamente')
                                intentos = intentos + 1
                case 3:
                    print('Saliendo...')
                    break
                case _:
                    print('¡Ops! Parece que haz seleccionado una opción no válida. Pruebe nuevamente...')
        except ValueError:
            print('¡Error! Ingrese un número de opción válido')