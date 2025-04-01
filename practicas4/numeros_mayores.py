uno=float(input("escriba un numero: "))
dos=float(input(f"escriba un numero mayor que {uno}: "))
while uno < dos:
        dos=float(input(f"escriba otro numero mayor que {uno}: "))

print(f"{dos} no es mayor que {uno}.")