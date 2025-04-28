
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
      # Lista principal de clientes
    clientes = []

    # Ciclo principal
    while True:
        print(" \n=== Menú de Clientes ===")
        print("[1] Crear cliente")
        print("[2] Consultar clientes")
        print("[3] Modificar cliente")
        print("[4] Borrar cliente")
        print("[5] Salir")
        
        opcion = input("Seleccione una opción: ")

        if opcion == "1":  # Crear cliente
            print("\n--- Crear Cliente ---")
            id_cliente = input("ID del cliente: ")
            nombre     = input("Nombre: ")
            correo     = input("Correo: ")
            telefono   = input("Teléfono: ")
            cliente    = [id_cliente, nombre, correo, telefono]
            clientes.append(cliente)
            print("Cliente creado exitosamente.\n")

        elif opcion == "2":  # Consultar clientes
            print("\n--- Lista de Clientes ---")
            if len(clientes) == 0:
                print("No hay clientes registrados.\n")
            else:
                for cliente in clientes:
                    print(f"ID: {cliente[0]}\ntNombre: {cliente[1]}\nCorreo: {cliente[2]}\nTeléfono: {cliente[3]}")
                print()

        elif opcion == "3":  # Modificar cliente
            print("\n--- Modificar Cliente ---")
            id_buscar = input("Ingrese el ID del cliente a modificar: ")
            encontrado = False
            for cliente in clientes:
                if cliente[0] == id_buscar:
                    print(f"Cliente encontrado: {cliente}")
                    cliente[1] = input("Nuevo nombre: ")
                    cliente[2] = input("Nuevo correo: ")
                    cliente[3] = input("Nuevo teléfono: ")
                    print("Cliente modificado exitosamente.\n") 
                    encontrado = True
                    break
            if not encontrado:
                print("Cliente no encontrado.\n")

        elif opcion == "4":  # Borrar cliente
            print("\n--- Borrar Cliente ---")
            id_buscar = input("Ingrese el ID del cliente a borrar: ")
            encontrado = False
            for i in range(len(clientes)):
                if clientes[i][0] == id_buscar:
                    print(f"Cliente encontrado: {clientes[i]}")
                    clientes.pop(i)
                    print("Cliente borrado exitosamente.\n")
                    encontrado = True
                    break
            if not encontrado:
                print("Cliente no encontrado.\n")

        elif opcion == "5":  # Salir
            print("Saliendo del programa...")
            break

        else:
            print("Opción inválida. Intente nuevamente.\n")

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