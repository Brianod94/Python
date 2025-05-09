def calificaciones(nota1,nota2,nota3):
    return(nota1*0.3)+(nota2*0.3)+(nota3*0.4)


nota1=float(input("digite 1ar nota: "))
nota2=float(input("digite 2da nota: "))
nota3=float(input("digite 3ra nota: "))

nota_final= calificaciones(nota1,nota2,nota3)
print(f"la nota final del Estudiante es: {nota_final:.3}")
if nota_final > 3:
    print("Aprobado")

else:
    print("Reprobado")

