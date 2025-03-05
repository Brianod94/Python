print("1 curso se dividio en AyB deacuerdo a su nombre y sexo")
name=input("¿cual es su nombre?: ")
sexo=input("sexo ( M o F ) ")

if sexo=="M":
    if name > "n":
        grupo= "A"
    else:
        grupo= "B"
else:
    if name < "m":
        grupo= "A"
    else:
        grupo="B"
print("tu grupo es ",grupo)
