#ejercicio 1
#escriba un programa que pida una palabra
####y la muestra por pantalla 10 veces

palabra=str(input("escriba una palabra "))
x=1
while x<11:
    print (palabra)
    x+=1

print("fin.")

# edades 
edad=int(input("cual es su edad: "))
x=0
while x < edad:
    x+=1 
    print(f"has cumplido {x} años")

# tablas de mltiplicar
tabla=int(input("ingrese tabla a multiplicar: "))
contador=0
while contador<=10:
    resultado = tabla*contador 
    print(tabla,"*",contador,"=",resultado )
    contador+=1