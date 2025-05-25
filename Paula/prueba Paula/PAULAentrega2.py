from datetime import datetime
import re

# Diccionarios para usuarios 
user1 = {"bo": "admin1234"}
user2 = {"kp": "local1234"}
user3 = {"jm": "produ1234"}

# Listas para almacenar la información
clientes = []
inventario = []
pedidos = []    
productos = []

# Listas con las tallas y colores disponibles
tallas_disponibles = ["XS", "S", "M", "L", "XL", "XXL", "XXXL"]
colores_disponibles = ["azul", "caqui", "naranja"] 
contador = 0
# ================== VARIABLES GLOBALES ==================

# Listas para almacenar la información (ahora se cargarán desde archivos)
clientes = []
inventario = []
pedidos = []    
productos = []

# Listas con las tallas y colores disponibles
tallas_disponibles = ["XS", "S", "M", "L", "XL", "XXL", "XXXL"]
colores_disponibles = ["azul", "caqui", "naranja"] 
contador = 0

# ================== SISTEMA DE ARCHIVOS ==================
def guardar_datos():
    """Guarda todas las listas en archivos .txt para persistencia de datos"""
    try:
        # Guardar clientes
        with open('clientes.txt', 'w') as f: #open es un metodo que permite trabajar con archivos "W" es modo de apertura para escribir
            for cliente in clientes:
                linea = f"{cliente['id']}|{cliente['empresa']}|{cliente['representante']}|{cliente['correo']}|{cliente['telefono']}|{cliente['fecha']}\n"
                f.write(linea)
        
        # Guardar productos
        with open('productos.txt', 'w') as f:
            for producto in productos:
                linea = f"{producto['id']}|{producto['nombre']}|{producto['descripcion']}|{producto['precio']}|{producto['fecha']}\n"
                f.write(linea)
        
        # Guardar pedidos
        with open('pedidos.txt', 'w') as f:
            for pedido in pedidos:
                linea = f"{pedido['fecha']}|{pedido['id_cliente']}|{pedido['cliente_nombre']}|{pedido['id_producto']}|{pedido['producto_nombre']}|{pedido['color']}|{pedido['talla']}|{pedido['cantidad']}|{pedido['precio_unitario']}|{pedido['subtotal']}|{pedido['iva']}|{pedido['total']}\n"
                f.write(linea)
    except Exception as e:
        print(f"Error al guardar datos: {e}")

def cargar_datos():
    """Carga los datos desde archivos .txt al iniciar el programa"""
    global clientes, productos, pedidos
    
    # Cargar clientes
    try:
        with open('clientes.txt', 'r') as f:
            for linea in f:
                datos = linea.strip().split('|')
                clientes.append({
                    'id': datos[0],
                    'empresa': datos[1],
                    'representante': datos[2],
                    'correo': datos[3],
                    'telefono': datos[4],
                    'fecha': datos[5]
                })
    except FileNotFoundError:
        print("Archivo de clientes no encontrado. Se creará uno nuevo.")
    
    # Cargar productos
    try:
        with open('productos.txt', 'r') as f:
            for linea in f:
                datos = linea.strip().split('|')
                productos.append({
                    'id': datos[0],
                    'nombre': datos[1],
                    'descripcion': datos[2],
                    'precio': float(datos[3]),
                    'fecha': datos[4]
                })
    except FileNotFoundError:
        print("Archivo de productos no encontrado. Se creará uno nuevo.")
    
    # Cargar pedidos
    try:
        with open('pedidos.txt', 'r') as f:
            for linea in f:
                datos = linea.strip().split('|')
                pedidos.append({
                    'fecha': datos[0],
                    'id_cliente': datos[1],
                    'cliente_nombre': datos[2],
                    'id_producto': datos[3],
                    'producto_nombre': datos[4],
                    'color': datos[5],
                    'talla': datos[6],
                    'cantidad': int(datos[7]),
                    'precio_unitario': float(datos[8]),
                    'subtotal': float(datos[9]),
                    'iva': float(datos[10]),
                    'total': float(datos[11])
                })
    except FileNotFoundError:
        print("Archivo de pedidos no encontrado. Se creará uno nuevo.")
