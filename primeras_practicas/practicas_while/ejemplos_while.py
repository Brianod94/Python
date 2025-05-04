cambio =  True
while cambio == True:

    n=int(input("digite un numero entero positivo: "))

    if n > 0:

        cambio = False 
        resultado=0 
        i=1

        while i <= n:
        
            resultado += (1/i) 
            i += 1
        print(f"el resultado de la serie es: {resultado}" )

    else: 
        print("!ERROR¡ el numero debe ser positivo, vuelve a intentar. ")