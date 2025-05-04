print("evaluacio final empleado")
print("los niveles son:")
print("inaceptable")
print("aceptable")
print("excelente")
nivel=float(input("cual es el nivel: "))
salario=int(input("valor salario: "))
if nivel==0:
    bono= 0
    print("su evaluacion es: inaceptable")
elif nivel==0.5:
    bono=salario*nivel
    print("su evaluacion es: aceptable")
elif nivel==1:
    bono=salario*nivel
    print("su evaluacion es: Excelente")
else:
    print("!Error¡nivel no especifico")
print("el bono a recibir es: ",bono)