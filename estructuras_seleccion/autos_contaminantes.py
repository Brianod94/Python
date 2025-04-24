#En un centro de verificación de automóviles se desea saber el promedio de puntos contaminantes de los primeros
#25 automóviles que lleguen. Asimismo se desea saber los puntos contaminantes del carro que menos contaminó y
#del que más contaminó. 
maximo = 0
minimo = 1000

for i in range (1,6):
    cantidad_p_cont = int (input(f"digite cantidad de puntos contaminantes del vehiculo {i}. ")) #cantidad de puntos contaminantes
    promedio = cantidad_p_cont/5
    if cantidad_p_cont > maximo:
        maximo = cantidad_p_cont
    if cantidad_p_cont < minimo:
        minimo = cantidad_p_cont
   

print(f"el valor maximo es: {maximo}")
print(f"el valor minimo es: {minimo}")
print(f"el promedio es: {promedio}")
    

   
