from datetime import datetime
import re
#import uuid 

# Listas para almacenar la información
clientes = []
pedidos = []    
productos = []

# Listas con las tallas y colores disponibles
tallas_disponibles = ["XS", "S", "M", "L", "XL", "XXL", "XXXL"]
colores_disponibles = ["azul", "caqui", "naranja"] 
contador_ped = 0
contador_pro = 0

tallas_disponibles = ["XS", "S", "M", "L", "XL", "XXL", "XXXL"]
colores_disponibles = ["azul", "caqui", "naranja"] 
contador = 0
# Lista de usuarios existentes
users = [
    {"nombre_usuario": "Borozco", "contraseña": "4321", "rol": "admin"},
    {"nombre_usuario": "Kpuerta", "contraseña": "1234", "rol": "vendedor"},
    {"nombre_usuario": "Jmarti", "contraseña": "canalete", "rol": "produccion"}
]

roles_permitidos = ['admin', 'vendedor', 'produccion']

# Función para validar rol
def rol_es_valido(rol):
    return rol.lower() in roles_permitidos

# Menú de gestión de usuarios
def Gestion_usuarios():
    while True:
        print("\n===== Menú de Gestión de Usuarios =====")
        print("[1] Crear Usuario")
        print("[2] Consultar Usuarios")
        print("[3] Modificar Usuario")
        print("[4] Eliminar Usuario")
        print("[5] Salir")
        print("=======================================")

        opcion = input("Seleccione una opción: ").strip()

        if opcion == "1":
            registrar_usuario()

        elif opcion == "2":
            consultar_usuarios()

        elif opcion == "3":
            modificar_usuarios()

        elif opcion == "4":
            eliminar_usuario()

        elif opcion == "5":
            print("🔙 Volviendo al menú anterior...\n")
            break

        else:
            print("❌ Opción inválida. Intente de nuevo.\n")

# Registrar nuevo usuario
def registrar_usuario():
    nombre_usuario = input("Nombre de usuario: ").strip()
    contraseña = input("Ingrese contraseña: ").strip()
    rol = input("Ingrese el rol asignado (admin, vendedor, produccion): ").strip().lower()

    if any(u['nombre_usuario'] == nombre_usuario for u in users):
        print(f"❌ El usuario '{nombre_usuario}' ya existe.")
        return

    if not rol_es_valido(rol):
        print(f"❌ Rol inválido. Roles permitidos: {roles_permitidos}")
        return

    nuevo_usuario = {
        "nombre_usuario": nombre_usuario,
        "contraseña": contraseña,
        "rol": rol
    }
    users.append(nuevo_usuario)
    print(f"✅ Usuario '{nombre_usuario}' registrado como '{rol}'.")

# Consultar usuarios
def consultar_usuarios():
    if not users:
        print("No hay usuarios registrados.")
        return
    print("\n📋 Lista de usuarios:")
    for u in users:
        print(f"Usuario: {u['nombre_usuario']}, Rol: {u['rol']}")

# Modificar usuario
def modificar_usuarios():
    nombre = input("Ingrese el nombre del usuario a modificar: ").strip()

    usuario = next((u for u in users if u["nombre_usuario"] == nombre), None)

    if not usuario:
        print("❌ Usuario no encontrado.")
        return

    print(f"Usuario encontrado: {usuario}")

    while True:
        print("\nCampos disponibles:")
        print("[1] Nombre de usuario")
        print("[2] Contraseña")
        print("[3] Rol")
        print("[4] Guardar y salir")
        print("[5] Cancelar cambios")

        opcion = input("Opción: ").strip()

        if opcion == "1":
            nuevo_nombre = input("Nuevo nombre de usuario: ").strip()
            if any(u['nombre_usuario'] == nuevo_nombre for u in users):
                print("❌ Ese nombre de usuario ya existe.")
            else:
                usuario["nombre_usuario"] = nuevo_nombre
                print("✅ Nombre actualizado.")

        elif opcion == "2":
            nueva_contra = input("Nueva contraseña: ").strip()
            usuario["contraseña"] = nueva_contra
            print("✅ Contraseña actualizada.")

        elif opcion == "3":
            nuevo_rol = input("Nuevo rol: ").strip().lower()
            if rol_es_valido(nuevo_rol):
                usuario["rol"] = nuevo_rol
                print("✅ Rol actualizado.")
            else:
                print(f"❌ Rol inválido. Roles permitidos: {roles_permitidos}")

        elif opcion == "4":
            print("✅ Cambios guardados.")
            break

        elif opcion == "5":
            print("❎ Cambios descartados.")
            break

        else:
            print("❌ Opción inválida.")

