# digitar el año actual y un año cualquiera 
#y que nos muestre cuantos años han pasado y cuantos año falta 
año1=int(input("¿en que año actual?"))
año2=int(input("ingresa un año cualquiera"))
diferencia= año1-año2
if diferencia>0:
    print("falta ", diferencia +"años para llegar",año2)
elif diferencia<0:
    print("han pasado", diferencia + "años desde el año.",año2)
else:
    print("es el mismo año")