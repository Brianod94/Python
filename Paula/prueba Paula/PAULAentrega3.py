from datetime import datetime
import re
clientes = []
pedidos = []    
productos = []
tallas_disponibles = ["XS", "S", "M", "L", "XL", "XXL", "XXXL"]
colores_disponibles = ["azul", "caqui", "naranja"] 
contador = 0
# Lista de usuarios existentes
users = [
    {"nombre_usuario": "Bo", "contraseña": "4321", "rol": "admin"},
    {"nombre_usuario": "Kp", "contraseña": "1234", "rol": "vendedor"},
    {"nombre_usuario": "Jm", "contraseña": "canalete", "rol": "produccion"}
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



# funcion para crear codigos automaticos
def generar_codigo():
    global contador
    contador += 1
    return f'PRO{contador:03d}'
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
        if rol == "admin": #============================= opciones disponibles del admin
            if opcion == 1:
                registrar_cliente_admin()
            elif opcion == 2:
                listar_pedidos()
            elif opcion == 3:
                Gestion_usuarios()
            elif opcion == 4:
                print("Cerrando sesión...\n")
                break
            else:
                print("Opción inválida.\n")

        elif rol == "vendedor": #===========================opciones disponibles del vendedor

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
                print("Opción inválida. Intente nuevamente.")


        elif rol == "produccion":
            if opcion == 1:
                gestion_de_productos()
            elif opcion == 2:
                print("Cerrando sesión...\n")
                break
            else:
                print("Opción inválida.\n")
# ================================== gestion de clientes con todas sus validaciones ===============================================
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
    
    # Validar que existan clientes registrados
    if not clientes:
        print("❌ No hay clientes registrados para modificar.\n")
        return
    
    # Solicitar ID del cliente a modificar
    id_modificar = input("Ingrese el ID del cliente a modificar: ").strip()
    
    # Buscar cliente
    cliente_encontrado = None
    for cliente in clientes:
        if cliente["id"] == id_modificar:
            cliente_encontrado = cliente
            break
    
    if not cliente_encontrado:
        print("❌ Cliente no encontrado.\n")
        return
    
    # Mostrar información actual del cliente
    print("\n📝 Cliente encontrado - Datos actuales:")
    print(f"1. ID: {cliente_encontrado['id']}")
    print(f"2. Empresa: {cliente_encontrado['empresa']}")
    print(f"3. Representante: {cliente_encontrado['representante']}")
    print(f"4. Correo: {cliente_encontrado['correo']}")
    print(f"5. Teléfono: {cliente_encontrado['telefono']}")
    print(f"Fecha Registro: {cliente_encontrado['fecha']}")
    
    # Menú de campos modificables
    while True: # FACILITA LA MODIFICACION DEL CLIENTE YA QUE PODEMOS ELEGIR CAMPO SOLICITADO
        print("\nSeleccione el campo a modificar:")
        print("[1] Nombre de la Empresa")
        print("[2] Representante Legal")
        print("[3] Correo Electrónico")
        print("[4] Teléfono")
        print("[5] Guardar cambios y salir")
        print("[6] Salir sin guardar")
        
        opcion = input("Opción: ").strip()
        
        if opcion == "1":  # Modificar empresa
            while True:
                nueva_empresa = input("Nuevo nombre de la Empresa: ").title()
                if validar_nombre(nueva_empresa):
                    cliente_encontrado["empresa"] = nueva_empresa
                    print("✅ Nombre de empresa actualizado.")
                    break
                print("❌ El nombre de la empresa solo debe contener letras y espacios.")
        
        elif opcion == "2":  # Modificar representante
            while True:
                nuevo_representante = input("Nuevo representante legal: ").title()
                if validar_nombre(nuevo_representante):
                    cliente_encontrado["representante"] = nuevo_representante
                    print("✅ Representante legal actualizado.")
                    break
                print("❌ El nombre del representante solo debe contener letras y espacios.")
        
        elif opcion == "3":  # Modificar correo
            while True:
                nuevo_correo = input("Nuevo correo: ").lower()
                if validar_correo(nuevo_correo):
                    cliente_encontrado["correo"] = nuevo_correo
                    print("✅ Correo electrónico actualizado.")
                    break
                print("❌ Correo inválido. Intenta nuevamente.")
        
        elif opcion == "4":  # Modificar teléfono
            while True:
                nuevo_telefono = input("Nuevo teléfono: ")
                if validar_telefono(nuevo_telefono):
                    cliente_encontrado["telefono"] = nuevo_telefono
                    print("✅ Teléfono actualizado.")
                    break
                print("❌ Teléfono inválido. Solo números, de 7 a 15 dígitos.")
        
        elif opcion == "5":  # Guardar cambios
            cliente_encontrado["fecha"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            print("✅ Cambios guardados exitosamente.\n")
            break
        
        elif opcion == "6":  # Salir sin guardar
            print("❎ Cambios descartados. Volviendo al menú anterior.\n")
            break
        
        else:
            print("❌ Opción inválida. Intente nuevamente.")
#=================================eliminar cliente en caso de que sea necesario
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

    # ==============================Mostrar información antes de confirmar
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
#================================menu para registrar cliente desde el admin
def registrar_cliente_admin():# esta funcion mantiene todo el CRUD ya que es de roll administrativo 
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
def registrar_cliente_vendedor(): #esta funcion solo mantiene estas 2 opciones ya presentadas 
    while True:                     #ya que es el vendedor 
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
#==================================================  CRUD GESTION DE PRODUCTOS   =======================================
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
    #    id_producto = input("ID del producto: ").strip()
    #    
    #    if not id_producto:
    #        print("El ID no puede estar vacío.")
    #    elif not id_producto.isalnum():
    #        print("El ID solo puede contener letras y números.")
    #    elif any(producto['id'] == id_producto for producto in productos):
    #        print("Este ID ya existe. Por favor, ingresa uno diferente.")
    #    else:
    #        id_valido = True
    
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

def modificar_producto(productos): # FACILITA LA MODIFICACION DEL PRDUCTO YA QUE PODEMOS ELEGIR CAMPO SOLICITADO
    print("\n==== Modificar Producto ====")
    
    # Validar que existan productos registrados
    if not productos:
        print("❌ No hay productos registrados para modificar.\n")
        return
    
    # Mostrar lista de productos disponibles
    print("\n📋 Lista de Productos Disponibles:")
    for producto in productos:
        print(f"ID: {producto['id']} | Nombre: {producto['nombre']} | Precio: ${producto['precio']:.2f}")
    
    # Solicitar ID del producto a modificar
    id_modificar = input("\nIngrese el ID del producto a modificar: ").strip()
    
    # Buscar producto
    producto_encontrado = None
    for producto in productos:
        if producto["id"] == id_modificar:
            producto_encontrado = producto
            break
    
    if not producto_encontrado:
        print("❌ Producto no encontrado.\n")
        return
    
    # Mostrar información actual del producto
    print("\n📝 Producto encontrado - Datos actuales:")
    print(f"1. ID: {producto_encontrado['id']}")
    print(f"2. Nombre: {producto_encontrado['nombre']}")
    print(f"3. Descripción: {producto_encontrado['descripcion']}")
    print(f"4. Precio: ${producto_encontrado['precio']:.2f}")
    print(f"Fecha Registro: {producto_encontrado['fecha']}")
    
    # Menú de campos modificables
    while True:
        print("\nSeleccione el campo a modificar:")
        print("[1] Nombre del Producto")
        print("[2] Descripción")
        print("[3] Precio")
        print("[4] Guardar cambios y salir")
        print("[5] Salir sin guardar")
        
        opcion = input("Opción: ").strip()
        
        if opcion == "1":  # Modificar nombre
            while True:
                nuevo_nombre = input("Nuevo nombre del producto: ").strip().title()
                if nuevo_nombre:
                    producto_encontrado["nombre"] = nuevo_nombre
                    print("✅ Nombre del producto actualizado.")
                    break
                print("❌ El nombre no puede estar vacío.")
        
        elif opcion == "2":  # Modificar descripción
            nueva_descripcion = input("Nueva descripción: ").strip()
            producto_encontrado["descripcion"] = nueva_descripcion
            print("✅ Descripción actualizada.")
        
        elif opcion == "3":  # Modificar precio
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
        
        elif opcion == "4":  # Guardar cambios
            producto_encontrado["fecha"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            print("✅ Cambios guardados exitosamente.\n")
            break
        
        elif opcion == "5":  # Salir sin guardar
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
                print("✅ Producto eliminado correctamente.")
            else:
                print("Operación cancelada.")
            return
    
    print(f"No se encontró producto con ID '{id_producto_eliminar}'.")

def registrar_pedido():
    # Validaciones iniciales
    if not productos:
        print("❌ No hay productos registrados.\n")
        return
    if not clientes:
        print("❌ No hay clientes registrados.\n")
        return

    # Buscar cliente
    print("\nClientes disponibles:")
    for cliente in clientes:
        print(f"ID: {cliente['id']} - {cliente['empresa']}")
    
    id_cliente = input("\nIngrese ID del cliente: ").strip()
    cliente_encontrado = next((c for c in clientes if c["id"] == id_cliente), None)
    
    if not cliente_encontrado:
        print("❌ Cliente no encontrado.\n")
        return

    # Buscar producto
    print("\nProductos disponibles:")
    for producto in productos:
        print(f"ID: {producto['id']} - {producto['nombre']} (${producto['precio']})")
    
    id_producto = input("\nIngrese ID del producto: ").strip()
    producto_encontrado = next((p for p in productos if p["id"] == id_producto), None)
    
    if not producto_encontrado:
        print("❌ Producto no encontrado.\n")
        return

    # Selección de talla y color
    print(f"\nTallas disponibles: {', '.join(tallas_disponibles)}")
    talla = input("Talla (ej. M): ").strip().upper()
    if talla not in tallas_disponibles:
        print("❌ Talla no disponible.\n")
        return

    print(f"\nColores disponibles: {', '.join(colores_disponibles)}")
    color = input("Color (ej. azul): ").strip().lower()
    if color not in colores_disponibles:
        print("❌ Color no disponible.\n")
        return

    # Cantidad
    try:
        cantidad = int(input("Cantidad: "))
        if cantidad <= 0:
            print("❌ La cantidad debe ser positiva.\n")
            return
    except ValueError:
        print("❌ Ingrese un número válido.\n")
        return

    # Cálculos
    precio_unitario = producto_encontrado["precio"]
    subtotal = cantidad * precio_unitario
    iva = subtotal * 0.19
    total = subtotal + iva

    # Crear pedido
    pedido = {
        "fecha": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "id_cliente": id_cliente,
        "cliente_nombre": cliente_encontrado["empresa"],
        "id_producto": id_producto,
        "producto_nombre": producto_encontrado["nombre"],
        "color": color,
        "talla": talla,
        "cantidad": cantidad,
        "precio_unitario": precio_unitario,
        "subtotal": subtotal,
        "iva": iva,
        "total": total
    }

    pedidos.append(pedido)
    print(f"\n✅ Pedido registrado (Total: ${total:.2f})\n")

def listar_pedidos():
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

def consultar_productos_disponibles():
    print("\n==== Productos Disponibles ====")
    if not productos:
        print("No hay productos registrados.")
        return
    
    for producto in productos:
        print(f"ID: {producto['id']} | {producto['nombre']:20} | Precio: ${producto['precio']:,}")

# ================== FLUJO PRINCIPAL ==================
def programa():#=======================================================================
    while True:
        resultado = menu_usuario()
        if resultado:
            rol, usuarios = resultado
            menu_principal(rol)
        else:
            print("Acceso denegado o máximo de intentos fallidos.")
            break

programa()

# ================== EJECUTAR ==================
