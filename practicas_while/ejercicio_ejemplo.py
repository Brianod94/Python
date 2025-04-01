num=int(input("digite un numero : "))
num2=int(input(f"digite un numero que sea mayor que {num} :"))
while num2 <= num:
    num2=int(input(f"{num2} no es mayor que {num}. intentalo de nuevo: "))


print(f"los numero que ha escrito son {num} y {num2}.")