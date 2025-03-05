boys=int(input("cantidad de niños: "))
girls=int(input("cantidad niñas: "))
total_estudiantes= boys+girls  #primero hallamos el totalde estudiantes
porcentaje_boys= boys/total_estudiantes*100  #luego hallamos el porcentaje de niños
porcentaje_gilrs= girls/total_estudiantes*100  #luego hallamos el porcentaje de niñas
print("porcentaje de niños: ", porcentaje_boys)
print("porcentaje de niñas: ", porcentaje_gilrs)
if porcentaje_boys>porcentaje_gilrs:            #comparamos los porcentajes y sacamos 
    print("HAY MAYORIA DE NIÑOS")               #la mayoria de niños y niñas o su igualdad
elif porcentaje_gilrs>porcentaje_boys:
    print("HAY MAYORIA DE NIÑAS")
else:   
    print("IGUAL CANTIDAD DE NIÑOS Y NIÑAS")  