#Mensaje de bienvenida.
print("*****************************************************")
print("********🫡  Bienvenido a Pizza Bella Napoli 🍕**********\n\n")

opciones = 0

while opciones != "3":
    print("¿Ingrese numero del Tipo pizza que desea ordenar?\n")
    print("[1] Vegetariana. 🥬")
    print("[2] No vegetariana. 🍖")
    print("[3] Salir. 👋")
    print("\n*****************************************************\n")

    opciones = input("¿Opcion? = ")
    
    #desicion sobre el tipo de pizza 
    if opciones =="1":
        print("Ingrese el numero del ingrediente adicional\n\n[1] Pimiento🫑\n[2] Champiñon🍄‍🟫\n[3] Otro➕.")
        ingrediente=input("¿Opcion? = ")

        if  ingrediente=="1":
            print("\nUsted ordeno una pizza vegetariena con mozarella🧀, tomate🍅 y pimiento🫑\n")

        elif ingrediente=="2":
            print("\nUsted ordeno una pizza vegetariena con mozarella🧀, tomate🍅 y champiñon🍄‍🟫\n")

        elif ingrediente=="3":
            otro = input("Ingrese el ingrediente que desea agregar: ")
            print(f"\nUsted ordeno una pizza vegetariena con mozarella🧀, tomate🍅 y {otro}\n")

        else:
            print("\n!❌ERROR¡ ingrediente no encontrado\n")

    elif opciones =="2":
        print("Ingrese numero del ingrediente adiccional.\n[1] Peperoni🥓\n[2] Jamon🥩\n[3] Salmon🍣\n[4] Otro➕.")
        ingrediente = input("¿opcion? = ")

        if ingrediente=="1":
            print("\nUsted ordeno una pizza no vegetariena y es con mozarella🧀, tomate🍅 y peperoni🥓\n")
        
        elif ingrediente=="2":
            print("\nUsted ordeno una pizza no vegetariena y es con mozarella🧀, tomate🍅 y jamon🥩\n")
        
        elif ingrediente=="3":
            print("\nUsted ordeno una pizza no vegetariena y es con mozarella🧀, tomate🍅 y salmon🍣\n")

        elif ingrediente=="4":
            otro = input("Ingrese el ingrediente que desea agregar: ")
            print(f"\nUsted ordeno una pizza no vegetariena y es con mozarella🧀, tomate🍅 y {otro}\n")
        
        else:
            print("\n!❌ERROR¡ ingrediente no encontrado\n")

    elif opciones == "3": 
        print("¡Nos alegra que nos visitaran!🤗\n")
        print("GRACIAS POR SU VISITA VUELVA PRONTO😋")

    else:
        print("!❌ERROR¡ opcion no encontrada\n")
