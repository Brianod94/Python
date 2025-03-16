print("===='AVISOS FINALES'====")
numero_par=int(input("ingrese un numero que sea PAR. "))
numero_impar=int(input("ingrese un numero que sea IMPAR. "))
if numero_par%2!=0:
    print("este numero no es correcto debe ser PAR.")
if numero_impar%2==0:
    print("este numero no es correcto debe ser IMPAR.")   
if numero_par%2==0 and numero_impar%2!=0:
    print("¡gracias por su colaboracion!")
else: 
    print("ejecute de nuevo el programa para volver a intentar")