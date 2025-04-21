num=int(input("digite un numero: "))
while num <= 0:
    print("el numero debe ser mayor que '0'")
    num=int(input("digite un numero: "))
num2=int(input("digite otro numero: "))
suma= num+num2
rest= num-num2
mult= num*num2
print(f"la suma de {suma}\nla resta es {rest}\nproducto es {mult}")


