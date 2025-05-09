# === VARIABLES GLOBALES ===
clientes = []
materia_prima = []
inventario = []
pedidos = []

# === FUNCIONES DE UTILIDADES ===
def input_numero(mensaje):
    while True:
        try:
            return int(input(mensaje))
        except ValueError:
            print("\u26a0\ufe0f Error: Ingrese un n\u00famero v\u00e1lido.")

def input_telefono(mensaje):
    while True:
        telefono = input(mensaje)
        if telefono.isdigit():
            return telefono
        else:
            print("\u26a0\ufe0f Error: El tel\u00e9fono debe contener solo n\u00fameros.")

# === FUNCIONES DE CLIENTES ===
def registrar_cliente():
    print("\n=== Registrar Cliente ===")
    id_cliente = input("ID del cliente: ")
    for cliente in clientes:
        if cliente['id'] == id_cliente:
            print("\u26a0\ufe0f Error: ID ya existe.")
            return
    nombre_empresa = input("Nombre de la Empresa: ").title()
    representante = input("Representante Legal: ").title()
    correo = input("Correo: ")
    telefono = input_telefono("Tel\u00e9fono: ")
    clientes.append({
        'id': id_cliente,
        'empresa': nombre_empresa,
        'representante': representante,
        'correo': correo,
        'telefono': telefono
    })
    print("\u2705 Cliente registrado exitosamente.")

def listar_clientes():
    print("\n=== Lista de Clientes ===")
    if not clientes:
        print("No hay clientes registrados.")
    for c in clientes:
        print(f"ID: {c['id']} | Empresa: {c['empresa']} | Representante: {c['representante']} | Correo: {c['correo']} | Tel\u00e9fono: {c['telefono']}")

# === FUNCIONES DE MATERIA PRIMA ===
def registrar_materia_prima():
    print("\n=== Registrar Materia Prima ===")
    id_producto = input("ID del producto: ")
    for producto in materia_prima:
        if producto['id'] == id_producto:
            print("\u26a0\ufe0f Error: ID de producto ya existe.")
            return
    nombre = input("Nombre del Producto: ").title()
    unidad = input("Unidad de Medida (m, kg, unidades): ")
    materia_prima.append({
        'id': id_producto,
        'nombre': nombre,
        'unidad': unidad
    })
    inventario.append({
        'id': id_producto,
        'nombre': nombre,
        'cantidad': 0
    })
    print("\u2705 Producto registrado exitosamente.")

def listar_materia_prima():
    print("\n=== Lista de Materia Prima ===")
    if not materia_prima:
        print("No hay materia prima registrada.")
    for p in materia_prima:
        print(f"ID: {p['id']} | Nombre: {p['nombre']} | Unidad: {p['unidad']}")

# === FUNCIONES DE INVENTARIO ===
def gestionar_inventario():
    print("\n=== Gestionar Inventario ===")
    id_buscar = input("Ingrese ID del producto: ")
    for item in inventario:
        if item['id'] == id_buscar:
            print(f"Producto: {item['nombre']} | Cantidad actual: {item['cantidad']}")
            cantidad = input_numero("Cantidad a agregar (usar negativo para restar): ")
            item['cantidad'] += cantidad
            print("\u2705 Inventario actualizado.")
            return
    print("\u26a0\ufe0f Producto no encontrado en inventario.")

def mostrar_inventario():
    print("\n=== Inventario Actual ===")
    if not inventario:
        print("No hay productos en inventario.")
    for item in inventario:
        print(f"ID: {item['id']} | Producto: {item['nombre']} | Cantidad: {item['cantidad']}")

# === FUNCIONES DE PEDIDOS ===
def registrar_pedido():
    print("\n=== Registrar Pedido ===")
    cliente_id = input("ID del cliente: ")
    for cliente in clientes:
        if cliente['id'] == cliente_id:
            break
    else:
        print("\u26a0\ufe0f Cliente no encontrado.")
        return

    pedido = {'cliente_id': cliente_id, 'productos': []}
    while True:
        mostrar_inventario()
        id_producto = input("ID del producto a pedir (o 'fin' para terminar): ")
        if id_producto.lower() == 'fin':
            break
        for item in inventario:
            if item['id'] == id_producto:
                cantidad = input_numero("Cantidad solicitada: ")
                if cantidad <= item['cantidad']:
                    item['cantidad'] -= cantidad
                    pedido['productos'].append({'id': id_producto, 'nombre': item['nombre'], 'cantidad': cantidad})
                    print("Producto agregado al pedido.")
                else:
                    print("\u26a0\ufe0f No hay suficiente stock.")
                break
        else:
            print("\u26a0\ufe0f Producto no encontrado.")
    pedidos.append(pedido)
    print("\u2705 Pedido registrado exitosamente.")

def listar_pedidos():
    print("\n=== Pedidos Registrados ===")
    if not pedidos:
        print("No hay pedidos registrados.")
    for p in pedidos:
        print(f"Cliente ID: {p['cliente_id']}")
        for prod in p['productos']:
            print(f"- {prod['nombre']} | Cantidad: {prod['cantidad']}")

# === LOGIN Y MENUS ===
def login():
    usuarios = {
        "administrador": "admin123",
        "vendedor": "vend123"
    }
    print("\n======= Ingreso al Sistema =======")
    print("[0] Salir del sistema")
    user = input("Ingrese usuario (o 0 para salir): ").lower()

    if user == "0":
        return "salir"

    password = input("Ingrese contrase\u00f1a: ")

    if user in usuarios and usuarios[user] == password: #verifica si user esta dentro del diccionario usuarios
        print(f"\nBienvenido {user.capitalize()}!\n")
        return user
    else:
        print("\nUsuario o contrase\u00f1a incorrectos.\n")
        return None

def menu_principal(rol):
    while True:
        print("\n===== Men\u00fa Principal =====")
        if rol == "administrador":
            print("[1] Registro de Clientes")
            print("[2] Registro de Materia Prima")
            print("[3] Gesti\u00f3n de Inventario")
            print("[4] Valores Definitivos (Pedidos)")
            print("[5] Cerrar Sesi\u00f3n")
        elif rol == "vendedor":
            print("[1] Consultar Inventario")
            print("[2] Registrar Pedido")
            print("[3] Registrar Cliente")
            print("[4] Cerrar Sesi\u00f3n")

        opcion = input_numero("Seleccione una opci\u00f3n: ")

        if rol == "administrador":
            if opcion == 1:
                registrar_cliente()
                listar_clientes()
            elif opcion == 2:
                registrar_materia_prima()
                listar_materia_prima()
            elif opcion == 3:
                gestionar_inventario()
            elif opcion == 4:
                listar_pedidos()
            elif opcion == 5:
                print("Cerrando sesi\u00f3n...")
                break
            else:
                print("Opci\u00f3n inv\u00e1lida.")

        elif rol == "vendedor":
            if opcion == 1:
                mostrar_inventario()
            elif opcion == 2:
                registrar_pedido()
            elif opcion == 3:
                registrar_cliente()
            elif opcion == 4:
                print("Cerrando sesi\u00f3n...")
                break
            else:
                print("Opci\u00f3n inv\u00e1lida.")

# === MAIN ===
def main():
    while True:
        rol = login()

        if rol == "salir":
            print("\nGracias por usar el sistema. \u2728 Hasta luego!")
            break

        if rol:
            menu_principal(rol)

# Ejecutamos el programa
if __name__ == "__main__":
    main()
