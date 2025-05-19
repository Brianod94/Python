user1 = {"EstelaRojas": "admin1234"}
user2 = {"ElbaCoser": "local1234"}
user3 = {"JorgeCamisas": "produ1234"}

def menu_usuario():

    while True:
        print("\n===== INICIO DE SESION =====\n")

        print("     Bienvenido a confectex, para ingresar al sistema \n por favor ingrese el perfil de usuario que le corresponde.")

        print("[1] Administrador")
        print("[2] Vendedor")
        print("[3] Produccion")

        opc = input ("Ingrese la opcion para iniciar sesion: ")
        if opc == "1" :
            autenticar_admin(user1)
        elif opc == "2" :
            autenticar_vendedor()
        elif opc == "3":
            autenticar_produccion()
        else: 
            print(" opcion invalida, intente nuevamente ")
       
def autenticar_admin(user1, max_intentos=3):
    intentos = 0
    while True:
        intentos < max_intentos
        user = input("Ingrese Usuario\n")
        password = input("Contraseña\n")
        if user in user1 and user1[user] == password:
            print("*************************************")
            print(f"-----¡Bienvenido {user.capitalize()}!------")
            print("*************************************")
            return user
        else:
            print("\nUsuario o contraseña incorrectos.\n")
            intentos += 1

    print("Demasiados intentos fallidos. Acceso denegado.\n")
    return None  
def autenticar_vendedor(user2, max_intentos=3):
    intentos = 0
    while intentos < max_intentos:
        user = input("Ingrese Usuario\n")
        password = input("Contraseña\n")
        if user in user2 and user2[user] == password:
            print("*************************************")
            print(f"-----¡Bienvenido {user.capitalize()}!------")
            print("*************************************")
            return user
def autenticar_produccion(user3, max_intentos=3):
    intentos = 0
    while intentos < max_intentos:
        user = input("Ingrese Usuario\n")
        password = input("Contraseña\n")
        if user in user3 and user3[user] == password:
            print("*************************************")
            print(f"-----¡Bienvenido {user.capitalize()}!------")
            print("*************************************")
            return user
def menu_principal(rol):
    while True:
        print("\n===== Menú Principal =====\n")
        rol = user1, user2, user3

        if rol == user1:
            print("[1] Registro de Clientes")
            print("[2] Gestión de Inventario")
            print("[3] Valores Definitivos (Pedidos)")
            print("[4] Cerrar Sesión")
          
            print("=========================")
        elif rol == user2 :
            print("[1] Consultar Inventario")
            print("[2] Registrar Pedido")
            print("[3] Registrar Cliente")
            print("[4] Cerrar Sesión")
        elif rol == user3:
            print("[1] Consultar pedido")
        else:
            print("Rol desconocido. Cerrando sesión.")
            break

        try:
            opcion = int(input("Seleccione una opción: "))
        except ValueError:
            print("Por favor, ingrese un número válido.\n")
            continue

        if rol == user1:
            if opcion == 1:
                registrar_cliente()
            elif opcion == 2:
                Gestion_inventario()
            elif opcion == 3:
                    listar_pedidos()
            elif opcion == 4:
                    print("Cerrando sesión...\n")
            break
            
        else:
            print("Opción inválida.\n")
        
        if rol == user2:
            if opcion == 1:
                Consult_inventario()
            elif opcion == 2:
                registrar_pedido()
            elif opcion == 3:
                registrar_cliente()
                break
            elif opcion == 4:
                print("Cerrando sesión...\n")
        if  rol == user3 :
            if opcion == 1:
                consultar_pedidos()
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
                fecha = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                cliente = [id_cliente, nombre_empresa, nombre_representante, correo, telefono, fecha]
                clientes.append(cliente)
                print(f"Cliente creado exitosamente el {fecha}.\n")

        elif opcion == "2":
            print("\n==== Lista de Clientes ====")
            if len(clientes) == 0:
                print("No hay clientes registrados.\n")
            else:
                for cliente in clientes:
                    print(f""" | ID: {cliente[0]} 
| Empresa: {cliente[1]}
| Representante: {cliente[2]} 
| Correo: {cliente[3]}
| Teléfono: {cliente[4]} 
| Fecha Registro: {cliente[5]}""")
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
                    cliente[5] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
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
def Gestion_inventario():
    while True:
        print("\n=== Registrar inventario ===")
        print("========================= \n" )
                
        print("[1] Registrar nuevo inventario")
        print("[2] eliminar inventario")

        opcion=input('ingrese la opcion de inventario deseada: ')

        if opcion == "1":
            reference_number=int(input("ingrese numero de referencia de la prenda: "))
            for items in inventario:
                if items [0] == inventario:
                    print("Error: el numero de referencia ingresado ya existe.\n")
                    break
            else:
                Nombre_prenda=input("ingrese nombre de la prenda a ingresar: ")
                Colores=input("ingrese los coloress disponibles: ")
                Tallas=input("ingrese las tallas disponibles")
                valor_fabricacion=int(input("ingrese valor de fabricacion: "))
                Precio_venta=int(input("ingrese precio de venta: "))
                fecha = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                items=[reference_number, Nombre_prenda, Colores, Tallas, valor_fabricacion, Precio_venta, fecha]
                inventario.append(items)
                print(f"La prenda fue registrada exitosamente {fecha}.\n")

        elif opcion == 2:
            print("\n==== Eliminar item ====")
            referencenumber=int(input("ingrese el numero dee referencia del item que desea eliminar"))
            for i in range(len(items)):
                if items[i][0] == referencenumber:
                    print(f"item encontrado: {items[i]}")
                    items.pop[i]
                    print("item eliminado de forma exitosa.\n")
                    break
                else:
                    print("item no encontrado.\n")
def Consult_inventario():
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

def listar_pedidos():
    print("\n=== Listado de Pedidos ===")
    if len(pedidos) == 0:
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
    
    print(len(pedidos - 1))
    
def mostrar_inventario():
    print("\n=== Consulta de Inventario ===")
    if len(materias_primas) == 0:
        print("No hay materias primas registradas.\n")
    else:
        for mp in materias_primas:
            print(f"Materia Prima: {mp[0]} | Cantidad: {mp[1]} | Fecha Registro: {mp[2]}")
        print()


def programa():
    while True:
        usuario_autenticado = menu_usuario()
        if usuario_autenticado:
            menu_principal(usuario_autenticado)
        else:
            print("Acceso denegado o máximo de intentos fallidos.")
            break
programa()