from datatime import datatime 
import re
# diccionarios para usuarios 
user1 = {"Brayan orozco": "admin1234"}
user2 = {"Kevin puerta": "local1234"}
user3 = {"Julio martinez": "produ1234"}
#listas para almacenar la informacion
clientes = []
inventario = []
pedidos = []    
productos = []
#aqui creo una lista con las tallas y los colores disponibles
tallas_disponibles = ["XS", "S", "M", "L", "XL", "XXL", "XXXL"]
colores_disponibles = ["azul", "caqui", "naranja"]  

#============funciones para validar===========
def validar_correo(correo):
    # Patrón para validar correos comunes (usuario@dominio.ext)
    patron = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    return re.match(patron, correo) is not None

def validar_telefono(telefono):
    # Valida que solo contenga dígitos y que la longitud esté entre 7 y 15
    return telefono.isdigit() and 7 <= len(telefono) <= 15

def validar_nombre(nombre): # No se permiten dígitos ni símbolos adicionales.
    # Permite solo letras (mayúsculas y minúsculas) y espacios.
    patron = r'^[A-Za-z\s]+$'
    return re.match(patron, nombre) is not None
#permite al usuario elegir un rol de inicio de sesión (Administrador, Vendedor o Producción)
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
#======permite autenticar un usuario verificando que su nombre y contraseña 
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
            intentos += 1
            print("\nUsuario o contraseña incorrectos.\n")
            print(f"Intentos restantes: {max_intentos - intentos}\n")

    print("Demasiados intentos fallidos. Acceso denegado.\n")
    return None
# opciones de menu duacuerdo al rol solicitado 
def menu_principal(rol):
    while True:
        print("\n================ MENÚ PRINCIPAL ===========================")

        if rol == "admin":
            print("[1] Gestión de Clientes")
            print("[2] Valores Definitivos (Pedidos)")
            print("[3] Cerrar Sesión")

        elif rol == "vendedor":
            print("[1] Consultar productos disponibles")
            print("[2] Gestión de Pedidos")
            print("[3] Gestión de Clientes")
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
        # Lógica según rol
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
                consultar_productos_disponibles()
            elif opcion == 2:
                registrar_pedido()
            elif opcion == 3:
                registrar_cliente_vendedor()
            elif opcion == 4:
                print("Cerrando sesión...\n")
                break
            else:
                print("Opción inválida.\n")

        elif rol == "produccion":
            if opcion == 1:
                gestion_de_productos()
            elif opcion == 2:
                print("Cerrando sesión...\n")
                break
            else:
                print("Opción inválida.\n")
# crear clientes con validaciones de ingreso de datos
def crear_cliente(clientes):
    print("\n==== Crear Cliente ====")
    id_cliente = input("ID del cliente: ")
    
    if not id_cliente.strip(): #valida que este campo no quede vacio 
        print("❌ El ID del cliente no puede estar vacío.")
        return

    for cliente in clientes: # valida que el id ingresado no este repetido 
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
    clientes.append(cliente) #este diccionario se guarda dentro de la lista clientes 
    print(f"✅ Cliente creado exitosamente el {cliente['fecha']}.\n")
# consultar clientes ya creados
def consultar_cliente(clientes):
    print("\n==== Consultar Clientes ====")
    buscar_cliente = input("Ingrese el ID o nombre de la empresa a buscar: ").strip().lower()

    if not buscar_cliente:
        print("❌ Debe ingresar un dato para buscar.\n")
        return

    encontrados = []  #Almacena temporalmente todos los clientes que coinciden
    # con el criterio de búsqueda (ID o nombre de empresa).
    for cliente in clientes:
        id_cliente = cliente["id"].lower()
        nombre_empresa = cliente["empresa"].lower()

        if buscar_cliente in id_cliente or buscar_cliente in nombre_empresa:
            encontrados.append(cliente)

    if encontrados:
        print(f"\n✅ Se encontraron {len(encontrados)} cliente(s):\n")
        for cliente in encontrados:
            print("=" * 40)
            print(f"ID: {cliente['id']}")
            print(f"Empresa: {cliente['empresa']}")
            print(f"Representante: {cliente['representante']}")
            print(f"Correo: {cliente['correo']}")
            print(f"Teléfono: {cliente['telefono']}")
            print(f"Fecha Registro: {cliente['fecha']}")
    else:
        print("❌ No se encontraron clientes con ese criterio.\n")
