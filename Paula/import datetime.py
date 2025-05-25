import datetime

def existe_id(productos, codigo):
    """Verifica si un ID ya existe en la lista de productos"""
    for producto in productos:
        if producto['id'] == codigo:
            return True
    return False

def existe_nombre(productos, nombre):
    """Verifica si un nombre de producto ya existe (insensible a mayúsculas)"""
    for producto in productos:
        if producto['nombre'].lower() == nombre.lower():
            return True
    return False

def generar_codigo_producto(productos):
    """Genera un código de producto único con formato PRO001, PRO002, etc."""
    numero = len(productos) + 1
    while True:
        codigo = f"PRO{numero:03d}"
        if not existe_id(productos, codigo):
            return codigo
        numero += 1

def agregar_producto(productos):
    print("\n==== Agregar Producto ====")
    
    # Generar ID único
    id_producto = generar_codigo_producto(productos)
    print(f"ID generado automáticamente: {id_producto}")

    # Validación del nombre
    nombre_valido = False
    while not nombre_valido:
        nombre_producto = input("Nombre del producto: ").strip().title()
        if nombre_producto:
            if existe_nombre(productos, nombre_producto):
                print("⚠️ Advertencia: Ya existe un producto con este nombre")
                confirmacion = input("¿Desea continuar de todos modos? (s/n): ").lower()
                if confirmacion == 's':
                    nombre_valido = True
            else:
                nombre_valido = True
        else:
            print("❌ Error: El nombre no puede estar vacío")

    # Resto del código se mantiene igual...
    descripcion_producto = input("Descripción: ").strip()

    # Validación del precio
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

    # Crear nuevo producto
    nuevo_producto = {
        "id": id_producto,
        "nombre": nombre_producto,
        "descripcion": descripcion_producto,
        "precio": precio_producto,
        "fecha": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }

    productos.append(nuevo_producto)
    print(f"\n✅ Producto '{nombre_producto}' agregado exitosamente!")
    print(f"ID: {id_producto} | Precio: ${precio_producto:.2f}\n")
    