from datetime import datetime
import re

#=========================================== Listas de tallas y colores disponibles
tallas_disponibles = ["XS", "S", "M", "L", "XL", "XXL", "XXXL"]
colores_disponibles = ["azul", "caqui", "naranja"]

#=========================================== Usuarios por rol
user1 = {"Brayan orozco": "admin1234"}
user2 = {"Kevin puerta": "local1234"}
user3 = {"Julio martinez": "produ1234"}

# ===========================================Datos principales
clientes = []
inventario = []
pedidos = []
productos = []

# ================== FUNCIONES DE VALIDACIÓN ==================
def validar_correo(correo):
    patron = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    return re.match(patron, correo) is not None

def validar_telefono(telefono):
    return telefono.isdigit() and 7 <= len(telefono) <= 15

def validar_nombre(nombre):
    patron = r'^[A-Za-z\s]+$'
    return re.match(patron, nombre) is not None

# ================== FUNCIONES DE AUTENTICACIÓN DE USUARIOS ==================
def menu_usuario():
    while True:
        print("\n================ INICIO DE SESION =========================")
        print("===============Bienvenido a Confectex======================")
        print("Seleccione su perfil de usuario:")
        print("[1] Administrador")
        print("[2] Vendedor")
        print("[3] Producción")
        print("===========================================================")

        opc = input("Ingrese la opción para iniciar sesión: ")

        if opc == "1":
            usuario = autenticador_usuario(user1, "admin")
            if usuario:
                return ("admin", usuario)
        elif opc == "2":
            usuario = autenticador_usuario(user2, "vendedor")
            if usuario:
                return ("vendedor", usuario)
        elif opc == "3":
            usuario = autenticador_usuario(user3, "produccion")
            if usuario:
                return ("produccion", usuario)
        else:
            print("Opción inválida, intente nuevamente.")

def autenticador_usuario(usuarios_dict, rol, max_intentos=3):
    intentos = 0
    while intentos < max_intentos:
        user = input("Ingrese Usuario: ")
        password = input("Contraseña: ")

        if user in usuarios_dict and usuarios_dict[user] == password:
            print("\n===========================================================")
            print(f"----------------¡Bienvenido {user.capitalize()}!------------------")
            print("===========================================================")
            return user
        else:
            print("\nUsuario o contraseña incorrectos.\n")
            intentos += 1

    print("Demasiados intentos fallidos. Acceso denegado.\n")
    return None

def menu_principal(rol):
    while True:
        print("\n================ MENÚ PRINCIPAL =========================")
        if rol == "admin":
            print("[1] Gestion de Clientes")
            print("[2] Valores Definitivos (Pedidos)")
            print("[3] Cerrar Sesión")
        elif rol == "vendedor":
            print("[1] Consultar productos disponibles")
            print("[2] Gestion de Pedidos")
            print("[3] Gestion de Cliente")
            print("[4] Cerrar Sesión")
        elif rol == "produccion":
            print("[1] Gestión de productos")
            print("[2] Cerrar Sesión")
        else:
            print("Rol desconocido. Cerrando sesión.")
            break

        try:
            opcion = int(input("Seleccione una opción: "))
        except ValueError:
            print("Por favor, ingrese un número válido.\n")
            continue

        if rol == "admin":
            if opcion == 1:
                registrar_cliente_admin()
            elif opcion == 2:
                listar_pedidos()
            elif opcion == 3:
                print("Cerrando sesión...\n")
                break
            else:
                print("Opción inválida.\n")
        elif rol == "vendedor":
            if opcion == 1:
                Consulta_producto_vendedor()
            elif opcion == 2:
                registrar_pedido()
            elif opcion == 3:
                Registrar_cliente_vendedor()
            elif opcion == 4:
                print("Cerrando sesión...\n")
                break
            else:
                print("Opción inválida.\n")
        elif rol == "produccion":
            if opcion == 1:
                Gestion_productos()
            elif opcion == 2:
                print("Cerrando sesión...\n")
                break
            else:
                print("Opción inválida.\n")

