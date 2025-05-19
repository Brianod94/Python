import re
#cree una lista de clientes para la simulacion 
clientes_registrados={
    '001': 'julio',
    '002': 'jesus',
    '003': 'santiago'}
#aqui creo una lista con las tallas y los colores disponibles
tallas_permitidas=['XS','S','M','L','XL','XXL','XXXL']
colores_permitidos=['azul', 'caqui', 'naranja']
#aqui seguiria la lista donde se guaran los pedidos
pedidos=[]
#esta es la funcion de generar codigo en secuencia
def generar_codigo_pedido():
    numero=len(pedidos)+1
    return f'PED{numero:03d}'
#aqui seria la funcion de registrar pedido 
def registrar_pedido():
    print('\n**** Registrar nuevo pedido ****')
    #aqui se validaria el id del cliente
    while True:
        id_empresa=input('Ingrese el ID del cliente:').strip().upper()
        if id_empresa in clientes_registrados:
            print(f'Empresa reconocida:{clientes_registrados[id_empresa]}')
            break
        else:
            print('ID del clieente no válido Intente nuevamente')
    #aqui se valida el tipo de prenda 
    while True:
        tipo_prenda=input('Ingrese el tipo de prenda (inifuga o dril):').strip().lower()
        if tipo_prenda in ['inifuga','dril']:
            break
        else:
            print('Tipo de prenda inválida Solo se acepta inifuga o dril')

    # este while seria para validar los colores disponibles
    while True:
        print(f'Colores disponibles: {', '.lower(colores_permitidos)}')
        color=input('Ingrese el color de la prenda:').strip().lower()
        if color in colores_permitidos:
            break
        else:
            print('Color no disponible. Intente nuevamente')

    #aqui estamos utilizando el while para validar las tallas
    while True:
        talla = input(f"Ingrese la talla ({'/'.join(tallas_permitidas)}): ").strip().upper()
        if talla in tallas_permitidas:
            break
        else:
            print("Talla inválida. Intente nuevamente.")