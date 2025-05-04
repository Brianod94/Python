print("===='AVISOS INMEDIATOS'====")
numero_par=int(input("ingrese numero PAR. "))
if numero_par%2!=0:
    print("no ha escrito un numero PAR")
numero_impar=int(input("ingrese numero IMPAR. "))
if numero_impar%2==0:
    print("no ha escrito un numero IMPAR")
elif numero_par%2==0 and numero_impar%2!=0:
    print("!gracias por su colaboracion¡")
else:
    print("ejecute denuevo el programa")