# modificar clientes ya creados
def modificar_cliente(clientes):
    print("\n==== Modificar Cliente ====")
    id_buscar = input("Ingrese el ID del cliente a modificar: ").strip()

    cliente_encontrado = None
    for cliente in clientes:
        if cliente["id"] == id_buscar:
            cliente_encontrado = cliente
            break

    if not cliente_encontrado:
        print("❌ Cliente no encontrado.\n")
        return

    print(f"\n✏️ Modificando datos del cliente '{cliente_encontrado['empresa']}'")

    # Modificar nombre de empresa
    nueva_empresa = input(f"Empresa [{cliente_encontrado['empresa']}]: ").title()
    if nueva_empresa:
        if validar_nombre(nueva_empresa):
            cliente_encontrado['empresa'] = nueva_empresa
        else:
            print("❌ Nombre de empresa inválido. No se modificó.")

    # Modificar representante
    nuevo_representante = input(f"Representante [{cliente_encontrado['representante']}]: ").title()
    if nuevo_representante:
        if validar_nombre(nuevo_representante):
            cliente_encontrado['representante'] = nuevo_representante
        else:
            print("❌ Nombre del representante inválido. No se modificó.")

    # Modificar correo
    nuevo_correo = input(f"Correo [{cliente_encontrado['correo']}]: ").lower()
    if nuevo_correo:
        if validar_correo(nuevo_correo):
            cliente_encontrado['correo'] = nuevo_correo
        else:
            print("❌ Correo inválido. No se modificó.")

    # Modificar teléfono
    nuevo_telefono = input(f"Teléfono [{cliente_encontrado['telefono']}]: ")
    if nuevo_telefono:
        if validar_telefono(nuevo_telefono):
            cliente_encontrado['telefono'] = nuevo_telefono
        else:
            print("❌ Teléfono inválido. No se modificó.")

    print("✅ Cliente modificado exitosamente.\n")
#eliminar cliente en caso de que sea necesario
def eliminar_cliente(clientes):
    print("\n==== Eliminar Cliente ====")
    id_eliminar = input("Ingrese el ID del cliente a eliminar: ").strip()

    cliente_encontrado = None
    for cliente in clientes:
        if cliente["id"] == id_eliminar:
            cliente_encontrado = cliente
            break

    if not cliente_encontrado:
        print("❌ Cliente no encontrado.\n")
        return

    # Mostrar información antes de confirmar
    print("\n🗂️ Cliente encontrado:")
    print(f"ID: {cliente_encontrado['id']}")
    print(f"Empresa: {cliente_encontrado['empresa']}")
    print(f"Representante: {cliente_encontrado['representante']}")
    print(f"Correo: {cliente_encontrado['correo']}")
    print(f"Teléfono: {cliente_encontrado['telefono']}")
    print(f"Fecha Registro: {cliente_encontrado['fecha']}")

    confirmacion = input("\n¿Está seguro que desea eliminar este cliente? (s/n): ").lower()
    if confirmacion == 's':
        clientes.remove(cliente_encontrado)
        print("✅ Cliente eliminado exitosamente.\n")
    else:
        print("❎ Operación cancelada. No se eliminó ningún cliente.\n")
#menu para registrar cliente desde el admin
def registrar_cliente_admin():
    while True:
        print("\n===== Menú de Gestión de Clientes (Admin) =====")
        print("[1] Crear cliente")
        print("[2] Modificar cliente")
        print("[3] Eliminar cliente")
        print("[4] Consultar cliente")
        print("[5] Salir")
        print("===============================================")

        opcion = input("Seleccione una opción: ").strip()

        if opcion == "1":
            crear_cliente(clientes)

        elif opcion == "2":
            modificar_cliente(clientes)

        elif opcion == "3":
            eliminar_cliente(clientes)

        elif opcion == "4":
            consultar_cliente(clientes)

        elif opcion == "5":
            print("🔙 Volviendo al menú anterior...\n")
            break

        else:
            print("❌ Opción inválida. Intente de nuevo.\n")
#menu para registrar clientes desde el usuario vendedor
def registrar_cliente_vendedor():
    while True:
        print("\n===== Menú de Clientes (Vendedor) =====")
        print("[1] Crear cliente")
        print("[2] Consultar clientes")
        print("[3] Salir")
        print("=======================================")

        opcion = input("Seleccione una opción: ").strip()

        if opcion == "1":
            crear_cliente(clientes)

        elif opcion == "2":
            consultar_cliente(clientes)

        elif opcion == "3":
            print("🔙 Volviendo al menú anterior...\n")
            break

        else:
            print("❌ Opción inválida. Intente de nuevo.\n")

def gestion_de_productos():
    
    
    while True:
        print("\n====== MENÚ DE GESTIÓN DE PRODUCTOS ======")
        print("1. Agregar producto")
        print("2. Consultar productos")
        print("3. Modificar producto")
        print("4. Eliminar producto")
        print("5. Salir")
        
        opcion = input("Selecciona una opción (1-5): ").strip()
        
        if opcion == "1":
            agregar_producto(productos)
        elif opcion == "2":
            consultar_productos(productos)
        elif opcion == "3":
            modificar_producto(productos)
        elif opcion == "4":
            eliminar_producto(productos)
        elif opcion == "5":
            print("¡Hasta luego!")
            break
        else:
            print("Opción no válida. Por favor, ingresa un número del 1 al 5.")

