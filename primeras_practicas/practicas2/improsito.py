print("tramos impositivos para declara renta")
name=("cual es su nombre: ")
renta_anual=float(input("cual es su renta anual: "))
if renta_anual < 10000000:
    renta_anual=renta_anual*0.5
    print("su improsito es el 5%",renta_anual)
elif renta_anual < 20000000:
    renta_anual=renta_anual*0.15
    print("su improsito es el 15%",renta_anual)
elif renta_anual < 35000000:
    renta_anual=renta_anual*0.20
    print("su improsito es el 20%",renta_anual)
elif renta_anual < 60000000:
    renta_anual=renta_anual*0.30
    print("su improsito es el 30%",renta_anual)
else:
    renta_anual=renta_anual*0.45
    print("su improsito es el 45%",renta_anual)
