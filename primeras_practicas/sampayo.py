def llenar_lista():
    """Llena una lista con 5 números ingresados por el usuario."""
    lista = []
    for i in range(5):
        numero = float(input(f"Ingrese el número {i+1}: "))
        lista.append(numero)
    return lista

def encontrar_mayor(lista):
    """Imprime la posición y el valor del elemento mayor en la lista."""
    mayor = lista[0]
    posicion = 0
    for i in range(1, len(lista)):
        if lista[i] > mayor:
            mayor = lista[i]
            posicion = i
    print(f"El valor mayor es {mayor} y se encuentra en la posición {posicion}.")

# Ejemplo de uso
mi_lista = llenar_lista()
encontrar_mayor(mi_lista)