elif opcion == "2":
            print("\n==== Consultar Clientes ====")
            buscar_cliente = input("Ingrese el ID o nombre de la empresa a buscar: ").strip().lower()
            encontrados = [c for c in clientes if buscar_cliente in c["id"].lower() or buscar_cliente in c["empresa"].lower()]

            if encontrados:
                for cliente in encontrados:
                    print(f"""\nID: {cliente['id']}\nEmpresa: {cliente['empresa']}\nRepresentante: {cliente['representante']}\n
                          Correo: {cliente['correo']}\nTeléfono: {cliente['telefono']}\nFecha Registro: {cliente['fecha']}""")
            else:
                print("No se encontraron clientes con ese criterio.\n")

        elif opcion == "3":
            print("\n==== Modificar Cliente ====")
            id_buscar = input("Ingrese el ID del cliente a modificar: ")
            cliente = next((c for c in clientes if c["id"] == id_buscar), None)

            if cliente:
                print("Deje en blanco para mantener el valor actual.")
                cliente["empresa"] = input(f"Nuevo nombre de empresa [{cliente['empresa']}]: ") or cliente["empresa"]
                cliente["representante"] = input(f"Nuevo representante legal [{cliente['representante']}]: ") or cliente["representante"]
                cliente["correo"] = input(f"Nuevo correo [{cliente['correo']}]: ") or cliente["correo"]
                cliente["telefono"] = input(f"Nuevo teléfono [{cliente['telefono']}]: ") or cliente["telefono"]
                cliente["fecha"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                print("Cliente modificado exitosamente.\n")
            else:
                print("Cliente no encontrado.\n")
