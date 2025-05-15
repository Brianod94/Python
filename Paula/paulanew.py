import re
from datetime import datetime

# ================== LISTAS Y VARIABLES GLOBALES ==================
clientes = []
materias_primas = []
pedidos = []
usuarios = {
    "Administrador": "admin1234",
    "Vendedor": "local1234",
    "Produccion": "produ1234"
}

# ================== FUNCIONES DE VALIDACIÓN ==================
def validar_correo(correo):
    # Patrón para validar correos comunes (usuario@dominio.ext)
    patron = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    return re.match(patron, correo) is not None

def validar_telefono(telefono):
    # Valida que solo contenga dígitos y que la longitud esté entre 7 y 15
    return telefono.isdigit() and 7 <= len(telefono) <= 15

def validar_nombre(nombre):
    # Permite solo letras (mayúsculas y minúsculas) y espacios.
    # No se permiten dígitos ni símbolos adicionales.
    patron = r'^[A-Za-z\s]+$'
    return re.match(patron, nombre) is not None

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
        print("\n=== Menú de Clientes ===")
        print("[1] Crear cliente")
        print("[2] Consultar clientes")
        print("[3] Modificar cliente")
        print("[4] Borrar cliente")
        print("[5] Salir")

        opcion = input("Seleccione una opción: ")

        ## ================== validaciones registro de clientes  ==================

        if opcion == "1":
            print("\n==== Crear Cliente ====")
            id_cliente = input("ID del cliente: ")
            if any(c['id'] == id_cliente for c in clientes):
                print("Error: El ID ingresado ya existe.\n")
            else:
                #====================== Validación del nombre de la empresa ========================
                while True:
                    empresa = input("Nombre de la Empresa: ").title()
                    if validar_nombre(empresa):
                        break
                    print("❌ El nombre de la empresa solo debe contener letras y espacios.")

                    #====================== Validación del representante lega l======================
                while True:
                    representante = input("Representante legal: ").title()
                    if validar_nombre(representante):
                        break
                    print("❌ El nombre del representante solo debe contener letras y espacios.")

                # ====================== Validación de correo ======================
                while True:
                    correo = input("Correo: ").lower()
                    if validar_correo(correo):
                        break
                    print("❌ Correo inválido. Intenta nuevamente.")

                # ====================== Validación de teléfono ======================
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

        elif opcion == "2":
            print("\n==== Consultar Clientes ====")
            buscar_cliente = input("Ingrese el ID o nombre de la empresa a buscar: ").strip().lower()
            encontrados = [c for c in clientes if buscar_cliente in c["id"].lower() or buscar_cliente in c["empresa"].lower()]
            if encontrados:
                for cliente in encontrados:
                    print(f"""\nID: {cliente['id']}
Empresa: {cliente['empresa']}
Representante: {cliente['representante']}
Correo: {cliente['correo']}
Teléfono: {cliente['telefono']}
Fecha Registro: {cliente['fecha']}""")
            else:
                print("No se encontraron clientes con ese criterio.\n")

        elif opcion == "3":
            print("\n==== Modificar Cliente ====")
            id_buscar = input("Ingrese el ID del cliente a modificar: ")
            cliente = next((c for c in clientes if c["id"] == id_buscar), None)
            if cliente:
                print("Deje en blanco para mantener el valor actual.")

                # ======================Validación para la empresa======================
                nuevo_empresa = input(f"Nuevo nombre de empresa [{cliente['empresa']}]: ").title()
                if nuevo_empresa:
                    if validar_nombre(nuevo_empresa):
                        cliente["empresa"] = nuevo_empresa
                    else:
                        print("❌ Nombre de la empresa inválido. Se mantiene el valor anterior.")

                # ======================Validación para el representante======================
                nuevo_representante = input(f"Nuevo representante legal [{cliente['representante']}]: ").title()
                if nuevo_representante:
                    if validar_nombre(nuevo_representante):
                        cliente["representante"] = nuevo_representante
                    else:
                        print("❌ Nombre del representante inválido. Se mantiene el valor anterior.")

                # ======================Validación de correo======================
                nuevo_correo = input(f"Nuevo correo [{cliente['correo']}]: ").lower()
                if nuevo_correo:
                    if validar_correo(nuevo_correo):
                        cliente["correo"] = nuevo_correo
                    else:
                        print("❌ Correo inválido. Se mantuvo el anterior.")

                # ======================Validación de teléfono======================
                nuevo_telefono = input(f"Nuevo teléfono [{cliente['telefono']}]: ")
                if nuevo_telefono:
                    if validar_telefono(nuevo_telefono):
                        cliente["telefono"] = nuevo_telefono
                    else:
                        print("❌ Teléfono inválido. Se mantuvo el anterior.")

                cliente["fecha"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                print("✅ Cliente modificado exitosamente.\n")
            else:
                print("Cliente no encontrado.\n")

        elif opcion == "4":
            print("\n==== Borrar Cliente ====")
            id_buscar = input("Ingrese el ID del cliente a borrar: ")
            for i, c in enumerate(clientes):
                if c["id"] == id_buscar:
                    print(f"Cliente encontrado: {c}")
                    del clientes[i]
                    print("✅ Cliente borrado exitosamente.\n")
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
        usuario_autenticado = autenticar(usuarios)
        if usuario_autenticado:
            menu_principal(usuario_autenticado)
        else:
            break

# ================== EJECUTAR ==================
programa()
