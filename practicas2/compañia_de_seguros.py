monto_asegurar=float(input("cual es el monto asegurar: "))
if monto_asegurar<=50000000:
    cuota_pagar=monto_asegurar*0.03
    
else:
    monto_asegurar>50000000
    cuota_pagar=monto_asegurar*0.02
print("la cuota a pagar es: ",cuota_pagar)
