numeros=[1,2,3,4,5,6,7,8,9]
numeros.append(10)
numeros.extend(["B","r","i","a","n"])
# numeros.pop(0)
print("esta lista contiene ",len(numeros)," elementos")
for i in range (0, len(numeros)):
    print(numeros[i],end =", ")
