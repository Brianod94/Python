j=True
while j==True:
    uno=int(input("que tabla desea saber es: "))
    if uno > 0:

        i=1
        while i < 11:
            print(f"{uno} x {i} = {uno*i}")
            i+=1
        
    else:
        print("el numero debe ser mayor que 0.")