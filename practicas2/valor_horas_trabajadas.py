hras_trabajadas=int(input("ingrese cantidad de horas: "))
valor_horas=float(input("valor de la hora: "))
bono_transporte=140000
sueldo_bruto=valor_horas*hras_trabajadas
descuento=sueldo_bruto*0.1
salario_a_pagar=sueldo_bruto-descuento        
if sueldo_bruto<1800000:
    print("salario a pagares + bono: ",salario_a_pagar+bono_transporte)
else:
    print("salario a pagares: ",salario_a_pagar)
print("su sueldo es: ",sueldo_bruto)
print("descuento de renta es: ",descuento) 


    

