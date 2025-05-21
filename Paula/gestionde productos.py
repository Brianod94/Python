from datetime import datetime

# Lista global para almacenar productos
productos = []

# ===== Funciones para gestionar productos =====

def agregar_producto(productos):
    print("\n==== Agregar Producto ====")
    id_producto = input("ID del producto: ").strip()

    # Verificar que el ID no exista
    for p in productos:
        if p['id'] == id_producto:
            print("❌ Error: El ID ingresado ya existe.\n")
            return

    nombre = input("Nombre del producto: ").strip().title()
    descripcion = input("Descripción: ").strip()

    # Validar precio
    while True:
        precio_input = input("Precio: ").strip()
        try:
            precio = float(precio_input)
            if precio < 0:
                print("❌ El precio no puede ser negativo.")
            else:
                break
        except ValueError:
            print("❌ Debe ingresar un número válido para el precio.")

    # Validar stock
    while True:
        stock_input = input("Cantidad en stock: ").strip()
        if stock_input.isdigit():
            stock = int(stock_input)
            break
        else:
            print("❌ Debe ingresar un número entero válido para el stock.")

    producto = {
        "id": id_producto,
        "nombre": nombre,
        "descripcion": descripcion,
        "precio": precio,
        "stock": stock,
        "fecha": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }

    productos.append(producto)
    print(f"✅ Producto '{nombre}' agregado exitosamente.\n")

def consultar_productos(productos):
    print("\n==== Consultar Productos ====")
    buscar = input("Ingrese ID o nombre del producto para buscar (deje vacío para ver todos): ").strip().lower()

    encontrados = []

    if buscar == "":
        encontrados = productos[:]  # Copia todos los productos
    else:
        for p in productos:
            if buscar in p["id"].lower() or buscar in p["nombre"].lower():
                encontrados.append(p)

    if encontrados:
        print(f"\n✅ Se encontraron {len(encontrados)} producto(s):\n")
        for p in encontrados:
            print("="*40)
            print(f"ID: {p['id']}")
            print(f"Nombre: {p['nombre']}")
            print(f"Descripción: {p['descripcion']}")
            print(f"Precio: ${p['precio']:.2f}")
            print(f"Stock: {p['stock']}")
            print(f"Fecha Registro: {p['fecha']}")
    else:
        print("❌ No se encontraron productos con ese criterio.\n")

def modificar_producto(productos):
    print("\n==== Modificar Producto ====")
    id_buscar = input("Ingrese el ID del producto a modificar: ").strip()

    producto_encontrado = None
    for p in productos:
        if p["id"] == id_buscar:
            producto_encontrado = p
            break

    if not producto_encontrado:
        print("❌ Producto no encontrado.\n")
        return

    print(f"\n✏️ Modificando producto '{producto_encontrado['nombre']}'")

    nuevo_nombre = input(f"Nombre [{producto_encontrado['nombre']}]: ").strip().title()
    if nuevo_nombre:
        producto_encontrado['nombre'] = nuevo_nombre

    nueva_descripcion = input(f"Descripción [{producto_encontrado['descripcion']}]: ").strip()
    if nueva_descripcion:
        producto_encontrado['descripcion'] = nueva_descripcion

    # Modificar precio
    while True:
        nuevo_precio = input(f"Precio [{producto_encontrado['precio']}]: ").strip()
        if nuevo_precio == "":
            break
        try:
            precio_valor = float(nuevo_precio)
            if precio_valor < 0:
                print("❌ El precio no puede ser negativo.")
            else:
                producto_encontrado['precio'] = precio_valor
                break
        except ValueError:
            print("❌ Debe ingresar un número válido para el precio.")

    # Modificar stock
    while True:
        nuevo_stock = input(f"Stock [{producto_encontrado['stock']}]: ").strip()
        if nuevo_stock == "":
            break
        if nuevo_stock.isdigit():
            producto_encontrado['stock'] = int(nuevo_stock)
            break
        else:
            print("❌ Debe ingresar un número entero válido para el stock.")

    print("✅ Producto modificado exitosamente.\n")

def eliminar_producto(productos):
    print("\n==== Eliminar Producto ====")
    id_eliminar = input("Ingrese el ID del producto a eliminar: ").strip()

    producto_encontrado = None
    for p in productos:
        if p["id"] == id_eliminar:
            producto_encontrado = p
            break

    if not producto_encontrado:
        print("❌ Producto no encontrado.\n")
        return

    print("\n🗂️ Producto encontrado:")
    print(f"ID: {producto_encontrado['id']}")
    print(f"Nombre: {producto_encontrado['nombre']}")
    print(f"Descripción: {producto_encontrado['descripcion']}")
    print(f"Precio: ${producto_encontrado['precio']:.2f}")
    print(f"Stock: {producto_encontrado['stock']}")
    print(f"Fecha Registro: {producto_encontrado['fecha']}")

    confirmacion = input("\n¿Está seguro que desea eliminar este producto? (s/n): ").lower()
    if confirmacion == 's':
        productos.remove(producto_encontrado)
        print("✅ Producto eliminado exitosamente.\n")
    else:
        print("❎ Operación cancelada. No se eliminó ningún producto.\n")

# ===== Menú para Producción =====

def gestion_productos_produccion():
    while True:
        print("\n===== Menú de Gestión de Productos (Producción) =====")
        print("[1] Agregar producto")
        print("[2] Modificar producto")
        print("[3] Eliminar producto")
        print("[4] Consultar productos")
        print("[5] Salir")
        print("=====================================================")

        opcion = input("Seleccione una opción: ").strip()

        if opcion == "1":
            agregar_producto(productos)

        elif opcion == "2":
            modificar_producto(productos)

        elif opcion == "3":
            eliminar_producto(productos)

        elif opcion == "4":
            consultar_productos(productos)

        elif opcion == "5":
            print("🔙 Volviendo al menú anterior...\n")
            break

        else:
            print("❌ Opción inválida. Intente nuevamente.\n")

# Para probar el menú directamente:
if __name__ == "__main__":
    gestion_productos_produccion()
