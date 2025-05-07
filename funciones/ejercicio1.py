# Variables globales
ventas_por_tienda = {1: 0, 2: 0, 3: 0}
ventas_por_deporte = {}

def registrar_venta():
    try:
        print("\n--- Registro de Venta ---")
        tienda = int(input("Ingrese el código de la tienda (1, 2 o 3): "))
        if tienda not in ventas_por_tienda:
            print("❌ Código de tienda inválido. Debe ser 1, 2 o 3.\n")
            return
        
        deporte = input("Ingrese el nombre del deporte: ").strip()
        if not deporte:
            print("❌ El nombre del deporte no puede estar vacío.\n")
            return
        
        valor = float(input("Ingrese el valor de la venta: "))
        if valor <= 0:
            print("❌ El valor de la venta debe ser mayor que 0.\n")
            return

        # Confirmación
        print(f"\nConfirme la venta:\nTienda: {tienda}\nDeporte: {deporte}\nValor: ${valor:.2f}")
        confirmar = input("¿Desea guardar esta venta? (s/n): ").strip().lower()
        if confirmar != 's':
            print("Venta cancelada.\n")
            return
        
        # Actualizar ventas (ya NO se guarda en archivo)
        ventas_por_tienda[tienda] += valor
        if deporte in ventas_por_deporte:
            ventas_por_deporte[deporte] += valor
        else:
            ventas_por_deporte[deporte] = valor
        
        print("✅ Venta registrada exitosamente.\n")
    
    except ValueError:
        print("❌ Entrada inválida. Asegúrese de ingresar números donde corresponde.\n")

def mostrar_venta_total_por_tienda():
    print("\nVentas totales por tienda:")
    for tienda, total in ventas_por_tienda.items():
        print(f"Tienda {tienda}: ${total:.2f}")
    print()

def mostrar_venta_total_por_deporte():
    print("\nVentas totales por deporte:")
    for deporte, total in ventas_por_deporte.items():
        print(f"{deporte}: ${total:.2f}")
    print()

def menu():
    while True:
        print("*************************************")
        print("Menú:")
        print("[1] Registrar Venta")
        print("[2] Mostrar venta total por tienda")
        print("[3] Mostrar venta total por deporte")
        print("[4] Salir")
        print("*************************************")
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            registrar_venta()
        elif opcion == "2":
            mostrar_venta_total_por_tienda()
        elif opcion == "3":
            mostrar_venta_total_por_deporte()
        elif opcion == "4":
            print("Saliendo del programa.")
            break
        else:
            print("Opción inválida.\n")

# Ejecutar el menú principal
menu()
