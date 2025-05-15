# ================== LISTAS Y VARIABLES GLOBALES ==================
clientes = []
productos_finales = []

usuarios = {
    "Administrador": "admin1234",
    "Vendedor": "local1234",
}

# ================== FUNCIONES DE AUTENTICACIÓN ==================
def autenticar(usuarios, max_intentos=3):
    intentos = 0
    while intentos < max_intentos:
        user = input("Ingrese Usuario\n")
        password = input("Contraseña\n")

        if user in usuarios and usuarios[user] == password:
            print("*************************************")
            print(f"-----¡Bienvenido {user.capitalize()}!------")
            print("*************************************")
            return user
        else:
            print("\nUsuario o contraseña incorrectos.\n")
            intentos += 1

    print("Demasiados intentos fallidos. Acceso denegado.\n")
    return None

# ================== FUNCIONES DEL MENÚ PRINCIPAL ==================
def menu_principal(rol):
    while True:
        print("\n===== Menú Principal =====\n")
        rol = rol.lower()

        if rol == "administrador":
            print("[1] Registro de Clientes")
            print("[2] Registro de Producto Final")
            print("[3] Gestión de Inventario")
            print("[4] Valores Definitivos (Pedidos)")
            print("[5] Cerrar Sesión")
            print("=========================")
        elif rol == "vendedor":
            print("[1] Consultar Inventario")
            print("[2] Registrar Pedido")
            print("[3] Registrar Cliente")
            print("[4] Cerrar Sesión")
        else:
            print("Rol desconocido. Cerrando sesión.")
            break

        try:
            opcion = int(input("Seleccione una opción: "))
        except ValueError:
            print("Por favor, ingrese un número válido.\n")
            continue

        if rol == "administrador":
            if opcion == 1:
                registrar_cliente()
            elif opcion == 2:
                registrar_producto_final()
            elif opcion == 3:
                gestionar_inventario()
            elif opcion == 4:
                listar_pedidos()
            elif opcion == 5:
                print("Cerrando sesión...\n")
                break
            else:
                print("Opción inválida.\n")
        elif rol == "vendedor":
            if opcion == 1:
                mostrar_inventario()
            elif opcion == 2:
                registrar_pedido()
            elif opcion == 3:
                registrar_cliente()
            elif opcion == 4:
                print("Cerrando sesión...\n")
                break
            else:
                print("Opción inválida.\n")

# ================== FUNCIONES DEL MÓDULO CLIENTES ==================
def registrar_cliente():
    while True:
        print("\n=== Menú de Clientes ===")
        print("[1] Crear cliente")
        print("[2] Consultar clientes")
        print("[3] Modificar cliente")
        print("[4] Borrar cliente")
        print("[5] Salir")
        print("********************************************\n")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            print("\n==== Crear Cliente ====")
            id_cliente = input("ID del cliente: ")
            for cliente in clientes:
                if cliente[0] == id_cliente:
                    print("Error: El ID ingresado ya existe.\n")
                    break
            else:
                nombre_empresa = input("Nombre de la Empresa: ").title()
                nombre_representante = input("Representante legal: ").title()
                correo = input("Correo: ").title()
                telefono = input("Teléfono: ")
                cliente = [id_cliente, nombre_empresa, nombre_representante, correo, telefono]
                clientes.append(cliente)
                print("Cliente creado exitosamente.\n")

        elif opcion == "2":
            print("\n==== Lista de Clientes ====")
            if len(clientes) == 0:
                print("No hay clientes registrados.\n")
            else:
                for cliente in clientes:
                    print(f"ID: {cliente[0]} | Empresa: {cliente[1]} | Representante: {cliente[2]} | Correo: {cliente[3]} | Teléfono: {cliente[4]}")
                print()

        elif opcion == "3":
            print("\n==== Modificar Cliente ====")
            id_buscar = input("Ingrese el ID del cliente a modificar: ")
            for cliente in clientes:
                if cliente[0] == id_buscar:
                    print(f"Cliente encontrado: {cliente}")
                    cliente[1] = input("Nuevo nombre de empresa: ").title()
                    cliente[2] = input("Nuevo representante legal: ").title()
                    cliente[3] = input("Nuevo correo: ").title()
                    cliente[4] = input("Nuevo teléfono: ")
                    print("Cliente modificado exitosamente.\n")
                    break
            else:
                print("Cliente no encontrado.\n")

        elif opcion == "4":
            print("\n==== Borrar Cliente ====")
            id_buscar = input("Ingrese el ID del cliente a borrar: ")
            for i in range(len(clientes)):
                if clientes[i][0] == id_buscar:
                    print(f"Cliente encontrado: {clientes[i]}")
                    clientes.pop(i)
                    print("Cliente borrado exitosamente.\n")
                    break
            else:
                print("Cliente no encontrado.\n")

        elif opcion == "5":
            print("Saliendo del módulo de clientes...\n")
            break
        else:
            print("Opción inválida.\n")

# aqui la actualizacion de productos finales 
def registrar_producto_final():
    while True:
        print('\n=== Menú de Productos Finales ===')
        print('[1] Agregar producto')
        print('[2] Consultar productos')
        print('[3] Salir')
        print('*********************************')

        opcion=input('Seleccione una opción: ')

        if opcion=='1':
            print('\n=== Agregar Producto Final ===')
            id_producto=input('ID del producto:')
            for producto in productos_finales:
                if producto['id']==id_producto:
                    print('Error: El ID ingresado ya existe.\n')
                    break
            else:
                nombre=input('Nombre del producto:').title()
                try:
                    cantidad=float(input('Cantidad disponible:'))
                    unidad=input('Unidad de medida (ej. unidad, paquete):').lower()
                    costo=float(input('Costo por unidad:'))
                except ValueError:
                    print('Error: Por favor ingrese valores numéricos válidos para cantidad y costo.\n')
                    continue

                producto={
                    'id': id_producto,
                    'nombre': nombre,
                    'cantidad': cantidad,
                    'unidad': unidad,
                    'costo': costo
                }
                productos_finales.append(producto)
                print('Producto registrado exitosamente.\n')

        elif opcion=='2':
            print('\n=== Lista de Productos Finales ===')
            if not productos_finales:
                print('No hay productos registrados.\n')
            else:
                for producto in productos_finales:
                    print(f'ID: {producto['id']} | Nombre: {producto['nombre']} |'
                          f'Cantidad: {producto['cantidad']} {producto['unidad']} |'
                          f'Costo/u: ${producto['costo']:.2f}')
                print()

        elif opcion=='3':
            print('Saliendo del menú de productos finales...\n')
            break
        else:
            print('Opción inválida.\n')

# ================== FUNCIONES SIMULADAS (PLANTILLAS) ==================
def gestionar_inventario():
    print("\n=== Gestión de Inventario ===")
    print("Función de gestión de inventario en desarrollo.\n")

def listar_pedidos():
    print("\n=== Listado de Pedidos ===")
    print("Función de listado de pedidos en desarrollo.\n")

def registrar_pedido():
    print("\n=== Registro de Pedido ===")
    print("Función de registro de pedido en desarrollo.\n")

def mostrar_inventario():
    print("\n=== Consulta de Inventario ===")
    print("Función de consulta de inventario en desarrollo.\n")

# ================== FLUJO PRINCIPAL ==================
def programa():
    while True:
        usuario_autenticado = autenticar(usuarios)
        if usuario_autenticado:
            menu_principal(usuario_autenticado)
        else:
            print("Acceso denegado o máximo de intentos fallidos.")
            break

# ================== EJECUTAR PROGRAMA ==================
programa()
