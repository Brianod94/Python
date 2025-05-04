print("pagar impuestos si eres mayor de 18 años")
nombre=input("¿cual es su nombre?. = ")
edad=int(input("ingrese la edad. = "))
salario=int(input("cual es su salario mensual: = "))
if edad>18 and salario>=1600000:
    print("usted debe declarar renta")
else:
    print("no debe de declarar renta")