# Función para crear códigos automáticos
def generar_codigo():
    global contador
    contador += 1
    return f'PRO{contador:03d}'

# ============ Funciones para validar ============
def validar_correo(correo):
    patron = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    return re.match(patron, correo) is not None

def validar_telefono(telefono):
    return telefono.isdigit() and 7 <= len(telefono) <= 15

def validar_nombre(nombre):
    patron = r'^[A-Za-z\s]+$'
    return re.match(patron, nombre) is not None

# Función para el menú de inicio de sesión
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

# Función para autenticar usuarios
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

# Menú principal según rol
def menu_principal(rol):
    while True:
        print("\n================ MENÚ PRINCIPAL ===========================")

        if rol == "admin":
            print("[1] Gestión de Clientes")
            print("[2] Consultar pedidos realizados")
            print("[3] Cerrar Sesión")

        elif rol == "vendedor":
            print("[1] Consultar pedidos realizados")
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
                listar_pedidos()
            elif opcion == 2:
                registrar_pedido()
            elif opcion == 3:
                registrar_cliente_vendedor()
            elif opcion == 4:
                print("Cerrando sesión...\n")
                break
            else:
                print("Opción inválida. Intente nuevamente.")

        elif rol == "produccion":
            if opcion == 1:
                gestion_de_productos()
            elif opcion == 2:
                print("Cerrando sesión...\n")
                break
            else:
                print("Opción inválida.\n")

# ================================== Gestión de clientes ===============================================
def crear_cliente(clientes):
    print("\n==== Crear Cliente ====")
    id_cliente = input("ID del cliente: ")
    
    if not id_cliente.strip():
        print("❌ El ID del cliente no puede estar vacío.")
        return

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
    guardar_datos()  # <-- Añadimos esta línea
    print(f"✅ Cliente creado exitosamente el {cliente['fecha']}.\n")

def consultar_cliente(clientes):
    print("\n==== Consultar Clientes ====")
    buscar_cliente = input("Ingrese el ID o nombre de la empresa a buscar: ").strip().lower()

    if not buscar_cliente:
        print("❌ Debe ingresar un dato para buscar.\n")
        return

    encontrados = []
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

