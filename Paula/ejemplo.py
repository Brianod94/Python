clientes=[]
materias_primas=[]
productos=[]
pedidos=[]
print("===REGISTRO DE CLIENTES===")
num_clientes=int(input("Ingrese cantidad de clientes: "))
for i in range(num_clientes):
    cliente=input(f"Ingrese nombre del cliente {i + 1}: ")
    print('el cliente es: ', cliente) 
