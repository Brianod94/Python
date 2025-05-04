def autenticar(usuario, clave, usuarios):
    """
    Verifica las credenciales del usuario y retorna su rol si son válidas.
    """
    for u in usuarios:
        if u['usuario'] == usuario and u['clave'] == clave:
            return u['rol']
    return None


def tiene_permiso(rol, operacion):
    """
    Determina si un rol tiene permiso para ejecutar la operación solicitada.
    """
    if rol == 'ADMINISTRADOR':
        return True
    if rol == 'VENDEDOR':
        return operacion in ('CREAR', 'CONSULTAR')
    return False


def encontrar_cliente(lista, id_buscar):
    """
    Busca un cliente por su ID en la lista y lo retorna, o None si no existe.
    """
    return next((c for c in lista if c['id'] == id_buscar), None)


def main():
    usuarios = [
        {'usuario': 'admin', 'clave': '1234', 'rol': 'ADMINISTRADOR'},
        {'usuario': 'vendedor', 'clave': 'abcd', 'rol': 'VENDEDOR'}
    ]
    lista_clientes = []

    # Autenticación
    rol_actual = None
    while rol_actual is None:
        usuario = input("Usuario: ").strip()
        clave = input("Clave: ").strip()
        rol_actual = autenticar(usuario, clave, usuarios)
        if rol_actual is None:
            print("Usuario o clave incorrectos. Intente de nuevo.\n")

    print(f"\n¡Bienvenido! Rol asignado: {rol_actual}\n")

    # Menú principal
    opciones = {
        '1': 'CREAR',
        '2': 'CONSULTAR',
        '3': 'MODIFICAR',
        '4': 'ELIMINAR',
        '5': 'SALIR'
    }

    while True:
        print("Menú de opciones:")
        print("1. Crear cliente")
        print("2. Consultar cliente")
        print("3. Modificar cliente")
        print("4. Eliminar cliente")
        print("5. Salir")
        opcion = input("Seleccione una opción (1-5): ").strip()

        operacion = opciones.get(opcion, 'DESCONOCIDA')

        # Verificar permisos
        if operacion != 'SALIR' and not tiene_permiso(rol_actual, operacion):
            print("No tiene permisos para realizar esta operación.\n")
            continue

        # Ejecutar operación
        if opcion == '1':  # CREAR
            id_cliente = input("ID cliente: ").strip()
            nombre = input("Nombre: ").strip()
            correo = input("Correo: ").strip()
            telefono = input("Teléfono: ").strip()
            cliente = {
                'id': id_cliente,
                'nombre': nombre,
                'correo': correo,
                'telefono': telefono
            }
            lista_clientes.append(cliente)
            print("Cliente creado exitosamente.\n")

        elif opcion == '2':  # CONSULTAR
            id_buscar = input("ID del cliente a consultar: ").strip()
            cliente = encontrar_cliente(lista_clientes, id_buscar)
            if cliente:
                print("Datos del cliente:")
                for k, v in cliente.items():
                    print(f"  {k}: {v}")
                print()
            else:
                print("Cliente no encontrado.\n")

        elif opcion == '3':  # MODIFICAR
            id_buscar = input("ID del cliente a modificar: ").strip()
            cliente = encontrar_cliente(lista_clientes, id_buscar)
            if cliente:
                print("Ingrese nuevos datos (enter para conservar actual):")
                nuevo_nombre = input(f"Nombre ({cliente['nombre']}): ").strip() or cliente['nombre']
                nuevo_correo = input(f"Correo ({cliente['correo']}): ").strip() or cliente['correo']
                nuevo_telefono = input(f"Teléfono ({cliente['telefono']}): ").strip() or cliente['telefono']
                cliente.update({
                    'nombre': nuevo_nombre,
                    'correo': nuevo_correo,
                    'telefono': nuevo_telefono
                })
                print("Cliente modificado exitosamente.\n")
            else:
                print("Cliente no encontrado.\n")

        elif opcion == '4':  # ELIMINAR
            id_buscar = input("ID del cliente a eliminar: ").strip()
            cliente = encontrar_cliente(lista_clientes, id_buscar)
            if cliente:
                lista_clientes.remove(cliente)
                print("Cliente eliminado exitosamente.\n")
            else:
                print("Cliente no encontrado.\n")

        elif opcion == '5':  # SALIR
            print("Saliendo del programa...")
            break

        else:
            print("Opción inválida, por favor seleccione un número del 1 al 5.\n")

if __name__ == '__main__':
    main()
