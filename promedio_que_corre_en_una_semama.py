lunes=float(input('tiempo recorrido lunes = '))
miecoles=float(input('tiempo recorrido miercoles = '))
viernes=float(input('tiempo recorrido viernes = '))
promedios_semanal=(lunes+miecoles+viernes)/3
print('promedio recorrido en la semana fue = ',f"{round(promedios_semanal)} minutos") #round funciona para redondear el resultado 
#5.	Todos los lunes, miércoles y viernes, una persona corre la misma ruta
#  y cronometra los tiempos obtenidos.
#  Determinar el tiempo promedio que la persona tarda en recorrer 
# la ruta en una semana cualquiera