#pedir un limite al usuario que sea positiva
limite = float(input("ingrese un valor limite: "))

#verifica quee el limite sea positivo
while limite <=0:
    print("El valor debe ser positivo.")
    limite = int(input("ingrese un valor limite: "))


#paso #"2" inicializar la suma en 0

suma=0

# paso 3 inicial el ciclo para pedir numeros hasta que la suma supere el limite
while suma <= limite:
    numero = int(input("ingrese un numero.\n"))
    suma += numero #sumamos el numero ingresado con la variable SUMA
    print(f"la suma actal es: {suma}")

#paso 4 cuando la suma supere el limite el buble se termina 

print("¡el limite ha sido superado!")