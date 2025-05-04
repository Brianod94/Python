#Escriba un programa que pida primero un número par (positivo o negativo)
#  y si el valor no es correcto, muestre un aviso. 
# Si el valor es correcto, pedirá un número impar (positivo o negativo)
#  y si el valor no es correcto, mostrará un aviso.
print("===='AVISO INMEDIATO'====")
numero_par=int(input("ingrese un numero que sea PAR. "))
if numero_par%2!=0:
    print("¡NO HA ESCIRO UN NUMER PAR CORRECTO!")
    print("EJECUTE DENUEVO EL PROGRAMA PARA VOLVER A INTENTARLO")
else:
    numero_impar=int(input("ingrese un numero que sea IMPAR. "))
    if numero_impar%2==0:
        print("¡NO HA ESCRITO UN NUMERO IMPAR CORRECTO!")
        print("EJECUTE DENUEVO EL PROGRAMA PARA VOLVER A INTENTARLO")
    else:
        print("gracias por su colaboracion")
