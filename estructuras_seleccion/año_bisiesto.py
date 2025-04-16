print("cual es un año bisiesto")
bisiesto=True
while bisiesto == True:
    year=int(input("ingrese un año: "))
    if year % 4 == 0 and year % 100 != 0 or year % 400==0:
        print("el año es bisiesto")
    else:
        print("el año es comun")