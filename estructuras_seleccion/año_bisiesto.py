print("cual es un año bisiesto")
bisiesto=True
while bisiesto == True:
    year=int(input("ingrese un año: "))
    if year % 4 == 0 and year % 100 != 0 or year % 400==0:
        print("el año es bisiesto")
    else:
        print("el año es comun")

year1=int(input('ingrese primer year:'))
year2=int(input ('ingrese segundo year:'))
contador=0
for year in range(year1, year2, 1):
    
    if (year % 4 == 0 and year % 100 != 0) or (year % 400== 0):
        #print('es biciesto')
        contador+=1
    #print(f"iterable{i}")
   
print (contador)
