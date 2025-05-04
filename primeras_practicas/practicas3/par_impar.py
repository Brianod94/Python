#Escriba un programa que pida primero un número par y luego un número impar 
# (positivos o negativos). En caso de que uno o los dos valores no sea 
# correcto, se mostrará un único aviso
print("===='AVISO UNICO'====")
print("ingrese un numero PAR E IMPAR.\n(positivo o negativo)")
numero_par=int(input("ingrese un numero que sea PAR. "))
numero_impar=int(input("ingrese un numero que sea IMPAR. "))
if numero_par%2==0 and numero_impar%2!=0:
    print("¡gracias por su colaboracion!")
else:
    print("uno o mas valores que ha escrito no son correctos.")
    print("ejecute denuevo el programa.")