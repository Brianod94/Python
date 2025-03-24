
altura = float(input("¿cuanto mide en metros?. "))
peso = float(input("¿cual es su peso actual?. "))


masa_corporal = peso/altura**2

if masa_corporal< 18.5:
    print(f"BAJO DE PESO. {round(masa_corporal,2)}")
    
elif masa_corporal < 24.9:
    print(f"NORMAL. {round(masa_corporal,2)}")
elif masa_corporal <29.9:
    print(f"SOBREPESO. {round(masa_corporal,2)} ")
elif masa_corporal < 34.9:
    print(f"OBESIDAD LEVE. {round(masa_corporal,2)}")
elif masa_corporal < 39.9: 
    print(f"OBESIDAD MEDIA. {round(masa_corporal,2)}")
else:
    print(f"OBESIDAD MORVIDA. {round(masa_corporal,2)}")
