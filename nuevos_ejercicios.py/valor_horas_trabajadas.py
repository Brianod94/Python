hras_trabajadas=int(input("ingrese cantidad de horas: "))
valor_horas=float(input("valor de la hora: "))
sueldo_bruto=valor_horas*hras_trabajadas
descuento=sueldo_bruto*0.1
salario_a_pagar=sueldo_bruto-descuento        
if sueldo_bruto<1800000:
    bono_transporte=105000
    print("su sueldo es: ",sueldo_bruto)
    print("descuento de renta es: ",descuento)
    print("salario a pagares: ",salario_a_pagar)
    print("tiene bono de transporte de: ",bono_transporte)
else:
    bono_transporte="no aplica bono transporte"
    print("su sueldo es: ",sueldo_bruto)
    print("descuento de renta es: ",descuento)
    print("salario a pagares: ",salario_a_pagar)
    print("tiene bono de transporte de: ",bono_transporte)

    

