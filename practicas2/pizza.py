while True:
    print("*****************************************************")
    print("**********Bienvenido a Pizza Bella Napoli************")
    print("¿Ingrese numero del Tipo pizza que desea ordenar?")# \n1. vegetariana\n2. No vegetariana\n3. Salir")
    print("[1] Vegetariana.")
    print("[2] No vegetariana.")
    print("[3] Salir")
    print("*****************************************************")
    tipo= input("¿opcion? = ")
    
    
    #desicion sobre el tipo de pizza 
    if tipo =="1":
        print("ingrese el numero del ingrediente adicional\n[1] pimiento\n[2] tufo")
        ingrediente=input("¿opcion? = ")
        if  ingrediente=="1":
            print("\nustep ordeno una pizza vegetariena con mozarella,tomate y pimiento\n")
        elif ingrediente=="2":
            print("\nustep ordeno una pizza vegetariena con mozarella,tomate y tofu\n")
        else:
            print("\n!ERROR¡ ingrediente no encontrado\n")

    elif tipo =="2":
        print("ingrese numero del ingrediente adiccional.\n[1] Peperoni\n[2] Jamon\n[3] Salmon")
        ingrediente = input("¿opcion? = ")
        if ingrediente=="1":
            print("\nustep ordeno una pizza no vegetariena y es con mozarella,tomate y peperoni\n")
        elif ingrediente=="2":
            print("\nustep ordeno una pizza no vegetariena y es con mozarella,tomate y jamon\n")
        elif ingrediente=="3":
            print("\nustep ordeno una pizza no vegetariena y es con mozarella,tomate y salmon\n")
        else:
            print("\n!ERROR¡ ingrediente no encontrado\n")
        
    else:
        print ("esta opcion no esta disponible")

    