def modificar_cliente(clientes):
    print("\n==== Modificar Cliente ====")
    
    if not clientes:
        print("❌ No hay clientes registrados para modificar.\n")
        return
    
    id_modificar = input("Ingrese el ID del cliente a modificar: ").strip()
    
    cliente_encontrado = None
    for cliente in clientes:
        if cliente["id"] == id_modificar:
            cliente_encontrado = cliente
            break
    
    if not cliente_encontrado:
        print("❌ Cliente no encontrado.\n")
        return
    
    print("\n📝 Cliente encontrado - Datos actuales:")
    print(f"1. ID: {cliente_encontrado['id']}")
    print(f"2. Empresa: {cliente_encontrado['empresa']}")
    print(f"3. Representante: {cliente_encontrado['representante']}")
    print(f"4. Correo: {cliente_encontrado['correo']}")
    print(f"5. Teléfono: {cliente_encontrado['telefono']}")
    print(f"Fecha Registro: {cliente_encontrado['fecha']}")
    
    while True:
        print("\nSeleccione el campo a modificar:")
        print("[1] Nombre de la Empresa")
        print("[2] Representante Legal")
        print("[3] Correo Electrónico")
        print("[4] Teléfono")
        print("[5] Guardar cambios y salir")
        print("[6] Salir sin guardar")
        
        opcion = input("Opción: ").strip()
        
        if opcion == "1":
            while True:
                nueva_empresa = input("Nuevo nombre de la Empresa: ").title()
                if validar_nombre(nueva_empresa):
                    cliente_encontrado["empresa"] = nueva_empresa
                    print("✅ Nombre de empresa actualizado.")
                    break
                print("❌ El nombre de la empresa solo debe contener letras y espacios.")
        
        elif opcion == "2":
            while True:
                nuevo_representante = input("Nuevo representante legal: ").title()
                if validar_nombre(nuevo_representante):
                    cliente_encontrado["representante"] = nuevo_representante
                    print("✅ Representante legal actualizado.")
                    break
                print("❌ El nombre del representante solo debe contener letras y espacios.")
        
        elif opcion == "3":
            while True:
                nuevo_correo = input("Nuevo correo: ").lower()
                if validar_correo(nuevo_correo):
                    cliente_encontrado["correo"] = nuevo_correo
                    print("✅ Correo electrónico actualizado.")
                    break
                print("❌ Correo inválido. Intenta nuevamente.")
        
        elif opcion == "4":
            while True:
                nuevo_telefono = input("Nuevo teléfono: ")
                if validar_telefono(nuevo_telefono):
                    cliente_encontrado["telefono"] = nuevo_telefono
                    print("✅ Teléfono actualizado.")
                    break
                print("❌ Teléfono inválido. Solo números, de 7 a 15 dígitos.")
        
        elif opcion == "5":
            cliente_encontrado["fecha"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            guardar_datos()  # <-- Añadimos esta línea
            print("✅ Cambios guardados exitosamente.\n")
            break
        
        elif opcion == "6":
            print("❎ Cambios descartados. Volviendo al menú anterior.\n")
            break
        
        else:
            print("❌ Opción inválida. Intente nuevamente.")

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
        guardar_datos()  # <-- Añadimos esta línea
        print("✅ Cliente eliminado exitosamente.\n")
    else:
        print("❎ Operación cancelada. No se eliminó ningún cliente.\n")

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

# ================================== Gestión de Productos ===============================================
def gestion_de_productos():
    while True:
        print("\n====== MENÚ DE GESTIÓN DE PRODUCTOS ======")
        print("[1] Agregar producto")
        print("[2] Consultar productos")
        print("[3] Modificar producto")
        print("[4] Eliminar producto")
        print("[5] Salir")
        
        opcion = input("Selecciona una opción (1-5): ").strip()
        
        if opcion == "1":
            agregar_producto(productos)
        elif opcion == "2":
            consultar_producto(productos)
        elif opcion == "3":
            modificar_producto(productos)
        elif opcion == "4":
            eliminar_producto(productos)
        elif opcion == "5":
            print("¡Hasta luego!")
            break
        else:
            print("!ERROR¡ Opción no válida. Por favor.")

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

    id_producto = generar_codigo()
    nuevo_producto = {
        "id": id_producto,
        "nombre": nombre_producto,
        "descripcion": descripcion_producto,
        "precio": precio_producto,
        "fecha": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }
    
    productos.append(nuevo_producto)
    guardar_datos()  # <-- Añadimos esta línea
    print(f"\n✅ Producto '{nombre_producto}' agregado exitosamente!")
    print(f"ID: {id_producto} | Precio: ${precio_producto:.2f}\n")

def consultar_producto(productos):
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
        print("❌ No hay productos registrados para modificar.\n")
        return
    
    print("\n📋 Lista de Productos Disponibles:")
    for producto in productos:
        print(f"ID: {producto['id']} | Nombre: {producto['nombre']} | Precio: ${producto['precio']:.2f}")
    
    id_modificar = input("\nIngrese el ID del producto a modificar: ").strip()
    
    producto_encontrado = None
    for producto in productos:
        if producto["id"] == id_modificar:
            producto_encontrado = producto
            break
    
    if not producto_encontrado:
        print("❌ Producto no encontrado.\n")
        return
    
    print("\n📝 Producto encontrado - Datos actuales:")
    print(f"1. ID: {producto_encontrado['id']}")
    print(f"2. Nombre: {producto_encontrado['nombre']}")
    print(f"3. Descripción: {producto_encontrado['descripcion']}")
    print(f"4. Precio: ${producto_encontrado['precio']:.2f}")
    print(f"Fecha Registro: {producto_encontrado['fecha']}")
    
    while True:
        print("\nSeleccione el campo a modificar:")
        print("[1] Nombre del Producto")
        print("[2] Descripción")
        print("[3] Precio")
        print("[4] Guardar cambios y salir")
        print("[5] Salir sin guardar")
        
        opcion = input("Opción: ").strip()
        
        if opcion == "1":
            while True:
                nuevo_nombre = input("Nuevo nombre del producto: ").strip().title()
                if nuevo_nombre:
                    producto_encontrado["nombre"] = nuevo_nombre
                    print("✅ Nombre del producto actualizado.")
                    break
                print("❌ El nombre no puede estar vacío.")
        
        elif opcion == "2":
            nueva_descripcion = input("Nueva descripción: ").strip()
            producto_encontrado["descripcion"] = nueva_descripcion
            print("✅ Descripción actualizada.")
        
        elif opcion == "3":
            while True:
                nuevo_precio = input("Nuevo precio: ").strip()
                try:
                    precio_float = float(nuevo_precio)
                    if precio_float >= 0:
                        producto_encontrado["precio"] = precio_float
                        print("✅ Precio actualizado.")
                        break
                    print("❌ El precio no puede ser negativo.")
                except ValueError:
                    print("❌ Debe ingresar un número válido para el precio.")
        
        elif opcion == "4":
            producto_encontrado["fecha"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            guardar_datos()  # <-- Añadimos esta línea
            print("✅ Cambios guardados exitosamente.\n")
            break
        
        elif opcion == "5":
            print("❎ Cambios descartados. Volviendo al menú anterior.\n")
            break
        
        else:
            print("❌ Opción inválida. Intente nuevamente.")

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
                guardar_datos()  # <-- Añadimos esta línea
                print("✅ Producto eliminado correctamente.")
            else:
                print("Operación cancelada.")
            return
    
    print(f"No se encontró producto con ID '{id_producto_eliminar}'.")

# ================================== Gestión de Pedidos ==============================================
def registrar_pedido():
    print("\n📦 === Registrar Pedido ===")

    if not productos:
        print("❌ No hay productos registrados.\n")
        return
    if not clientes:
        print("❌ No hay clientes registrados.\n")
        return

    # Menú de clientes
    print("\n👥 Clientes disponibles:")
    for indice, cliente in enumerate(clientes, start=1):
        print(f"{indice}. {cliente['empresa']} (ID: {cliente['id']})")

    cliente_encontrado = None
    while cliente_encontrado is None:
        try:
            seleccion_cliente = int(input("\nSeleccione el número del cliente: "))
            if 1 <= seleccion_cliente <= len(clientes):
                cliente_encontrado = clientes[seleccion_cliente - 1]
            else:
                print("❌ Número fuera de rango.")
        except ValueError:
            print("❌ Ingrese un número válido.")

    # Agregar varios productos
    agregar_otro_producto = "s"
    while agregar_otro_producto.lower() == "s":
        # Menú de productos
        print("\n🛍️ Productos disponibles:")
        for indice, producto in enumerate(productos, start=1):
            print(f"{indice}. {producto['nombre']} - ${producto['precio']:,} (ID: {producto['id']})")

        producto_encontrado = None
        while producto_encontrado is None:
            try:
                seleccion_producto = int(input("\nSeleccione el número del producto: "))
                if 1 <= seleccion_producto <= len(productos):
                    producto_encontrado = productos[seleccion_producto - 1]
                else:
                    print("❌ Número fuera de rango.")
            except ValueError:
                print("❌ Ingrese un número válido.")

        # Menú de tallas
        print("\n📏 Tallas disponibles:")
        for i, talla in enumerate(tallas_disponibles, start=1):
            print(f"{i}. {talla}")
        talla_ingresada = ""
        while talla_ingresada == "":
            try:
                seleccion_talla = int(input("Seleccione el número de la talla: "))
                if 1 <= seleccion_talla <= len(tallas_disponibles):
                    talla_ingresada = tallas_disponibles[seleccion_talla - 1]
                else:
                    print("❌ Número fuera de rango.")
            except ValueError:
                print("❌ Ingrese un número válido.")

        # Menú de colores
        print("\n🎨 Colores disponibles:")
        for i, color in enumerate(colores_disponibles, start=1):
            print(f"{i}. {color}")
        color_ingresado = ""
        while color_ingresado == "":
            try:
                seleccion_color = int(input("Seleccione el número del color: "))
                if 1 <= seleccion_color <= len(colores_disponibles):
                    color_ingresado = colores_disponibles[seleccion_color - 1]
                else:
                    print("❌ Número fuera de rango.")
            except ValueError:
                print("❌ Ingrese un número válido.")

        # Cantidad
        try:
            cantidad_ingresada = int(input("🧮 Ingrese la cantidad: "))
            if cantidad_ingresada <= 0:
                print("❌ La cantidad debe ser mayor que 0.\n")
                continue
        except ValueError:
            print("❌ Por favor ingrese un número válido.\n")
            continue

        # Cálculos
        precio_unitario = producto_encontrado["precio"]
        subtotal = cantidad_ingresada * precio_unitario
        iva = subtotal * 0.19
        total = subtotal + iva

        # Crear pedido
        nuevo_pedido = {
            "fecha": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "id_cliente": cliente_encontrado["id"],
            "cliente_nombre": cliente_encontrado["empresa"],
            "id_producto": producto_encontrado["id"],
            "producto_nombre": producto_encontrado["nombre"],
            "color": color_ingresado,
            "talla": talla_ingresada,
            "cantidad": cantidad_ingresada,
            "precio_unitario": precio_unitario,
            "subtotal": subtotal,
            "iva": iva,
            "total": total
        }

        pedidos.append(nuevo_pedido)
        guardar_datos()

        print(f"\n✅ Producto agregado al pedido (Total con IVA: ${total:,.2f})")

        # ¿Agregar otro producto?
        agregar_otro_producto = input("\n➕ ¿Desea agregar otro producto al mismo pedido? (s/n): ").strip().lower()
        while agregar_otro_producto not in ["s", "n"]:
            agregar_otro_producto = input("❓ Respuesta inválida. Ingrese 's' o 'n': ").strip().lower()

    print("\n✅ Pedido finalizado y registrado correctamente.\n")



def listar_pedidos():#=========================================listar pedidos===================
    print("\n==== Listado de Pedidos ====")
    
    if not pedidos:
        print("No hay pedidos registrados.")
        return
    
    # Encabezado
    print("-" * 80)
    print(f"{'Fecha':<20} | {'Cliente':<20} | {'Producto':<20} | {'Cantidad':>10} | {'Total':>10}")
    print("-" * 80)
    
    for pedido in pedidos:
        print(
            f"{pedido['fecha']:<20} | "
            f"{pedido['cliente_nombre']:<20} | "
            f"{pedido['producto_nombre']:<20} | "
            f"{pedido['cantidad']:>10} | "
            f"${pedido['total']:>9.2f}"
        )
    
    # Total general
    total_general = sum(p['total'] for p in pedidos)
    print("-" * 80)
    print(f"{'TOTAL GENERAL:':<63} ${total_general:>9.2f}")
    print("-" * 80)


# ================== FLUJO PRINCIPAL ==================
def programa():
    cargar_datos()  # <-- Añadimos esta línea
    while True:
        resultado = menu_usuario()
        if resultado:
            rol, usuario = resultado
            menu_principal(rol)
        else:
            guardar_datos()  # <-- Añadimos esta línea
            print("Acceso denegado o máximo de intentos fallidos.")
            break

programa()