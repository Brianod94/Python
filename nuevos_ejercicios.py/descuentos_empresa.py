Seguridad_social=0.08
Ahorro_empleados=0.05
Fondo_solidaridad=0.01
Salario_basico=float(input("ingrese el salario basico : "))
#calcular los descuentos sobre el valor del salario basico
descuento1=Salario_basico*Seguridad_social
descuento2=Salario_basico*Ahorro_empleados
descuento3=Salario_basico*Fondo_solidaridad
Total_descuento=descuento1+descuento2+descuento3
Salario_pagar=Salario_basico-Total_descuento
print("salario a pagar es: ", Salario_pagar)
