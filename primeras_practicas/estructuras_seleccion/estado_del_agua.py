estado = True
while estado == True:
    agua=int(input("¿cual es la temperatura del agua? "))
    if agua < 0:
        print("estado solido 'congelado'")
    elif agua < 100:
        print("estado liquido")
    else:
        print("estado gas 'vapor'")