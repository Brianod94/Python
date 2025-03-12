numero_par=int(input("ingrese un numero que sea PAR. "))
numero_impar=int(input("ingrese un numero que sea IMPAR. "))
if numero_par%2!=0:
    print("este numero no es correcto debe ser PAR.")
    print("vuelo a intentar")
elif numero_impar%2==0:
    print("este numero no es correcto debe ser IMPAR.")
    print("que lo vuela intentar")
elif numero_par%2==0 and numero_impar%2!=0:
    print("gracias por su colaboracion")
else: 
    print("vuelo a intentar")