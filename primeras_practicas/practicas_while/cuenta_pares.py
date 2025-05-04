numero=int(input("escriba un numero par: "))
while numero%2!=0:
    numero=int(input(f"{numero} no es par. vuelve a intentar. "))
i=1
pregunta=input("¿quieres escribir otro numero par? si o no: ")

while pregunta =="si" or pregunta == "SI":
    numero=int(input("escriba otro numero par: "))
    while numero%2!=0:
        numero=int(input(f"{numero} no es par. vuelve a intentar. "))
    i+=1
    pregunta=input("¿quieres escribir otro numero par? si o no: ")
print(f"has escrito {i} numero par.")