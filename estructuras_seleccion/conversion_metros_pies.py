#conversor de metros s pies y de pies a metros
print("conversion de metros a pies y de pies a metros")
print("ingrese el tipo de conversion.")
print("[1] metros a pies. ")
print("[2] pies a metros. ")
metro, pies = 1 , 3.28084
tipo = int(input("¡opcion! = "))
if tipo == 1:
    metro1 = int(input("Metros > pies:\n"))
    metro1 = metro1 * pies
    print(f"la cantidad de pies son {round (metro1, 5)}")
elif tipo == 2: 
    pies1 = float(input("pies > metros:\n")) 
    pies1 =  pies1 / pies
    print(f"la cantidad de metros es {round (pies1, 4) }")
else:
    print("Opcion no disponible")