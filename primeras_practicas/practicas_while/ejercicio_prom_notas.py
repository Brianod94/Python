total_estudiantes = 4
contador = 0
aprobados = 0   #
reprobados = 0
suma_apro = 0
suma_repro = 0
suma_total = 0
#se inicia el ciclo para pedir ñas notas de los 30 estudiantes
print("Nota calificatoria es de '0.0' a '5.0'")
while contador < total_estudiantes:
    nota = float(input("ingrese la nota del estudiante: "))
    if nota < 0.0 or nota > 5.0:
         print("¡ERROR! debe ingresar una nota valida. ")
         print("Nota calificatoria es de '0.0' a '5.0'")
    else:

        if nota>=3.0:
            print("'aprobado'")
            aprobados += 1
            suma_apro=suma_apro+nota

        else:
            print("'reprobados'")
            reprobados += 1
            suma_repro=suma_repro+nota

        contador += 1 
        suma_total= (suma_apro+suma_repro)/total_estudiantes
print(f"total de estudiantes es: {total_estudiantes}")
print(f"total de aprobados {aprobados}")
print(f"total reprobados es: {reprobados}")
if aprobados!=0:
    print(f"promedio de aprobados {round(suma_apro/aprobados,2)}")
if reprobados!=0:
    print(f"promedio de reprobados {round(suma_repro/reprobados,2)}")
print(f"promedio total curso es: {suma_total}")