iva=0.19
valor_fijo=300000
kilometro1=1500
kilometro2=1000
kilometraje=float(input("kilometraje actual:"))
if kilometraje<=300:
    print("su valor a pagar es : ",valor_fijo)
    print("impuestos a pagar: ",(valor_fijo*iva))
    print("total a pagar es: ",(valor_fijo*iva)+valor_fijo)

elif kilometraje>300 and kilometraje < 1000:
    valor_1 = kilometro1*kilometraje
    print("su alquiler a pagar es de: ",valor_1)
    print("impuestos a pagar: ",(valor_1*iva))
    print("total a pagar es: ",(valor_1*iva)+valor_1)

else:
    kilometraje>1000
    valor_2 = (kilometro2+kilometro1)*kilometraje
    print("su alquiler a pagar es de: ",valor_2)
    print("impuestos a pagar: ",(valor_2*iva))
    print("total a pagar: ",(valor_2*iva+valor_2))


    