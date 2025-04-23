#Saldo inicial
saldo = 1000000

opcion = 0

print("💰 BIENVENIDO AL CAJERO AUTOMATICO")

while opcion != 4:
    print(f"\nSeleccione una opción:\n ")
    print(f"1. Consultar saldo")
    print(f"2. Retirar dinero")
    print(f"3. Depositar dinero")
    print(f"4. Salir")

    opcion = int(input("\nOpcion: "))

    if opcion == 1:
        print(f"\n📄 Su saldo actual es: ${saldo}")

    elif opcion == 2:
        retiro = int(input("¿Cuánto dinero desea retirar? $"))
        if retiro <= saldo:
            saldo -= retiro
            print(f"\n💵 Ha retirado: ${retiro}")
            print(f"📄 Su saldo actual es: ${saldo}")
        else:
            print("\n❌ No tiene suficiente saldo para realizar esta operación.")

    elif opcion == 3:
        deposito = int(input("¿Cuánto dinero desea depositar? $"))
        saldo += deposito
        print(f"\n💵 Ha depositado: ${deposito}")
        print(f"📄 Su saldo actual es: ${saldo}")

    elif opcion == 4:
        print("\n👋 Gracias por usar el cajero automático. ¡Hasta luego!")

    else:
        print("\n❌ Opción inválida. Por favor, seleccione una opción válida.\n")

