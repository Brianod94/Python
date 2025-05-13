def calcularIVA(p):
    iva = p* 0.19
    return iva 
p_compra=float(input("digte valor de la compra: "))
iva = calcularIVA(p_compra)
print(f"el valor de la compra sin IVA es {p_compra}")
print(f"el valor total a pagar es: {p_compra+iva}")
