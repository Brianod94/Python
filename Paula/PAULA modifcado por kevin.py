from datetime import datetime

# ================== DICCIONARIOS Y VARIABLES GLOBALES ==================
clientes = {}
materias_primas = []
pedidos = []

usuarios = {
    "Administrador": "admin1234",
    "Vendedor": "local1234",
    "Produccion": "produ1234"
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
            print("[2] Gestión de Inventario")
            print("[3] Valores Definitivos (Pedidos)")
            print("[4] Cerrar Sesión")
        elif rol == "vendedor":
            print("[1] Consultar Inventario")
            print("[2] Registrar Pedido")
            print("[3] Registrar Cliente")
            print("[4] Cerrar Sesión")
        elif rol == "produccion":
            print("[1] Consultar pedido")
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
                print("========================= \n")
                print("[1] Registrar nuevo inventario")
                print("[2] Consultar inventario")
            elif opcion == 3:
                listar_pedidos()
            elif opcion == 4:
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
        elif rol == "produccion":
            if opcion == 1:
                consultar_pedidos()
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
            if id_cliente in clientes:
                print("Error: El ID ingresado ya existe.\n")
            else:
                nombre_empresa = input("Nombre de la Empresa: ").title()
                nombre_representante = input("Representante legal: ").title()
                correo = input("Correo: ")
                telefono = input("Teléfono: ")
                fecha = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

                clientes[id_cliente] = {
                    "empresa": nombre_empresa,
                    "representante": nombre_representante,
                    "correo": correo,
                    "telefono": telefono,
                    "ultima_modificacion": fecha
                }
                print(f"Cliente creado exitosamente el {fecha}.\n")

        elif opcion == "2":
            print("\n==== Consultar Clientes ====")
            if not clientes:
                print("No hay clientes registrados.\n")
            else:
                busqueda = input("Ingrese el ID o nombre de la empresa a buscar: ").title()
                encontrados = False
                for cliente_id, cliente in clientes.items():
                    if busqueda in cliente["empresa"] or busqueda in cliente_id:
                        print(f"""| ID: {cliente_id}
| Empresa: {cliente["empresa"]}
| Representante: {cliente["representante"]} 
| Correo: {cliente["correo"]}
| Teléfono: {cliente["telefono"]} 
| Fecha Registro: {cliente["ultima_modificacion"]}\n""")
                        encontrados = True
                if not encontrados:
                    print("No se encontraron clientes con esa búsqueda.\n")

        elif opcion == "3":
            print("\n==== Modificar Cliente ====")
            id_buscar = input("Ingrese el ID del cliente a modificar: ")
            cliente = clientes.get(id_buscar)

            if cliente:
                print(f"\nCliente encontrado: {cliente}")
                print("Deje en blanco para mantener el valor actual.\n")

                nuevo_nombre = input(f"Nuevo nombre de empresa [{cliente['empresa']}]: ").title()
                nuevo_representante = input(f"Nuevo representante legal [{cliente['representante']}]: ").title()
                nuevo_correo = input(f"Nuevo correo [{cliente['correo']}]: ")
                nuevo_telefono = input(f"Nuevo teléfono [{cliente['telefono']}]: ")

                cliente['empresa'] = nuevo_nombre or cliente['empresa']
                cliente['representante'] = nuevo_representante or cliente['representante']
                cliente['correo'] = nuevo_correo or cliente['correo']
                cliente['telefono'] = nuevo_telefono or cliente['telefono']
                cliente['ultima_modificacion'] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

                print("\n✅ Cliente modificado exitosamente.\n")
            else:
                print("❌ Cliente no encontrado.\n")

        elif opcion == "4":
            print("\n==== Borrar Cliente ====")
            id_buscar = input("Ingrese el ID del cliente a borrar: ")
            if id_buscar in clientes:
                print(f"Cliente encontrado: {clientes[id_buscar]}")
                del clientes[id_buscar]
                print("Cliente borrado exitosamente.\n")
            else:
                print("Cliente no encontrado.\n")

        elif opcion == "5":
            print("Saliendo del módulo de clientes...\n")
            break
        else:
            print("Opción inválida.\n")

def gestionar_inventario():
    print("\n=== Gestión de Inventario ===")
    descripcion = input("Descripción del movimiento: ")
    fecha = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    materias_primas.append([descripcion, fecha])
    print(f"Movimiento registrado el {fecha}.\n")

def listar_pedidos():
    print("\n=== Listado de Pedidos ===")
    if not pedidos:
        print("No hay pedidos registrados.\n")
    else:
        for pedido in pedidos:
            print(f"Cliente: {pedido[0]} | Producto: {pedido[1]} | Fecha: {pedido[2]}")
        print()

def registrar_pedido():
    print("\n=== Registro de Pedido ===")
    cliente = input("Nombre del cliente: ").title()
    producto = input("Producto solicitado: ").title()
    fecha = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    pedidos.append([cliente, producto, fecha])
    print(f"Pedido registrado el {fecha}.\n")

def consultar_pedidos():
    print("\n=== Consulta de Pedidos ===")
    if not pedidos:
        print("No hay pedidos para consultar.\n")
    else:
        for pedido in pedidos:
            print(f"Cliente: {pedido[0]} | Producto: {pedido[1]} | Fecha: {pedido[2]}")

def mostrar_inventario():
    print("\n=== Consulta de Inventario ===")
    if not materias_primas:
        print("No hay materias primas registradas.\n")
    else:
        for mp in materias_primas:
            print(f"Materia Prima: {mp[0]} | Fecha Registro: {mp[1]}")

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