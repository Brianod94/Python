i=True
while i == True:
    uno=int(input("digite numeros enteros: "))
    dos=int(input("digite numeros enteros: "))
    tres=int(input("digite numeros enteros: "))
    cuatro=int(input("digite numeros enteros: "))
    if uno > dos and uno >tres and uno > cuatro:
        print(f"El numero mayor de los 4 es {uno}")
    elif dos > uno  and dos >tres and dos > cuatro:
        print(f"El numero mayor de los 4 es {dos}")
    elif tres > uno and tres > dos and tres > cuatro:
        print(f"El numero mayor de los 4 es {tres}")
    else:
        print(f"El numero mayor de los 4 es {cuatro}")
        