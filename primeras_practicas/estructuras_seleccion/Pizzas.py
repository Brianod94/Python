def mostrar_menu_principal():
    print("\n*****************************************************")
    print("¿Qué tipo de pizza desea ordenar?")
    print("[1] Vegetariana 🥬")
    print("[2] No vegetariana 🍖")
    print("[3] Salir 👋")
    print("*****************************************************")

def mostrar_ingredientes_vegetarianos():
    print("\nIngrese el número del ingrediente adicional:")
    print("[1] Pimiento 🫑")
    print("[2] Champiñón 🍄")
    print("[3] Otro ➕")

def mostrar_ingredientes_no_vegetarianos():
    print("\nIngrese el número del ingrediente adicional:")
    print("[1] Peperoni 🥓")
    print("[2] Jamón 🥩")
    print("[3] Salmón 🍣")
    print("[4] Otro ➕")

def obtener_opcion(mensaje, opciones_validas):
    while True:
        opcion = input(mensaje).strip()
        if opcion in opciones_validas:
            return opcion
        print(f"¡Error! Opción no válida. Por favor ingrese {', '.join(opciones_validas)}")

def main():
    # Mensaje de bienvenida
    print("*****************************************************")
    print("********🫡 Bienvenido a Pizza Bella Napoli 🍕********")
    print("*****************************************************")

    ingredientes_vegetarianos = {
        '1': ('Pimiento', '🫑'),
        '2': ('Champiñón', '🍄'),
        '3': ('Otro', '➕')
    }

    ingredientes_no_vegetarianos = {
        '1': ('Peperoni', '🥓'),
        '2': ('Jamón', '🥩'),
        '3': ('Salmón', '🍣'),
        '4': ('Otro', '➕')
    }

    while True:
        mostrar_menu_principal()
        opcion = obtener_opcion("Opción: ", ['1', '2', '3'])

        if opcion == '1':  # Pizza vegetariana
            mostrar_ingredientes_vegetarianos()
            ingrediente = obtener_opcion("Opción: ", ['1', '2', '3'])
            
            if ingrediente == '3':
                otro_ingrediente = input("Ingrese el ingrediente que desea agregar: ").strip()
                nombre_ingrediente, emoji = otro_ingrediente, "➕"
            else:
                nombre_ingrediente, emoji = ingredientes_vegetarianos[ingrediente]
            
            print(f"\nUsted ordenó una pizza vegetariana con mozzarella 🧀, tomate 🍅 y {nombre_ingrediente} {emoji}\n")

        elif opcion == '2':  # Pizza no vegetariana
            mostrar_ingredientes_no_vegetarianos()
            ingrediente = obtener_opcion("Opción: ", ['1', '2', '3', '4'])
            
            if ingrediente == '4':
                otro_ingrediente = input("Ingrese el ingrediente que desea agregar: ").strip()
                nombre_ingrediente, emoji = otro_ingrediente, "➕"
            else:
                nombre_ingrediente, emoji = ingredientes_no_vegetarianos[ingrediente]
            
            print(f"\nUsted ordenó una pizza no vegetariana con mozzarella 🧀, tomate 🍅 y {nombre_ingrediente} {emoji}\n")

        elif opcion == '3':  # Salir
            print("\n¡Gracias por visitar Pizza Bella Napoli! 🤗")
            print("Vuelva pronto 😋\n")
            break

if __name__ == "__main__":
    main()