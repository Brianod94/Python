
opc = 1 # inicializo la variable en 1 para empezar a recorrer las opciones 
while opc != 5: # mientras tiene el comparador de diferencia para que al moemento de ingresar una opcion mala salga un enunciado de error
  
  print("********************************************\n")
  #inicio del menu de seleccion con la opciones disponibles 
  print ('[1] Clientes')  #
  print ('[2] Materia Prima')
  print ('[3] Inventario')
  print ('[4] Valores Definitivos')
  print ('[5] salir')
  print("********************************************\n")
  # esta seria el comienzo del condicional para el momento de elegir cualquiera opcion 
  # cada 1 de la opciones debemos trabajarlas internamente para que empiecen a funcionar 
  opc = int(input ('digite opcion: '))
  if opc == 1: 
    print('aqui llamo a la función cliente()')
  elif opc == 2:
    print('aqui llamo a la función Materia prima()')
  elif opc == 3:
    print('aqui llamo a la función Inventario()')
  elif opc == 4:
    print('aqui llamo a la función Valores Defenitivos()')
  elif opc == 5:
    print ('Salir del proograma')
  else:
    print ('digite una Opcion Valida')

