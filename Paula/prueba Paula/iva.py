import re
#cree una lista de clientes para la simulación 
clientes_registrados = {
    "001": "julio",
    "002": "jesus",
    "003": "santiago"
}
#aqui creo una lista con las tallas y los colores disponibles
tallas_disponibles = ["XS", "S", "M", "L", "XL", "XXL", "XXXL"]
colores_disponibles = ["azul", "caqui", "naranja"]
#esta seria la lista para guardar los  pedidos
pedidos = []
#esta es la funcion de generar codigo en secuencia  
def generar_codigo_pedido():
    numero = len(pedidos) + 1
    return f"PED{numero:03d}"
#aqui seria la funcion de registrar pedido 
def registrar_pedido():
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
#este seria el menu para registrar un pedido
def menu():
    while True:
        print("\n=== MENÚ PRINCIPAL ===")
        print("1. Registrar nuevo pedido")
        print("2. Salir")
        opcion = input("Seleccione una opción: ").strip()
        if opcion == "1":
            registrar_pedido()
        elif opcion == "2":
            print("Saliendo del programa ¡Hasta luego!")
            break
        else:
            print("Opción no válida intente de nuevo")
menu()
