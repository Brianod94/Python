print("formula para saber si es un triangulo")
long_a = float(input("ingrese la longitud del lado a: "))
long_b = float(input("ingrese la longitud del lado b: "))  
long_c = float(input("ingrese la longitud del lado c: "))
if long_a + long_b > long_c and long_a + long_c > long_b and long_b + long_c > long_a:
    print("es un triangulo")
else:
    print("no es un triangulo")             