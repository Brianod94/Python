import time
import os
opc = 1
while opc != 5:
  time.sleep(5)
  os.system('clear')
  print("********************************************\n")
  print ('1. matricular asig')
  print ('2. digitar notas')
  print ('3. consutar notas por nombre de asignatura')
  print ('4. consultar aprobadas')
  print ('5. salir')
  print("********************************************\n")
  opc = int(input ('digite opcion: '))
  if opc == 1:
    print('aqui llamo a la función matricular()')
  elif opc == 2:
    print('aqui llamo a la función dignotas()')
  elif opc == 3:
    print('aqui llamo a la función consultarn()')
  elif opc == 4:
    print('aqui llamo a la función consultara()')
  elif opc == 5:
    print ('gracias por utilizar nuestros servicios')
  else:
    print ('digite una opc valida')
