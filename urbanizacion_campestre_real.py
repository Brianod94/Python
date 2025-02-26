valor_parcela=float(input("valor de la parcela: = "))
inicial_parcela=float(input("valor de la couta inicial: = "))
numeros_cuotas=float(input("ingrese total de cuotas: = "))
restante=valor_parcela-inicial_parcela
valor_final=valor_parcela+(restante*0.2)
valor_pagar_cuotas=valor_final/numeros_cuotas
print("valor total a pagar: = ",valor_final)
print("valor cuotas a pagar: = ",round(valor_pagar_cuotas))