def agregar_producto(productos):
    print("\n==== Agregar Producto ====")
    
    id_valido = False
    while not id_valido:
        id_producto = input("ID del producto: ").strip()
        
        if not id_producto:
            print("El ID no puede estar vacío.")
        elif not id_producto.isalnum():
            print("El ID solo puede contener letras y números.")
        elif any(producto['id'] == id_producto for producto in productos):
            print("Este ID ya existe. Por favor, ingresa uno diferente.")
        else:
            id_valido = True
    
    nombre_valido = False
    while not nombre_valido:
        nombre_producto = input("Nombre del producto: ").strip().title()
        if nombre_producto != "":
            nombre_valido = True
        else:
            print("❌ Error: El nombre no puede estar vacío")
    
    descripcion_producto = input("Descripción: ").strip()
    
    precio_valido = False
    while not precio_valido:
        precio_input = input("Precio: ").strip()
        try:
            precio_producto = float(precio_input)
            if precio_producto >= 0:
                precio_valido = True
            else:
                print("❌ Error: El precio no puede ser negativo")
        except ValueError:
            print("❌ Error: Debe ingresar un número válido")
    
    nuevo_producto = {
        "id": id_producto,
        "nombre": nombre_producto,
        "descripcion": descripcion_producto,
        "precio": precio_producto,
        "fecha": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }
    
    productos.append(nuevo_producto)
    print(f"\n✅ Producto '{nombre_producto}' agregado exitosamente!")
    print(f"ID: {id_producto} | Precio: ${precio_producto:.2f}\n")

def consultar_productos(productos):
    print("\n==== Consulta de Productos ====")
    
    if not productos:
        print("No hay productos registrados.")
        return
    
    id_buscar = input("Ingrese ID para buscar (Enter para mostrar todos): ").strip()
    
    if id_buscar == "":
        for producto in productos:
            print(f"ID: {producto['id']} | Nombre: {producto['nombre']} | Precio: ${producto['precio']:.2f} | Fecha: {producto['fecha']}")
    else:
        producto_encontrado = False
        for producto in productos:
            if producto['id'] == id_buscar:
                print(f"ID: {producto['id']}\nNombre: {producto['nombre']}\nDescripción: {producto['descripcion']}\nPrecio: ${producto['precio']:.2f}\nFecha: {producto['fecha']}")
                producto_encontrado = True
                break
        
        if not producto_encontrado:
            print(f"No se encontró producto con ID '{id_buscar}'.")

def modificar_producto(productos):
    print("\n==== Modificar Producto ====")
    
    if not productos:
        print("No hay productos para modificar.")
        return
    
    id_producto_modificar = input("Ingrese el ID del producto a modificar: ").strip()
    
    for producto in productos:
        if producto['id'] == id_producto_modificar:
            print(f"Producto encontrado: {producto['nombre']} (Precio: ${producto['precio']:.2f})")
            
            nuevo_nombre_producto = input("Nuevo nombre (Enter para dejar igual): ").strip().title()
            if nuevo_nombre_producto != "":
                producto['nombre'] = nuevo_nombre_producto
            
            nueva_descripcion_producto = input("Nueva descripción (Enter para dejar igual): ").strip()
            if nueva_descripcion_producto != "":
                producto['descripcion'] = nueva_descripcion_producto
            
            while True:
                nuevo_precio_producto = input("Nuevo precio (Enter para dejar igual): ").strip()
                if nuevo_precio_producto == "":
                    break
                try:
                    nuevo_precio_float = float(nuevo_precio_producto)
                    if nuevo_precio_float >= 0:
                        producto['precio'] = nuevo_precio_float
                        break
                    else:
                        print("❌ Error: El precio no puede ser negativo")
                except ValueError:
                    print("❌ Error: Debe ingresar un número válido")
            
            print("✅ Producto modificado correctamente.")
            return
    
    print(f"No se encontró producto con ID '{id_producto_modificar}'.")

def eliminar_producto(productos):
    print("\n==== Eliminar Producto ====")
    
    if not productos:
        print("No hay productos para eliminar.")
        return
    
    id_producto_eliminar = input("Ingrese el ID del producto a eliminar: ").strip()
    
    for indice, producto in enumerate(productos):
        if producto['id'] == id_producto_eliminar:
            confirmacion_eliminar = input(f"¿Seguro que quieres eliminar '{producto['nombre']}'? (s/n): ").strip().lower()
            if confirmacion_eliminar == "s":
                productos.pop(indice)
                print("✅ Producto eliminado correctamente.")
            else:
                print("Operación cancelada.")
            return
    
    print(f"No se encontró producto con ID '{id_producto_eliminar}'.")