# ================================================ MÓDULO CLIENTES ==================
def crear_cliente(clientes):
    print("\n==== Crear Cliente ====")
    id_cliente = input("ID del cliente: ")
    for cliente in clientes:
        if cliente['id'] == id_cliente:
            print("❌ Error: El ID ingresado ya existe.\n")
            return

    while True:
        empresa = input("Nombre de la Empresa: ").title()
        if validar_nombre(empresa):
            break
        print("❌ El nombre de la empresa solo debe contener letras y espacios.")

    while True:
        representante = input("Representante legal: ").title()
        if validar_nombre(representante):
            break
        print("❌ El nombre del representante solo debe contener letras y espacios.")

    while True:
        correo = input("Correo: ").lower()
        if validar_correo(correo):
            break
        print("❌ Correo inválido. Intenta nuevamente.")

    while True:
        telefono = input("Teléfono: ")
        if validar_telefono(telefono):
            break
        print("❌ Teléfono inválido. Solo números, de 7 a 15 dígitos.")

    cliente = {
        "id": id_cliente,
        "empresa": empresa,
        "representante": representante,
        "correo": correo,
        "telefono": telefono,
        "fecha": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }
    clientes.append(cliente)
    print(f"✅ Cliente creado exitosamente el {cliente['fecha']}.\n")

def consultar_cliente(clientes):
    print("\n==== Consultar Clientes ====")
    buscar_cliente = input("Ingrese el ID o nombre de la empresa a buscar: ").strip().lower()
    encontrados = [c for c in clientes if buscar_cliente in c["id"].lower() or buscar_cliente in c["empresa"].lower()]

    if encontrados:
        for cliente in encontrados:
            print(f"""
ID: {cliente['id']}
Empresa: {cliente['empresa']}
Representante: {cliente['representante']}
Correo: {cliente['correo']}
Teléfono: {cliente['telefono']}
Fecha Registro: {cliente['fecha']}""")
    else:
        print("❌ No se encontraron clientes con ese criterio.\n")

def modificar_cliente(clientes):
    print("\n==== Modificar Cliente ====")
    id_buscar = input("Ingrese el ID del cliente a modificar: ")
    cliente = next((c for c in clientes if c["id"] == id_buscar), None)

    if not cliente:
        print("❌ Cliente no encontrado.\n")
        return

    print("Deje en blanco para mantener el valor actual.")

    nuevo_empresa = input(f"Nuevo nombre de empresa [{cliente['empresa']}]: ").title()
    if nuevo_empresa:
        if validar_nombre(nuevo_empresa):
            cliente["empresa"] = nuevo_empresa
        else:
            print("❌ Nombre de la empresa inválido. Se mantiene el valor anterior.")

    nuevo_representante = input(f"Nuevo representante legal [{cliente['representante']}]: ").title()
    if nuevo_representante:
        if validar_nombre(nuevo_representante):
            cliente["representante"] = nuevo_representante
        else:
            print("❌ Nombre del representante inválido. Se mantiene el valor anterior.")

    nuevo_correo = input(f"Nuevo correo [{cliente['correo']}]: ").lower()
    if nuevo_correo:
        if validar_correo(nuevo_correo):
            cliente["correo"] = nuevo_correo
        else:
            print("❌ Correo inválido. Se mantuvo el anterior.")

    nuevo_telefono = input(f"Nuevo teléfono [{cliente['telefono']}]: ")
    if nuevo_telefono:
        if validar_telefono(nuevo_telefono):
            cliente["telefono"] = nuevo_telefono
        else:
            print("❌ Teléfono inválido. Se mantuvo el anterior.")

    cliente["fecha"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print("✅ Cliente modificado exitosamente.\n")

def eliminar_cliente(clientes):
    print("\n==== Eliminar Cliente ====")
    id_eliminar = input("Ingrese el ID del cliente a eliminar: ")
    cliente = next((c for c in clientes if c["id"] == id_eliminar), None)

    if not cliente:
        print("❌ Cliente no encontrado.\n")
        return

    confirmacion = input(f"¿Estás seguro de eliminar al cliente {cliente['empresa']}? (s/n): ").lower()
    if confirmacion == 's':
        clientes.remove(cliente)
        print("✅ Cliente eliminado exitosamente.\n")
    else:
        print("❌ Operación cancelada.\n")






if encontrados:
        print(f"\n✅ Se encontraron {len(encontrados)} producto(s):\n")
        for p in encontrados:
            print("="*40)
            print(f"ID: {p['id']}")
            print(f"Nombre: {p['nombre']}")
            print(f"Descripción: {p['descripcion']}")
            print(f"Precio: ${p['precio']:.2f}")
            print(f"Fecha Registro: {p['fecha']}")
    else:
        print("❌ No se encontraron productos con ese criterio.\n")
         producto = {
        "id": id_producto,
        "nombre": nombre,
        "descripcion": descripcion,
        "precio": precio,
        "fecha": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }