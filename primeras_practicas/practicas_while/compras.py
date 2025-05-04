salir = 1
total_cantidad=0
while salir== 1:

    valor = int(input("digite el valor del articulo:\n"))
    cantidad = int(input("cantidad de articulos:\n"))
    
    total_cantidad = total_cantidad+(valor*cantidad)
    print(f"acumulado. {total_cantidad}\n")

    salir=int(input("¿desea seguir comprando?.\n1. si\n2. no\n!opcion¡: ")) 
    if salir==2:
        print(f"total compra es: {total_cantidad}")
    