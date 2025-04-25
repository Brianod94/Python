# Calcular e imprimir la tabla de multiplicar de un número cualquiera.
# Imprimir el multiplicando, el multiplicador y el
# producto. 
for i in range(1,11):
    print(f"la tabla de multiplicar: {i}\n")
    for j in range(1,11):
        resultado = i * j
        print(f"la tabla es: {i} x {j} = {resultado}")
        
    print("***************************************\n")
    
    