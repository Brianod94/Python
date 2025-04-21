print("esto es un juego de preguntas conteste 'si' o 'no'\npara ganar debes responder todas bien")
uno = input("¿Colon descubrio America? ")
if uno == "si":
    dos = input("¿la independencia de venezuela fue el el año 1810? ")
    if dos == "no":
        tres = input("¿Soda stereo fue un grupo de rock mexicano? ")
        if tres == "no":
            print("¡felicidades! Haz ganado")
        else:
            print("¡incorrecto! FIN DEL JUEGO")
    else:
        print("¡incorrecto! perdiste")    
else:
     print("¡incorrecto! perdiste") 