# Eliminar usuario
def eliminar_usuario():
    nombre = input("Ingrese el nombre del usuario a eliminar: ").strip()
    usuario = next((u for u in users if u["nombre_usuario"] == nombre), None)

    if not usuario:
        print("❌ Usuario no encontrado.")
        return

    print(f"Usuario encontrado: {usuario}")
    confirmacion = input("¿Desea eliminar este usuario? (s/n): ").strip().lower()

    if confirmacion == 's':
        users.remove(usuario)
        print("✅ Usuario eliminado.")
    else:
        print("❎ Operación cancelada.")

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
                linea = f"{pedido['fecha']}|{pedido['id_pedido']}|{pedido['id_cliente']}|{pedido['cliente_nombre']}|{pedido['id_producto']}|{pedido['producto_nombre']}|{pedido['color']}|{pedido['talla']}|{pedido['cantidad']}|{pedido['precio_unitario']}|{pedido['subtotal']}|{pedido['iva']}|{pedido['total']}\n"
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
                    'id_pedido' : datos[1],
                    'id_cliente': datos[2],
                    'cliente_nombre': datos[3],
                    'id_producto': datos[4],
                    'producto_nombre': datos[5],
                    'color': datos[6],
                    'talla': datos[7],
                    'cantidad': datos[8],
                    'precio_unitario': float(datos[9]),
                    'subtotal': float(datos[10]),
                    'iva': float(datos[11]),
                    'total': datos[12]
                })
    except FileNotFoundError:
        print("Archivo de pedidos no encontrado. Se creará uno nuevo.")

def guardar_contadores_pro():
    """Guarda los contadores en un archivo"""
    try:
        with open('contadores_pro.txt', 'w') as f:
            f.write(f"contador_pro|{contador_pro}\n")
    except Exception as e:
        print(f"Error al guardar contadores: {e}")

def cargar_contadores_pro():
    """Carga los contadores desde archivo"""
    global contador_pro
    try:
        with open('contadores_pro.txt', 'r') as f:
            for linea in f:
                if 'contador_pro|' in linea:
                    contador_pro = int(linea.split('|')[1])
    except FileNotFoundError:
        print("Archivo de contadores no encontrado. Se iniciarán desde cero.")
    except Exception as e:
        print(f"Error al cargar contadores: {e}")
        
def guardar_contadores_ped():
    """Guarda los contadores en un archivo"""
    try:
        with open('contadores_ped.txt', 'w') as f:
            f.write(f"contador_ped|{contador_ped}\n")
    except Exception as e:
        print(f"Error al guardar contadores: {e}")

def cargar_contadores_ped():
    """Carga los contadores desde archivo"""
    global contador_pro
    try:
        with open('contadores_ped.txt', 'r') as f:
            for linea in f:
                if 'contador_ped|' in linea:
                    contador_ped = int(linea.split('|')[1])
    except FileNotFoundError:
        print("Archivo de contadores no encontrado. Se iniciarán desde cero.")
    except Exception as e:
        print(f"Error al cargar contadores: {e}")

# Función para crear códigos automáticos
def generar_codigo_producto():
    global contador_pro
    contador_pro += 1
    guardar_contadores_pro()
    return f'pr{contador_pro:03d}'

