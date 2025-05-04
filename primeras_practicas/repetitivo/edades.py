#promedio de edades de 10 alumnos 
contador = 0
edades = 0
while contador < 10:
    edad=int(input(f"ingrese la edad del alumno # {contador+1}: "))
    edades += edad
    contador +=1
promedio = edades /10
print(f"el promedio de edades es {promedio}")