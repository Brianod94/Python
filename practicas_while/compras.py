salir = False
total_catidad=0
while salir== False:

    valor = int(input("digite el valor del articulo:\n"))
    
    cantidad = int(input("cantidad de articulos:\n"))
    
    total_catidad = total_catidad+(valor*cantidad)
    print(f"acumulado. {total_catidad}\n")

    pregunta=int(input("¿desea seguir comprando?.\n1. si\n2. no\n!opcion¡: ")) 
    if pregunta==2: 
        salir=True
print(f"total compra es: {total_catidad}")   