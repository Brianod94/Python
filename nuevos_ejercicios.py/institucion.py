valor_hora=35000
ahorro_empleado=0.05
horas_trabajadas=int(input("cantidad de horas: "))
#multiplicamos el numero de horas por el valor
valor_pagar=horas_trabajadas*valor_hora
#al valor total le sacamos el 0.05 
# para saber cuanto es su ahorro
valor_ahorrado=valor_pagar*ahorro_empleado
print("total a pagar es: ",valor_pagar)
print("su ahorro es de: ",valor_ahorrado)