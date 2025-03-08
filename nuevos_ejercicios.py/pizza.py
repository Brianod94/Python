print("Bienvenido a Pizza Bella Napoli")
print("¿Ingrese numero del Tipo pizza que desea ordenar?\n1. vegetariana\n2. No vegetariana.")
tipo= input("¿opcion? = ")
#desicion sobre el tipo de pizza 
if tipo =="1":
    print("ingrese el numero del ingrediente adicional\n1. pimiento\n2. tufo")
    ingrediente=input("numero = ")
    if  ingrediente=="1":
        print("ustep ordeno una pizza vegetariena con mozarella,tomate y pimiento")
    elif ingrediente=="2":
        print("ustep ordeno una pizza vegetariena con mozarella,tomate y tofu")
    else:
        print("este ingrediente no esta disponible")
elif tipo =="2":
    print("ingrese numero del ingrediente adiccional.\n1. Peperoni\n2. Jamon\n3. Salmon")
    ingrediente = input("¿opcion? = ")
    if ingrediente=="1":
        print("ustep ordeno una pizza no vegetariena y es con mozarella,tomate y peperoni")
    elif ingrediente=="2":
        print("ustep ordeno una pizza no vegetariena y es con mozarella,tomate y jamon")
    elif ingrediente=="3":
        print("ustep ordeno una pizza no vegetariena y es con mozarella,tomate y salmon")
    else:
        print("ese ingrediente no esta disponible")
else:
    print("ese producto no se encuentra")