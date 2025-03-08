#3 persona deciden invertirr su dinero para forma una empesa
#e invierten una cantidad distinta
#el algoritmo debe imprimir el nombre de las personas y
# el porcentaje que invierte con respecto al valor de la inversion
nombre1=input("nombre persona 1: ")
inversion1=float(input("inversion persona1: "))
nombre2=input("nombre persona 2: ")
inversion2=float(input("inversion persona2: "))
nombre3=input("nombre persona 3: ")
inversion3=float(input("inversion persona3: "))
#calculamos el valor total de la inversion
total_inversion=inversion1+inversion2+inversion3
#ahora sacamos el porcentaje de cada persona
porcentaje1=(inversion1/total_inversion)*100
porcentaje2=(inversion2/total_inversion)*100
porcentaje3=(inversion3/total_inversion)*100
#imprime los nombres de cada 1 de ellos
print("costo total de inversion fue: ",total_inversion)
print("su nombre es:", nombre1 +"su inversion fue de: ",porcentaje1)
print("su nombre es:", nombre2 +"su inversion fue de: ",porcentaje2)
print("su nombre es:", nombre3 +"su inversion fue de: ",porcentaje3)
