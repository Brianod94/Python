primero=int(input("escriba un numero: "))
segundo=int(input(f"escriba un numero mayor que {primero}: "))

while segundo<=primero:
    
    segundo=int(input(f"{segundo} no es mayor que {primero} intentalo de nuevo: "))

tercero=int(input(f"escriba un numero entre {primero} y {segundo}. "))
i=0
while tercero> primero and tercero < segundo:
    i+=1
    tercero=int(input(f"escriba otro numero entre {primero} y {segundo}. "))
    
if i ==0:
    print (f"no ha escrito ningun numero entre {primero} y {segundo}")

else:
    print(f"ha escrito {i} entre {primero} y {segundo}. ")
