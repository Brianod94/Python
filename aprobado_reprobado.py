#Un alumno desea saber cuál será su calificación final en la materia de Algoritmos y si aprobó o no.
#  Dicha calificación se compone de los siguientes porcentajes:
	#55% del promedio de sus tres calificaciones parciales.
	#30% de la calificación del examen final.
	#15% de la calificación de un trabajo final
notas_paciales1=float(input("ingrese 1ra nota: = "))
notas_paciales2=float(input("ingrese 2da nota: = "))
notas_paciales3=float(input("ingrese 3ra nota: = "))   
examen_final=float(input("nota de examen final: = "))  #nota del examen final
trabajo_final=float(input("nota trabajo final: = "))   #nota del trabajo final
promedio_parcial=(notas_paciales1+notas_paciales2+notas_paciales3)/3 #sumatoria de la notas parciales
promedio_final=(promedio_parcial*0.55)	#
nota_exa_final=(examen_final*0.3)		#calificaciones con su respectivo porcentaje
notas_trab_fin=(trabajo_final*0.15)		#
calificacion_final=promedio_final+nota_exa_final+notas_trab_fin	#sumatoria de los porcentajes
if calificacion_final>3:
    print("has aprobado la materia")
else: 
    print("has reprobado la materia")
print("promedioparcial",promedio_parcial) 
print("promedio_final:",promedio_final)
print("examenfinal",nota_exa_final)
print("trabajofinal",notas_trab_fin)
print("tu calificacion final es: = ",calificacion_final)