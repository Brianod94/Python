#El ejercicio que resolvemos es:
#“Escribe un programa que, al recibir como dato un número entero positivo N, 
# calcule el resultado de la siguiente serie:
#1 + (1/2) + (1/3) + (1/4) + ... + (1/N)
#Si el usuario escribe un número incorrecto, el programa no se ejecuta. 
# En cambio, pregunta de nuevo por la información hasta que el dato ingresado sea correcto

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