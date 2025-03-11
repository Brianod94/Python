print("valores para declara renta")
v_salario=int(input("¿cual es su salario?.= "))
if v_salario<390:
    paga=v_salario
elif v_salario<650:
    paga=v_salario*0.10
else:
    paga=v_salario*0.15
print("su renta es: ",(paga))