def generar_codigo_pedido():
    global contador_ped
    contador_ped += 1
    guardar_contadores_ped()
    return f'pd{contador_ped:03d}'

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
            usuario = autenticador_usuario(users, "admin")
            if usuario:
                return ("admin", usuario)
        elif opc == "2":
            usuario = autenticador_usuario(users, "vendedor")
            if usuario:
                return ("vendedor", usuario)
        elif opc == "3":
            usuario = autenticador_usuario(users, "produccion")
            if usuario:
                return ("produccion", usuario)
        else:
            print("Opción inválida, intente nuevamente.")
#======permite autenticar un usuario verificando que su nombre y contraseña 
def autenticador_usuario(users, rol_esperado, max_intentos=3):
    for intento in range(max_intentos):
        user = input("Ingrese Usuario: ")
        contraseña = input("Contraseña: ")
        for usuario in users:
            if usuario["nombre_usuario"] == user and usuario["contraseña"] == contraseña and usuario["rol"] == rol_esperado:
                print(f"\n✅ ¡Bienvenido {user}!\n")
                return user
        print("❌ Usuario o contraseña incorrectos.")
    print("🔒 Acceso denegado por intentos fallidos.\n")
    return None


    print("Demasiados intentos fallidos. Acceso denegado.\n")
    return None
