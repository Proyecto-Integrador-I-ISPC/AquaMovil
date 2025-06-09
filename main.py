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
diccionario_clientes = {

    cliente_uno.email: cliente_uno
}

diccionario_empleados = {

    empleado_uno.email: empleado_uno
}

diccionario_administradores = {

    administrador_uno.email: administrador_uno
}

# Mensaje bienvenida
print('\n¡Bienvenido a AquaMóvil!')

while (True):
    
    print('1. Iniciar Sesión')
    print('2. Registrarse')
    print('3. Salir\n')
    
    respuesta = input('Por favor, seleccione una opción: ')
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

                        usuario = input('Ingrese su usuario (email): ')
                        contraseña = input('Ingrese su contraseña: ')

                        usuario = usuario.replace(" ", "")
                        contraseña = contraseña.replace(" ", "")

                        if not usuario or not contraseña:
                            print('¡Error! Campo/s vacío/s no permitido/s. Pruebe nuevamente...')
                        else: 
                            if usuario in diccionario_clientes:
                                cliente_obj = diccionario_clientes[usuario]
                                if cliente_obj.clave == contraseña:
                                    print('\n¡Ingreso exitoso! Haz iniciado sesión como cliente')
                                    while True:
                                        print('Tus opciones son:')
                                        print('1. Ver datos personales')
                                        print('2. Salir')
                                        respuesta_cliente = input().strip()

                                        if not respuesta_cliente:
                                            print('¡Error! Campo vacío no permitido')
                                            continue

                                        try:
                                            opcion = int(respuesta_cliente)
                                            if opcion == 1:
                                                cliente_obj.mostrar_datos_personales()
                                            elif opcion == 2:
                                                print('Saliendo...')
                                                break
                                            else:
                                                print('¡Ops! Opción no válida. Pruebe nuevamente...')
                                        except ValueError:
                                            print('\n¡Error! Ingrese un número válido')
                                    break
                                else:
                                    print('Contraseña incorrecta. Intente nuevamente.')
                            elif usuario in diccionario_empleados:
                                empleado_obj = diccionario_empleados[usuario]
                                if empleado_obj.clave == contraseña:
                                    print('\n¡Ingreso exitoso! Haz iniciado sesión como empleado')
                                    while True:
                                        print('Tus opciones son:')
                                        print('1. Ver datos personales')
                                        print('2. Salir')
                                        respuesta_empleado = input().strip()

                                        if not respuesta_empleado:
                                            print('¡Error! Campo vacío no permitido')
                                            continue

                                        try:
                                            opcion = int(respuesta_empleado)
                                            if opcion == 1:
                                                empleado_obj.mostrar_datos_personales()
                                            elif opcion == 2:
                                                print('Saliendo...')
                                                break
                                            else:
                                                print('¡Ops! Opción no válida. Pruebe nuevamente...')
                                        except ValueError:
                                            print('\n¡Error! Ingrese un número válido')
                                    break
                                else:
                                    print('Contraseña incorrecta. Intente nuevamente.')
                            elif usuario in diccionario_administradores:
                                administrador_obj = diccionario_administradores[usuario]
                                if administrador_obj.clave == contraseña:
                                    print('\n¡Ingreso exitoso! Haz iniciado sesión como administrador')
                
                                    while (True):
                                        print('\nTus opciones son:')
                                        print('1. Ver datos personales')
                                        print('2. Ver clientes')
                                        print('3. Ver empleados')
                                        print('4. Ver administradores')
                                        print('5. Cambiar un rol')
                                        print('6. Eliminar un usuario')
                                        print('7. Salir\n')
                                        respuesta_administrador = input()
                                        respuesta_administrador = respuesta_administrador.replace(" ", "")

                                        if not respuesta_administrador:
                                            print('¡Error! Campo vacío no permitido')
                                        else:
                                            try:
                                                respuesta_administrador = int(respuesta_administrador)
                                                match respuesta_administrador:
                                                    case 1:
                                                        administrador_obj.mostrar_datos_personales()
                                                    case 2:
                                                        administrador_obj.mostrar_clientes(diccionario_clientes)
                                                    case 3:
                                                        administrador_obj.mostrar_empleados(diccionario_empleados)
                                                    case 4:
                                                        administrador_obj.mostrar_administradores(diccionario_administradores)
                                                    case 5:
                                                        while (True):
                                                            print('\nOpciones Disponibles:')
                                                            print('1. Ingrese el email del usuario que desea cambiar de rol')
                                                            print('2. Salir\n')
                                                            opcion_seleccionada = input()
                                                            opcion_seleccionada = opcion_seleccionada.replace(" ", "")
                                                            if not opcion_seleccionada:
                                                                print('¡Error! Campo vacío no permitido. Pruebe nuevamente...')
                                                            else:
                                                                try:
                                                                    opcion_seleccionada = int(opcion_seleccionada)
                                                                    match opcion_seleccionada:
                                                                        case 1:
                                                                            usuario_a_cambiar = input('\nIngrese el email: ')
                                                                            usuario_a_cambiar = usuario_a_cambiar.replace(" ", "")

                                                                            if not usuario_a_cambiar:
                                                                                print('¡Error! Campo vacío no permitido. Pruebe nuevamente...')
                                                                            else:
                                                                                if usuario_a_cambiar in diccionario_clientes.keys():
                                                                                    print(f'\nEl usuario con correo "{usuario_a_cambiar}" es un cliente')
                                                                                    print('¿Qué rol desea asignarle?')
                                                                                    while(True):
                                                                                        print('1. Empleado') 
                                                                                        print('2. Administrador')
                                                                                        print('3. Salir\n')
                                                                                        opcion_rol = input()
                                                                                        opcion_rol = opcion_rol.replace(" ", "")

                                                                                        if not opcion_rol:
                                                                                            print('¡Error! Campo vacío no permitido. Pruebe nuevamente...')
                                                                                        else:
                                                                                            try:
                                                                                                opcion_rol = int(opcion_rol)
                                                                                                match opcion_rol:
                                                                                                    case 1:
                                                                                                        administrador_obj.cambiar_rol_empleado(diccionario_clientes, diccionario_empleados, diccionario_administradores, usuario_a_cambiar)
                                                                                                        break
                                                                                                    case 2:
                                                                                                        administrador_obj.cambiar_rol_administrador(diccionario_clientes, diccionario_empleados, diccionario_administradores, usuario_a_cambiar)
                                                                                                        break
                                                                                                    case 3:
                                                                                                        print('Saliendo...')
                                                                                                        break
                                                                                                    case _:
                                                                                                        print('¡Ops! Parece que haz seleccionado una opción no válida. Pruebe nuevamente...')
                                                                                            except ValueError:
                                                                                                print('¡Error! Ingrese un número de opción válida')
                                                                                elif usuario_a_cambiar in diccionario_empleados.keys():
                                                                                    print(f'\nEl usuario con correo "{usuario_a_cambiar}" es un empleado')
                                                                                    print('¿Qué rol desea asignarle?')
                                                                                    while(True):
                                                                                        print('1. Cliente') 
                                                                                        print('2. Administrador')
                                                                                        print('3. Salir\n')
                                                                                        opcion_rol = input()
                                                                                        opcion_rol = opcion_rol.replace(" ", "")

                                                                                        if not opcion_rol:
                                                                                            print('¡Error! Campo vacío no permitido. Pruebe nuevamente...')
                                                                                        else:
                                                                                            try:
                                                                                                opcion_rol = int(opcion_rol)
                                                                                                match opcion_rol:
                                                                                                    case 1:
                                                                                                        administrador_obj.cambiar_rol_cliente(diccionario_clientes, diccionario_empleados, diccionario_administradores, usuario_a_cambiar)
                                                                                                        break
                                                                                                    case 2:
                                                                                                        administrador_obj.cambiar_rol_administrador(diccionario_clientes, diccionario_empleados, diccionario_administradores, usuario_a_cambiar)
                                                                                                        break
                                                                                                    case 3:
                                                                                                        print('Saliendo...')
                                                                                                        break
                                                                                                    case _:
                                                                                                        print('¡Ops! Parece que haz seleccionado una opción no válida. Pruebe nuevamente...')
                                                                                            except ValueError:
                                                                                                print('¡Error! Ingrese un número de opción válida')
                                                                                elif usuario_a_cambiar in diccionario_administradores.keys():
                                                                                    print(f'\nEl usuario con correo "{usuario_a_cambiar}" es un administrador')
                                                                                    print('¿Qué rol desea asignarle?')
                                                                                    while(True):
                                                                                        print('1. Cliente') 
                                                                                        print('2. Empleado')
                                                                                        print('3. Salir\n')
                                                                                        opcion_rol = input()
                                                                                        opcion_rol = opcion_rol.replace(" ", "")

                                                                                        if not opcion_rol:
                                                                                            print('¡Error! Campo vacío no permitido. Pruebe nuevamente...')
                                                                                        else:
                                                                                            try:
                                                                                                opcion_rol = int(opcion_rol)
                                                                                                match opcion_rol:
                                                                                                    case 1:
                                                                                                        administrador_obj.cambiar_rol_cliente(diccionario_clientes, diccionario_empleados, diccionario_administradores, usuario_a_cambiar)
                                                                                                        break
                                                                                                    case 2:
                                                                                                        administrador_obj.cambiar_rol_empleado(diccionario_clientes, diccionario_empleados, diccionario_administradores, usuario_a_cambiar)
                                                                                                        break
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
                                                                            print('\nSaliendo...')
                                                                            break
                                                                        case _:
                                                                            print('¡Ops! Parece que haz seleccionado una opción no válida. Pruebe nuevamente...')
                                                                except ValueError:
                                                                    print('\n¡Error! Ingrese un número de opción válida') 
                                                    case 6:
                                                        while (True):
                                                            print('\nOpciones Disponibles:')
                                                            print('1. Ingrese el email del usuario que desea eliminar')
                                                            print('2. Salir\n')
                                                            opcion_seleccionada = input()
                                                            opcion_seleccionada = opcion_seleccionada.replace(" ", "")
                                                            if not opcion_seleccionada:
                                                                print('¡Error! Campo vacío no permitido. Pruebe nuevamente...') 
                                                            else:
                                                                try:
                                                                    opcion_seleccionada = int(opcion_seleccionada)
                                                                    match opcion_seleccionada:
                                                                        case 1:
                                                                            usuario_a_eliminar = input('\nIngrese el email: ')
                                                                            usuario_a_eliminar = usuario_a_eliminar.replace(" ", "")

                                                                            if not usuario_a_eliminar:
                                                                                print('¡Error! Campo vacío no permitido. Pruebe nuevamente...')
                                                                            else:
                                                                                if usuario_a_eliminar in diccionario_clientes.keys():
                                                                                    administrador_obj.eliminar_cliente(diccionario_clientes, administrador_obj, usuario_a_eliminar)
                                                                                    break
                                                                                elif usuario_a_eliminar in diccionario_empleados.keys():
                                                                                    administrador_obj.eliminar_empleado(diccionario_empleados, usuario_a_eliminar)
                                                                                    break
                                                                                elif usuario_a_eliminar in diccionario_administradores.keys() and usuario_a_eliminar != administrador_uno:
                                                                                    administrador_obj.eliminar_administrador(diccionario_administradores, administrador_obj, usuario_a_eliminar)
                                                                                    break
                                                                                else:
                                                                                    print('¡Error! El usuario que deseas eliminar no existe')
                                                                        case 2:
                                                                            print('Saliendo...')
                                                                            break
                                                                        case _:
                                                                            print('¡Ops! Parece que haz seleccionado una opción no válida. Pruebe nuevamente...')
                                                                except ValueError:
                                                                    print('\n¡Error! Ingrese un número de opción válida')
                                                    case 7:
                                                        print('\nSaliendo...')
                                                        break
                                                    case _:
                                                        print('¡Ops! Parece que haz seleccionado una opción no válida. Pruebe nuevamente...')
                                            except ValueError:
                                                print('\n¡Error! Ingrese un número de opción válida')
                                    break
                                else:
                                    print('\nNo existe ningún usuario registrado con ese usuario y contraseña.')
                            else:
                                if intentos < 3:
                                    print('\nNo se ha encontrado ninguna cuenta asociada a esos datos')
                                    intentos = intentos + 1
                                else:
                                    print('\n¡Error! Vuelve a intentarlo más tarde...')
                                    break
                case 2:
                    intentos = 0
                    max_intentos = 9

                    while intentos < max_intentos:
                        print('\nComplete el siguiente formulario para registrarse en el sistema:')

                        dni_usuario = input('DNI (sin guiones ni puntos): ').replace(" ", "")
                        nombre_usuario = input('Nombre: ').replace(" ", "")
                        apellido_usuario = input('Apellido: ').replace(" ", "")
                        email_usuario = input('Email: ').replace(" ", "")
                        telefono_usuario = input('Teléfono (sin símbolos ni espacios): ').replace(" ", "")
                        clave_usuario = input('Genere una clave: ').replace(" ", "")

                        if not all([dni_usuario, nombre_usuario, apellido_usuario, email_usuario, telefono_usuario, clave_usuario]):
                            print('¡Error! Campo/s vacío/s no permitido/s. Pruebe nuevamente...')
                            intentos += 1
                            continue

                        if len(dni_usuario) < 7:
                            print('¡Error! El DNI debe contener al menos 7 dígitos.')
                            intentos += 1
                            continue

                        if len(telefono_usuario) < 10 or len(telefono_usuario) > 15:
                            print('¡Error! El teléfono debe contener entre 10 y 15 caracteres.')
                            intentos += 1
                            continue

                        if len(clave_usuario) < 8:
                            print('¡Error! La clave debe contener 8 o más caracteres.')
                            intentos += 1
                            continue

                        try:
                            dni_usuario = int(dni_usuario)
                            telefono_usuario = int(telefono_usuario)

                            cliente = Cliente(
                                dni_cliente=dni_usuario,
                                nombre=nombre_usuario,
                                apellido=apellido_usuario,
                                email=email_usuario,
                                telefono=telefono_usuario,
                                clave=clave_usuario,
                                fecha_registro=datetime.now()
                            )

                            diccionario_clientes[cliente.email] = cliente
                            print(f'\n¡Éxito! El usuario "{cliente.nombre} {cliente.apellido}" ha sido registrado correctamente.')
                            break

                        except ValueError:
                            print('¡Error! DNI y teléfono deben contener solo números.')
                            intentos += 1

                        if intentos >= max_intentos:
                            print('\n¡Error! Has alcanzado el límite máximo de intentos. Vuelve a intentarlo más tarde.')
                            break
                case 3:
                    print('\nSaliendo del sistema... ¡Hasta luego!\n')
                    break
                case _:
                    print('¡Ops! Opción no válida. Pruebe nuevamente...')
        except ValueError:
            print('¡Error! Ingrese un número válido')