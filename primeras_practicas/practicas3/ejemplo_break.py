#ejemplo para break
print("while con sentencia break \n")
contador = 0
while contador < 10:
    contador +=1

    if contador == 5:
        break
    print("valor actual de la variable: ", contador)

print("fin del programa, la sentancia break se ha ejecutado.")


#ejemplo para continue

print("\nwhile con sentencia break \n")
contador = 0
while contador < 10:
    contador +=1   #incrementa el contador de 1 en 1 

    if contador == 5:
        continue
    print("valor actual de la variable: ", contador)
