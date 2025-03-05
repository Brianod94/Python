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
    print("el bono a recibir es: ",bono)
elif nivel==0.5:
    bono=salario*nivel
    print("su evaluacion es: aceptable")
    print("el bono a recibir es:  ",bono)
elif nivel==1:
    bono=salario*nivel
    print("su evaluacion es: Excelente")
    print("el bono a recibir es: ",bono)
else:
    print("!Error¡nivel no especifico")
    

    
