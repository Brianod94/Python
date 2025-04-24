#Al cerrar un expendio de naranjas, 15 clientes que aun no han pagado recibirán un 15% de descuento si compran
#más de 10 kilos. Determinar cuanto pagara cada cliente y cuanto percibirá la tienda por esas compras
i = 0
suma = 0
valor_naranja = 2000 #este valor es por kilos
while i < 15:
    kilos=int(input(f"cuantos kilos de naranja lleva el cliente #{i+1}:\n "))
    if kilos <= 10: #si la compra es menor o igual a 10 no aplicara para descuento 
        total = valor_naranja * kilos
       
    else: 
        kilos > 10 # si supero los 10 kilos se le aplicara el 15% de descuento 
        valor = valor_naranja * kilos
        descuento = valor*0.15
        total = valor - descuento  # aqui aplicamos un 15% de descuento sobre el valor de la compra final 

    print(f"valor total a pagar es {total}\n================================")
    suma += total 
    i+=1
print (f"total ventas de la tienda: {suma}")
