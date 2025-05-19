productos = [] 
contador = 0


# funcion para crear codigos automaticos
def generar_codigo():
    global contador
    contador += 1
    return f'P{contador:05d}'

def registrar_producto():
    print('\n--- Ingresar Nuevo Producto ---')
    nombre = input('\nNombre del producto: ')
    talla = input('Talla del producto (ej: XS, S, M, L, XL, XXL, XXXL): ')
    color = input('Color del Producto (ej: Rojo,Azul,Verde): ')
    while True:
        try:
            precio = int(input('Precio del producto: '))
            if precio <= 0:
                print('El precio debe ser mayor que 0')
                continue
            break
        except ValueError:
            print('Por favor ingrese un número válido para el precio')

    codigo = generar_codigo()
    producto = {
        'codigo': codigo,
        'nombre': nombre,
        'talla' : talla,
        'color' : color,
        'precio': precio
    }
    productos.append(producto)
    print(f'\n Producto agregado con código {codigo}')
    return producto

def mostrar_productos():
    print('\n--- Lista de Productos ---')
    if not productos:
        print('No hay productos registrados')
        return
    
    for producto in productos:
        print(f' \n | Código: {producto['codigo']} \n | Nombre: {producto['nombre']} \n | Talla: {producto['talla']} \n | Color: {producto['color']} \n | Precio: ${producto['precio']:,}')

def menu_principal():
    while True:
        print('\n=== CREAR PRODUCTO ===')
        print('\n[1] Registrar producto')
        print('[2] Mostrar Producto')
        print('[3] Salir')
        
        opcion = input('\nSeleccione una opción: ')
        
        if opcion == '1':
            registrar_producto()
        elif opcion == '2':
            mostrar_productos()
        elif opcion == '3':
            print('Saliendo del sistema...')
            break
        else:
            print('Opción no válida. Por favor seleccione 1, 2 o 3')

menu_principal()