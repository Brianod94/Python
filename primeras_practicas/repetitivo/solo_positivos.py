print ("leer 10 numeros e imprimir solo los positivos ")

i=0
while i < 10:
    num=int(input(f"digite un numero {i+1}: "))
    if num > 0:
        print(f"{num} es positivo")
    i+=1
print()