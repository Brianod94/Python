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


def buscar_posicion(numero, lista):
    if numero in lista:
        posicion = lista.index(numero)
        print(f"El número {numero} se encuentra en la posición {posicion} de la lista.")
    else:
        print("Error: El número no se encuentra en la lista.")

# Lista de ejemplo
mi_lista = [10, 20, 30, 40, 50]

# Leer número desde el teclado
try:
    numero_usuario = int(input("Ingrese un número: "))
    buscar_posicion(numero_usuario, mi_lista)
except ValueError:
    print("Error: Entrada no válida. Por favor, ingrese un número entero.")