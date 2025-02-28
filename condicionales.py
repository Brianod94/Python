valor_camisa=float(input("valor de la camisa: = "))
valor_uniforme=float(input("valor del uniforme: = "))
total_compra=valor_camisa+valor_uniforme
if total_compra>200000:
    print("tiene un descuento del 15%")
    total_descuento=total_compra*0.15
    print("el descuento es: = ",total_descuento)
    precio_final=total_compra-total_descuento
    print("valor a pagar con descuentoes: = ",precio_final)
else:
    print("no tiene descuento")