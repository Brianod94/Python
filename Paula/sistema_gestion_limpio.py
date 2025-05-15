
from datetime import datetime
import re
import os

# ================== LIMPIAR PANTALLA ==================
def limpiar_pantalla():
    os.system('cls' if os.name == 'nt' else 'clear')

# ================== LISTAS Y VARIABLES GLOBALES ==================
clientes = []
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
        limpiar_pantalla()
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
            print("[2] Cerrar Sesión")
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
                print("[1] Registrar nuevo inventario")
                print("[2] Consultar inventario")
            elif opcion == 3:
                listar_pedidos()
            elif opcion == 4:
                print("Cerrando sesión...\n")
                break
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
        elif rol == "produccion":
            if opcion == 1:
                consultar_pedidos()
            elif opcion == 2:
                print("Cerrando sesión...\n")
                break

# ================== FUNCIONES DEL MÓDULO CLIENTES ==================
def registrar_cliente():
    while True:
        limpiar_pantalla()
        print("\n=== Menú de Clientes ===")
        print("[1] Crear cliente")
        print("[2] Consultar clientes")
        print("[3] Modificar cliente")
        print("[4] Borrar cliente")
        print("[5] Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            print("\n==== Crear Cliente ====")
            id_cliente = input("ID del cliente: ")
            if any(c['id'] == id_cliente for c in clientes):
                print("Error: El ID ingresado ya existe.\n")
            else:
                cliente = {
                    "id": id_cliente,
                    "empresa": input("Nombre de la Empresa: ").title(),
                    "representante": input("Representante legal: ").title(),
                    "correo": input("Correo: ").lower(),
                    "telefono": input("Teléfono: "),
                    "fecha": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                }
                clientes.append(cliente)
                print(f"Cliente creado exitosamente el {cliente['fecha']}.\n")

        elif opcion == "2":
            print("\n==== Consultar Clientes ====")
            buscar_cliente = input("Ingrese el ID o nombre de la empresa a buscar: ").strip().lower()
            encontrados = [c for c in clientes if buscar_cliente in c["id"].lower() or buscar_cliente in c["empresa"].lower()]

            if encontrados:
                for cliente in encontrados:
                    print(f"""\nID: {cliente['id']}\nEmpresa: {cliente['empresa']}\nRepresentante: {cliente['representante']}\nCorreo: {cliente['correo']}\nTeléfono: {cliente['telefono']}\nFecha Registro: {cliente['fecha']}""")
            else:
                print("No se encontraron clientes con ese criterio.\n")

        elif opcion == "3":
            print("\n==== Modificar Cliente ====")
            id_buscar = input("Ingrese el ID del cliente a modificar: ")
            cliente = next((c for c in clientes if c["id"] == id_buscar), None)

            if cliente:
                print("Deje en blanco para mantener el valor actual.")
                cliente["empresa"] = input(f"Nuevo nombre de empresa [{cliente['empresa']}]: ") or cliente["empresa"]
                cliente["representante"] = input(f"Nuevo representante legal [{cliente['representante']}]: ") or cliente["representante"]
                cliente["correo"] = input(f"Nuevo correo [{cliente['correo']}]: ") or cliente["correo"]
                cliente["telefono"] = input(f"Nuevo teléfono [{cliente['telefono']}]: ") or cliente["telefono"]
                cliente["fecha"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                print("Cliente modificado exitosamente.\n")
            else:
                print("Cliente no encontrado.\n")

        elif opcion == "4":
            print("\n==== Borrar Cliente ====")
            id_buscar = input("Ingrese el ID del cliente a borrar: ")
            for i, c in enumerate(clientes):
                if c["id"] == id_buscar:
                    print(f"Cliente encontrado: {c}")
                    del clientes[i]
                    print("Cliente borrado exitosamente.\n")
                    break
            else:
                print("Cliente no encontrado.\n")

        elif opcion == "5":
            break
        else:
            print("Opción inválida.\n")

# ================== FUNCIONES COMPLEMENTARIAS ==================
def mostrar_inventario():
    if not materias_primas:
        print("No hay materias primas registradas.\n")
    else:
        for mp in materias_primas:
            print(f"Materia Prima: {mp[0]} | Cantidad: {mp[1]} | Fecha Registro: {mp[2]}")

def registrar_pedido():
    print("\n=== Registro de Pedido ===")
    cliente = input("Nombre del cliente: ").title()
    producto = input("Producto solicitado: ").title()
    fecha = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    pedidos.append([cliente, producto, fecha])
    print(f"Pedido registrado el {fecha}.\n")

def listar_pedidos():
    if not pedidos:
        print("No hay pedidos registrados.\n")
    else:
        for pedido in pedidos:
            print(f"Cliente: {pedido[0]} | Producto: {pedido[1]} | Fecha: {pedido[2]}")

def consultar_pedidos():
    if not pedidos:
        print("No hay pedidos para producción.\n")
    else:
        for pedido in pedidos:
            print(f"Pedido para {pedido[0]}: {pedido[1]} registrado el {pedido[2]}")

# ================== FLUJO PRINCIPAL ==================
def programa():
    while True:
        limpiar_pantalla()
        usuario_autenticado = autenticar(usuarios)
        if usuario_autenticado:
            menu_principal(usuario_autenticado)
        else:
            break

# ================== EJECUTAR ==================
programa()
