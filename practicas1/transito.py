indice=input("indique 'si' o 'no' es positivo el indice de alcohol: ")
if indice== 'si':
    tipo_vehiculo=int(input("que tipo de vehiculo tiene:\n1. A.PARTICULAR\n2. t.publico\n3. CAMIONES\n"))
    if tipo_vehiculo==1:
        print("su grado de alcohol es 0,25. ")
    elif tipo_vehiculo==2:
        print("su grado de alcohol es 0,23. ")
    elif tipo_vehiculo==3:
     print("su grado de alcohol es 0,2. ")
    else:
        print("tipo de vehiculo no encontrado")
else:
        print("negativo")
    
