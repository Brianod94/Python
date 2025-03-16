# digitar el año actual y un año cualquiera 
#y que nos muestre cuantos años han pasado y cuantos año falta 
año1=int(input("año actual "))
año2=int(input("ingresa un año cualquiera: "))
if año1>año2:
    print(f"desde el año {año2}  han pasado {año1-año2} años")
elif año1<año2:
    print(f"para llegar al año {año2} faltan.{año2-año1} años ")
else:
    print("es el mismo año")