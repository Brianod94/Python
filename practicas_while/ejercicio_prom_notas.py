total_estudiantes = 30
contador = 0
aprobados = 0
reprobados = 0
suma_apro = 0
suma_repro = 0
suma_total = 0
#se inicia el ciclo para pedir ñas notas de los 30 estudiantes
print("Nota calificatoria es de '0.0' a '0.5'")
while contador < total_estudiantes:
    nota = float(input("ingrese la nota del estudiante: "))
    contador += 1

    while nota < 0.0 or nota > 5.0:
        print("¡ERROR! debe ingresar una nota valida. ")
        print("Nota calificatoria es de '0.0' a '0.5'")
        
        nota= float(input("ingrese nuevamente la nota del estudiante: "))
        contador += 1

        suma_total += nota

        if nota>=3.0:
            print("'aprobado'")
            aprobados += 1
        else:
            print("'reprobados'")
            reprobados += 1

        contador += 1 
    promedio_aprobados = suma_apro / aprobados if aprobados > 0 else 0
    promedio_reprobados = suma_repro / reprobados if reprobados > 0 else 0
    promedio_general = suma_total / total_estudiantes

    print("\nResultados del curso:")
    print(f"Cantidad de estudiantes aprobados: {aprobados}")
    print(f"Cantidad de estudiantes reprobados: {reprobados}")
    print(f"Promedio de los estudiantes aprobados: {promedio_aprobados:.2f}")
    print(f"Promedio de los estudiantes reprobados: {promedio_reprobados:.2f}")
    print(f"Promedio general del curso: {promedio_general:.2f}")
