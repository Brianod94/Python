#promedio de 7 calificaciones de un alumno 
contador = 0
notas = 0
while contador < 7:
    nota=int(input("ingrese nota del alumno: "))
    while nota < 0 or nota > 5:
        print("!ERROR¡ esta nota no esta permitida")
        nota=int(input("ingrese nota del alumno: "))
    notas += nota
    contador +=1
promedio = notas /7
if promedio < 3:
    print(f"{round (promedio,2)} 'reprobado'")
else: 
    print(f"{round (promedio,2)} 'aprobado'")
print(f"el promedio de las notas es {round (promedio,2)}")