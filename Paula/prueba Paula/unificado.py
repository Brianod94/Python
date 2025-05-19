from datetime import datetime
import re
clientes_registrados = {
    "001": "julio martinez",
    "002": "jesus",
    "003": "santiago"    
}
#aqui creo una lista con las tallas y los colores disponibles
tallas_disponibles = ["XS", "S", "M", "L", "XL", "XXL", "XXXL"]
colores_disponibles = ["azul", "caqui", "naranja"]  


 
user1 = {"EstelaRojas": "admin1234"}
user2 = {"ElbaCoser": "local1234"}
user3 = {"JorgeCamisas": "produ1234"}
clientes = []
inventario = []
pedidos = []    #esta seria la lista para guardar los  pedidos
productos = []
# ================== FUNCIONES DE VALIDACIÓN ==================
def validar_correo(correo): # type: ignore
    # Patrón para validar correos comunes (usuario@dominio.ext)
    patron = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    return re.match(patron, correo) is not None

def validar_telefono(telefono): # type: ignore
    # Valida que solo contenga dígitos y que la longitud esté entre 7 y 15
    return telefono.isdigit() and 7 <= len(telefono) <= 15 # type: ignore

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

def autenticador_usuario(usuarios_dict, rol, max_intentos=3): # type: ignore
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



# ================== FUNCIONES DEL MÓDULO CLIENTES ==================
def registrar_cliente_admin():#============================registro de clientes admin===========================
    while True:
        print("\n=== Menú de Clientes ===")
        print("[1] Crear cliente")
        print("[2] Modificar cliente")
        print("[3] Borrar cliente")
        print("[4] Salir")

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

        elif opcion == "3":
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
            break
        else:
            print("Opción inválida.\n")
            
def Consulta_producto_vendedor():#==========================consulta de productos=====================
    print("\n==== Inventario ====")
    if len(inventario) == 0:
        print("No hay items registrados.\n")
    else:
         for items in inventario:
             print(f""" | Referencia: {inventario[0]} 
| Nombre de la prenda: {inventario[1]}
| Tallas disponibles: {inventario[2]} 
| Colores disponibles: {inventario[3]}
| Valor de fabricacion: {inventario[4]} 
| Precio de venta: {inventario[5]}""")
    print(inventario)
    
def Consultar_productos_disponibles():#=====================productos disponibles ==========================
    pendiente="resolver"
    
def Gestión_productos():#===================================gestion de productos====================
    pendiente="resolver"

def listar_pedidos():       #=======================================================================    
    pendiente="resolver"
def generar_codigo_pedido():        #esta es la funcion de generar codigo en secuencia#============== 
    numero = len(pedidos) + 1
    return f"PED{numero:03d}"    

def registrar_pedido():     #aqui seria la funcion de registrar pedido#=============================
        print("\n****Registrar nuevo pedido****")
        #aqui se validaria el id del cliente
        while True:
            id_cliente = input("Ingrese el ID del cliente: ").strip()
            if id_cliente in clientes_registrados:
                print(f"Cliente reconocido: {clientes_registrados[id_cliente]}")
                break
            else:
                print("ID de cliente no encontrado intente nuevamente.")
        #aqui se valida el tipo de prenda 
        while True:
            print("Seleccione el tipo de prenda:")
            print("1. Inifuga")
            print("2. Dril")
            opcion = input("Ingrese el número de la opción (1 o 2): ").strip()

            if opcion == "1":
                tipo_prenda = "inifuga"
                break
            elif opcion == "2":
                tipo_prenda = "dril"
                break
            else:
                print("Opción no válida. Por favor ingrese 1 o 2.")
            while True:
                print(f"Colores disponibles: {', '.join(colores_disponibles)}")
                color = input("Ingrese el color de la prenda: ").strip().lower()
                if color in colores_disponibles:
                    break
                else:
                    print("Color no permitido intente nuevamente.")
        #aqui estamos utilizando el while para validar las tallas
        while True:
            print(f"Tallas disponibles: {' / '.join(tallas_disponibles)}")
            talla = input("Ingrese la talla: ").strip().upper()
            if talla in tallas_disponibles:
                break
            else:
                print("Talla no disponible intente nuevamente")
        while True:
            try:
                cantidad = int(input("Ingrese la cantidad de prendas: ").strip())
                if cantidad > 0:
                    break
                else:
                    print("La cantidad debe ser un número positivo")
            except ValueError:
                print("Cantidad errónea ingrese un número entero")
        # validar precio unitario
        while True:
            try:
                precio_unitario = float(input("Ingrese el precio unitario de la prenda: ").strip())
                if precio_unitario > 0:
                    break
                else:
                    print("El precio debe ser un número positivo")
            except ValueError:
                print("Valor erróneo ingrese un número decimal")
        # lo que nos hacia falta que era la idea de iva y el resto de totales independientes
        precio_total = cantidad * precio_unitario
        iva = round(precio_total * 0.19, 2)
        total_con_iva = round(precio_total + iva, 2)
        # esta es la opcion que nos crea el consecutivo de pedido
        codigo_pedido = generar_codigo_pedido()
        # en pedido seria dinde estamos creando el pedido
        pedido = {
            "codigo_pedido": codigo_pedido,
            "id_empresa": id_cliente,
            "empresa": clientes_registrados[id_cliente],
            "tipo_prenda": tipo_prenda,
            "color": color,
            "talla": talla,
            "cantidad": cantidad,
            "precio_unitario": precio_unitario,
            "total": round(precio_total, 2),
            "total_con_iva": total_con_iva,
            "iva": iva
        }
        pedidos.append(pedido)
        print("\n===============================")
        print("Datos del pedido:")
        print(f"codigo_pedido: {pedido['codigo_pedido']}")
        print(f"id_empresa: {pedido['id_empresa']}")
        print(f"empresa: {pedido['empresa']}")
        print(f"tipo_prenda: {pedido['tipo_prenda']}")
        print(f"color: {pedido['color']}")
        print(f"talla: {pedido['talla']}")
        print(f"cantidad: {pedido['cantidad']}")
        print(f"precio_unitario: {pedido['precio_unitario']}")
        print(f"Total sin IVA: ${pedido['total']:.2f}")
        print(f"Total con IVA: ${pedido['total_con_iva']:.2f}")
        print(f"Solo IVA (19%): ${pedido['iva']:.2f}")
        print("===============================\n")



# def consultar_pedidos():#=======================================================================
def consultar_pedido_por_codigo():
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