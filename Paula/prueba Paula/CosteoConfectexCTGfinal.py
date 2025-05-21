from datetime import datetime
import re

#aqui creo una lista con las tallas y los colores disponibles
tallas_disponibles = ["XS", "S", "M", "L", "XL", "XXL", "XXXL"]
colores_disponibles = ["azul", "caqui", "naranja"]  


 
user1 = {"Brayan orozco": "admin1234"}
user2 = {"Kevin puerta": "local1234"}
user3 = {"Julio martinez": "produ1234"}
clientes = []
inventario = []
pedidos = []    #esta seria la lista para guardar los  pedidos
productos = []
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
def menu_principal(rol):#=======================================================================
    while True:
        print("\n================ INICIO DE SESION =========================")
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
                Consultar_productos_disponibles()
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
                Gestión_productos()
            elif opcion == 2:
                print("Cerrando sesión...\n")
                break
            else:
                print("Opción inválida.\n")

def crear_cliente(clientes):#=============================crear cliente===================
    print("\n==== Crear Cliente ====")
    id_cliente = input("ID del cliente: ")
    
    if not id_cliente.strip(): #valida que este campo no quede vacio 
        print("❌ El ID del cliente no puede estar vacío.")
        return

    for cliente in clientes:
        if cliente['id'] == id_cliente:
            print("❌ Error: El ID ingresado ya existe.\n")
            return

    # Validar nombre de la empresa
    while True:
        empresa = input("Nombre de la Empresa: ").title()
        if validar_nombre(empresa):
            break
        print("❌ El nombre de la empresa solo debe contener letras y espacios.")

    # Validar representante legal
    while True:
        representante = input("Representante legal: ").title()
        if validar_nombre(representante):
            break
        print("❌ El nombre del representante solo debe contener letras y espacios.")

    # Validar correo
    while True:
        correo = input("Correo: ").lower()
        if validar_correo(correo):
            break
        print("❌ Correo inválido. Intenta nuevamente.")

    # Validar teléfono
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
            print(f"""\nID: {cliente['id']}
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
    for cliente in clientes:
        if cliente["id"] == id_buscar:
            break
        else:
            print("❌ Cliente no encontrado.\n")
            return

# Aquí puedes usar 'cliente' que es el cliente encontrado

    print("Deje en blanco para mantener el valor actual.")

    # Empresa
    nuevo_empresa = input(f"Nuevo nombre de empresa [{cliente['empresa']}]: ").title()
    if nuevo_empresa:
        if validar_nombre(nuevo_empresa):
            cliente["empresa"] = nuevo_empresa
        else:
            print("❌ Nombre de la empresa inválido. Se mantiene el valor anterior.")

    # Representante
    nuevo_representante = input(f"Nuevo representante legal [{cliente['representante']}]: ").title()
    if nuevo_representante:
        if validar_nombre(nuevo_representante):
            cliente["representante"] = nuevo_representante
        else:
            print("❌ Nombre del representante inválido. Se mantiene el valor anterior.")

    # Correo
    nuevo_correo = input(f"Nuevo correo [{cliente['correo']}]: ").lower()
    if nuevo_correo:
        if validar_correo(nuevo_correo):
            cliente["correo"] = nuevo_correo
        else:
            print("❌ Correo inválido. Se mantuvo el anterior.")

    # Teléfono
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

    for cliente in clientes:
        if cliente["id"] == id_eliminar:
            break
    else:
        print("❌ Cliente no encontrado.\n")
        return

    confirmacion = input(f"¿Estás seguro de eliminar al cliente {cliente['empresa']}? (s/n): ").lower()
    if confirmacion == 's':
        clientes.remove(cliente)
        print("✅ Cliente eliminado exitosamente.\n")
    else:
        print("❌ Operación cancelada.\n")

# ================== FUNCIONES DEL MÓDULO CLIENTES ==================
def registrar_cliente_admin():#============================registro de clientes admin===========================
    while True:
        print("\n=== Menú de Clientes ===")
        print("[1] Crear cliente")
        print("[2] Modificar cliente")
        print("[3] Eliminar cliente")
        print("[4] Salir")

        opcion = input("Seleccione una opción: ")

        ## ================== validaciones registro de clientes  ==================

        if opcion == "1":
           crear_cliente(clientes)

        elif opcion == "2":
           modificar_cliente(clientes)

        elif opcion == "3":
            eliminar_cliente(clientes)

        elif opcion == "4":
            break
        else:
            print("Opción inválida.\n")
            
def Registrar_cliente_vendedor():#=========================regisro de clienes vendedor==========================
      while True:
        print("\n=== Menú de Clientes ===")
        print("[1] Crear cliente")
        print("[2] Consultar clientes")
        print("[3] Salir")

        opcion = input("Seleccione una opción: ")

        ## ================== validaciones registro de clientes  ==================

        if opcion == "1":
           crear_cliente(clientes)
        elif opcion == "2":
           consultar_cliente(clientes)
        elif opcion == "3":
            break
        else:
            print("Opción inválida.\n")
            
def Consulta_producto_vendedor():#==========================consulta de productos=====================
    print("\n==== Inventario ====")
    if len(inventario) == 0:
        print("No hay items registrados.\n")
    else:
         for item in inventario:
            print(f"""Referencia: {item['referencia']}
        Nombre de la prenda: {item['nombre']}
        Tallas disponibles: {item['tallas']}
        Colores disponibles: {item['colores']}
        Valor fabricación: {item['valor_fabricacion']}
        Precio venta: {item['precio_venta']}\n""")

    print(inventario)
    
def Consultar_productos_disponibles():#=====================productos disponibles ==========================
    pendiente="resolver"
    
def Gestión_productos():#===================================gestion de productos====================
    pendiente="resolver"

def generar_codigo_pedido():        #esta es la funcion de generar codigo en secuencia#============== 
    numero = len(pedidos) + 1
    return f"PED{numero:03d}"    

def registrar_pedido():
     while True:     #aqui seria la funcion de registrar pedido#=============================
        print("\n--- GESTIÓN DE PEDIDOS ---")
        print("1. Registrar Pedido")
        print("2. Ver Pedidos")
        print("3. Regresar al menú principal")

        opcion = input("Seleccione una opción: ")
        if opcion == '1':
            crear_pedido()
        elif opcion == '2':
            listar_pedidos()
        elif opcion == '3':
            break
        else:
            print("Opción inválida.")

def crear_pedido():
    print("\n--- REGISTRO DE PEDIDO ---")
    id_cliente = input("ID del cliente: ")

    # Buscar cliente por ID
    cliente = None
    for cliente in clientes:
            if cliente["id"] == id_cliente:
                cliente_en_lista = cliente
                break
    if cliente is None:
           print("❌ Cliente no registrado.")
           return


# Aquí puedes usar 'cliente_en_lista' como el cliente encontrado


    # Mostrar productos disponibles (por ahora solo la lista de productos)
    if not productos:
        print("❌ No hay productos registrados.")
        return

    # Mostrar productos disponibles
    print("\nProductos disponibles:")
    for i, prod in enumerate(productos, 1):
        print(f"{i}. Código: {prod['codigo']}, Nombre: {prod['nombre']}, Precio: ${prod['precio']:.2f}")

    codigo_producto = input("Código del producto: ")
    for producto_individual in lista_productos:
        if producto_individual["codigo"] == codigo_producto_buscado:
            # Aquí haces lo que necesites con el producto encontrado
            # por ejemplo, retornar o procesar
            return producto_individual  # o lo que quieras hacer
    print("❌ Producto no encontrado.")
    return


    try:
        cantidad = int(input("Cantidad: "))
        if cantidad <= 0:
            print("❌ La cantidad debe ser mayor que cero.")
            return
    except ValueError:
        print("❌ Cantidad inválida.")
        return

    precio_unitario = producto["precio"]
    total = cantidad * precio_unitario
    iva = total * 0.19
    total_con_iva = total + iva

    pedido = {
        "codigo_pedido": generar_codigo_pedido(),
        "id_empresa": cliente["id"],
        "empresa": cliente["empresa"],
        "tipo_prenda": producto["nombre"],
        "color": producto.get("color", "No especificado"),
        "talla": producto.get("talla", "No especificado"),
        "cantidad": cantidad,
        "precio_unitario": precio_unitario,
        "total": total,
        "iva": iva,
        "total_con_iva": total_con_iva
    }

    pedidos.append(pedido)
    print(f"\n✅ Pedido registrado con éxito. Código: {pedido['codigo_pedido']}\n")

    

def listar_pedidos():
    for i, pedido in enumerate(pedidos, 1):
        print(f"{i}. Cliente: {pedido['empresa']}, Producto: {pedido['tipo_prenda']}, Cantidad: {pedido['cantidad']}, Total: ${pedido['total']:.2f}")


def consultar_pedido_por_codigo():#====================consultar pedido===============
    if not pedidos:
        print("\n🚫 No hay pedidos registrados aún.\n")
        return

    codigo = input("🔎 Ingrese el código del pedido que desea consultar: ").strip()

    encontrado = False
    for pedido in pedidos:
        if pedido["codigo_pedido"] == codigo:
            print("\n✅ Pedido encontrado:")
            print(f"Código de pedido : {pedido['codigo_pedido']}")
            print(f"ID de empresa    : {pedido['id_empresa']}")
            print(f"Empresa          : {pedido['empresa']}")
            print(f"Tipo de prenda   : {pedido['tipo_prenda']}")
            print(f"Color            : {pedido['color']}")
            print(f"Talla            : {pedido['talla']}")
            print(f"Cantidad         : {pedido['cantidad']}")
            print(f"Precio unitario  : ${pedido['precio_unitario']:.2f}")
            print(f"Total sin IVA    : ${pedido['total']:.2f}")
            print(f"IVA (19%)        : ${pedido['iva']:.2f}")
            print(f"Total con IVA    : ${pedido['total_con_iva']:.2f}")
            print("-------------------------------\n")
            encontrado = True
            break

    if not encontrado:
        print("\n❌ No se encontró un pedido con ese código. Verifica e intenta nuevamente.\n")

   
    
def mostrar_inventario():#=======================================================================
    pendiente="resolver"



def programa():#=======================================================================
    while True:
        resultado = menu_usuario()
        if resultado:
            rol, usuario = resultado
            menu_principal(rol)
        else:
            print("Acceso denegado o máximo de intentos fallidos.")
            break

programa()#=======================================================================