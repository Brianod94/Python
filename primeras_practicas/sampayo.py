contador = 0
notas = 0

while contador < 7:

    nota = int(input("ingrese nota del alumno: "))

    if nota < 0 or nota > 5:
        print("!ERROR¡ esta nota no esta permitida")
        continue  # con esto se salta la iteracion y no cuenta lo que esta abajo
    else:
        notas += nota
        contador += 1
        promedio = notas / 7

if promedio < 3:
    print(f"{round (promedio,2)} 'reprobado'")
else:
    print(f"{round (promedio,2)} 'aprobado'")

print(f"el promedio de las notas es {round(promedio,2)}")