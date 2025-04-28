
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
      #  esta es la Lista para guardar personas
      personas = []

      # Ingreso los datos de la persona 
      while True:
          print("\n--- Ingresar datos de una la empresa representada y su representante ---")
          nombre_empresa = input("Nombre de la empresa: ")
          nombre_representante = input("Nombre del representante: ")
          Cedula = input("documento de identidad:  ")
          correo = input("Correo: ")
          
          # Guardamos los datos en una lista
          persona = [nombre_empresa, nombre_representante, Cedula, correo]
          
          # Agregamos la persona a la lista general
          personas.append(persona)
          
          # Preguntar si quiere agregar otra persona
          continuar = input("¿Deseas agregar otra persona? (s/n): ").lower()
          if continuar != 's':
              break

      # Consultar datos
      while True:
          print("\n--- Consultar datos ---")
          
          if len(personas) == 0:
              print("No hay personas registradas.")
              break
          
          # Mostrar lista de personas
          for i in range(len(personas)):
              print(f"{i+1}. {personas[i][0]}")  # Solo mostrar el nombre DE LA PERSONAS GUADADAS EN CADA ITERACION
                                                # RECUERDEN QUE SIEMPRE ESTA EN EL ESPACIO CERO Y POR ESO LE SUMO 1
          try:                # utilizamos las sentancias try y except por si evalua un error fuera de las opciones disponibles
              opcion = int(input("Elige el número de la persona para ver sus datos (0 para salir): "))
              
              if opcion == 0:
                  break       # detenemos el ciclo con la opcion cero para salir y regresar al primer menu de opciones
              elif 1 <= opcion <= len(personas):
                  persona_seleccionada = personas[opcion - 1]
                  print(f"\nDatos de {persona_seleccionada[0]}:")
                  print(f"Edad: {persona_seleccionada[1]}")
                  print(f"Correo: {persona_seleccionada[2]}")
              else:
                  print("Opción no válida.")
          except ValueError:     # evalua el error y muestra este enunciado sin que el interrumpa el programa 
              print("Por favor, ingresa un número válido.")
      
          print( )
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