# opciones de menu duacuerdo al rol solicitado 
def menu_principal(rol):  # menu principal deacuerdo al roll seleccionado 
    while True:             #cada roll ya tiene opciones predefinidas 
        print("\n================ MENÚ PRINCIPAL ===========================")

        if rol == "admin":
            print("[1] Gestión de Clientes")
            print("[2] Valores Definitivos (Pedidos)")
            print("[3] registrar nuevos usuarios")
            print("[4] Cerrar Sesión")

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
        if rol == "admin": # opciones disponibles del admin
            if opcion == 1:
                registrar_cliente_admin()
            elif opcion == 2:
                while True:
                    print("\n===== Menú de Pedidos (Admin) =====")
                    print("[1] Listar todos los pedidos")
                    print("[2] Reporte por rango de fechas")
                    print("[3] Volver al menú principal")
                    
                    sub_opcion = input("Seleccione una opción: ").strip()
                    
                    if sub_opcion == "1":
                        listar_pedidos()
                    elif sub_opcion == "2":
                        reporte_pedidos_por_fecha()
                    elif sub_opcion == "3":
                        break
                    else:
                        print("❌ Opción inválida. Intente de nuevo.\n")              
                
            elif opcion == 3:
                Gestion_usuarios()
            elif opcion == 4:
                print("Cerrando sesión...\n")
                break
            else:
                print("Opción inválida.\n")
                
        elif rol == "vendedor": #opciones disponibles del vendedor

            if opcion == 1:
                consultar_producto()
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
    
    #id_valido = False
    #while not id_valido:
       #id_producto = input("ID del producto: ").strip()
       
       #if not id_producto:
           #print("El ID no puede estar vacío.")
       #elif not id_producto.isalnum():
           #print("El ID solo puede contener letras y números.")
       #elif any(producto['id'] == id_producto for producto in productos):
           #print("Este ID ya existe. Por favor, ingresa uno diferente.")
       #else:
           #id_valido = True
    
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

    id_producto = generar_codigo_producto()
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
        id_pedido = generar_codigo_pedido()
        nuevo_pedido = {
            "id_pedido" : id_pedido,
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
    print(f"{'Fecha':<20} | {'id_pedido':>6} | {'Cliente':<20} | {'Producto':<20} | {'Cantidad':>10} | {'Total':>10}")
    print("-" * 80)
    
    for pedido in pedidos:
        print(
            f"{pedido['fecha']:<20} | "
            f"{pedido['id_pedido']:1>6} | "
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

def reporte_pedidos_por_fecha():
    print("\n📅 === Reporte de Pedidos por Rango de Fechas ===")
    
    if not pedidos:
        print("❌ No hay pedidos registrados.\n")
        return
    
    # Validar formato de fecha inicial
    while True:
        fecha_inicio = input("Ingrese fecha inicial (YYYY-MM-DD): ").strip()
        try:
            fecha_inicio_dt = datetime.strptime(fecha_inicio, "%Y-%m-%d")
            break
        except ValueError:
            print("❌ Formato de fecha inválido. Use YYYY-MM-DD.")
    
    # Validar formato de fecha final
    while True:
        fecha_fin = input("Ingrese fecha final (YYYY-MM-DD): ").strip()
        try:
            fecha_fin_dt = datetime.strptime(fecha_fin, "%Y-%m-%d")
            if fecha_fin_dt >= fecha_inicio_dt:
                break
            else:
                print("❌ La fecha final debe ser igual o posterior a la fecha inicial.")
        except ValueError:
            print("❌ Formato de fecha inválido. Use YYYY-MM-DD.")
    
    # Filtrar pedidos en el rango de fechas
    pedidos_filtrados = []
    for pedido in pedidos:
        try:
            fecha_pedido = datetime.strptime(pedido['fecha'].split()[0], "%Y-%m-%d")
            if fecha_inicio_dt <= fecha_pedido <= fecha_fin_dt:
                pedidos_filtrados.append(pedido)
        except (ValueError, IndexError):
            continue
    
    if not pedidos_filtrados:
        print(f"\nℹ️ No se encontraron pedidos entre {fecha_inicio} y {fecha_fin}.\n")
        return
    
    # Mostrar resultados
    print(f"\n📊 REPORTE DE PEDIDOS ({fecha_inicio} a {fecha_fin})")
    print("=" * 100)
    print(f"{'Fecha':<20} | {'id_pedido':>6} | {'Cliente':<20} | {'Producto':<20} | {'Color':<10} | {'Talla':<6} | {'Cant.':>6} | {'Total':>12}")
    print("=" * 100)
    
    total_general = 0
    for pedido in pedidos_filtrados:
        print(
            f"{pedido['fecha']:<20} | "
            f"{pedido['id_pedido']:>6} | "
            f"{pedido['cliente_nombre']:<20} | "
            f"{pedido['producto_nombre']:<20} | "
            f"{pedido['color']:<10} | "
            f"{pedido['talla']:<6} | "
            f"{pedido['cantidad']:>6} | "
            f"${float(pedido['total']):>11.2f}"
        )
        total_general += float(pedido['total'])
    
    print("=" * 100)
    print(f"{'TOTAL GENERAL:':<80} ${total_general:>11.2f}")
    print("=" * 100)
    
    # Opción para exportar a archivo
    exportar = input("\n¿Desea exportar este reporte a un archivo? (s/n): ").strip().lower()
    if exportar == 's':
        nombre_archivo = f"reporte_pedidos_{fecha_inicio}_a_{fecha_fin}.txt"
        try:
            with open(nombre_archivo, 'w') as f:
                f.write(f"REPORTE DE PEDIDOS ({fecha_inicio} a {fecha_fin})\n")
                f.write("=" * 100 + "\n")
                f.write(f"{'Fecha':<20} | {'Cliente':<20} | {'Producto':<20} | {'Color':<10} | {'Talla':<6} | {'Cant.':>6} | {'Total':>12}\n")
                f.write("=" * 100 + "\n")
                
                for pedido in pedidos_filtrados:
                    f.write(
                        f"{pedido['fecha']:<20} | "
                        f"{pedido['cliente_nombre']:<20} | "
                        f"{pedido['producto_nombre']:<20} | "
                        f"{pedido['color']:<10} | "
                        f"{pedido['talla']:<6} | "
                        f"{pedido['cantidad']:>6} | "
                        f"${pedido['total']:>11.2f}\n"
                    )
                
                f.write("=" * 100 + "\n")
                f.write(f"{'TOTAL GENERAL:':<80} ${total_general:>11.2f}\n")
                f.write("=" * 100 + "\n")
            
            print(f"✅ Reporte exportado correctamente como '{nombre_archivo}'")
        except Exception as e:
            print(f"❌ Error al exportar el reporte: {e}")

# ================== FLUJO PRINCIPAL ==================
def programa():
    cargar_datos()
    cargar_contadores_ped()
    cargar_contadores_pro()# <-- Añadimos esta línea
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