uno=int(input("escriba un numero: "))
dos=int(input(f"escriba un numero mayor que {uno}: "))

while dos > uno:
    uno=dos
    dos=int(input(f"escriba un numero mayor que {uno}: "))

print(f"{dos} no es mayor que {uno}")