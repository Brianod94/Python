print("===========sistema de vacaciones ===============")
clave_departamento=int(input("ingrese el departamento al cual pertenece\n1. Atencion al cliente\n2. Logistica\n3. Gerencia\nOpcion: "))
if clave_departamento==4:
     print("¡ESTE DEPARTAMENTO NO ESTA DISPONIBLE!")
     exit()
trabajador=input("nombre del trabajdor. ")
años=float(input("digite años de antiguedad. "))
#ATENCION AL CLIENTE
if clave_departamento==1:
    trabajador=input("nombre del trabajdor. ")
    años=float(input("digite años de antiguedad. "))
    if años==1:
        print(f"Trabajador {trabajador} recibe 6 dias de vacaciones. ")
    elif años>=2 and años<=6:
        print(f"Trabajador {trabajador} recibe 14 dias de vacaciones. ")
    elif años>=7:
        print(f"Trabajador {trabajador} recibe 20 dias de vacaciones. ")
    else:
        print("no tiene derecho a vacaciones")
#LOGISTICA
elif clave_departamento==2:
   
    if años==1:
        print(f"Trabajador {trabajador} recibe 7 dias de vacaciones. ")
    elif años>=2 and años<=6:
        print(f"Trabajador {trabajador} recibe 15 dias de vacaciones. ")
    elif años>=7:
        print(f"Trabajador {trabajador} recibe 22 dias de vacaciones. ")
    else:
        print("no tiene derecho a vacaciones")
#GERENCIA
else: 
    clave_departamento==3
    
    if años==1:
     print(f"Trabajador {trabajador} recibe 10 dias de vacaciones. ")
    elif años>=2 and años<=6:
        print(f"Trabajador {trabajador} recibe 20 dias de vacaciones. ")
    elif años>=7:
        print(f"Trabajador {trabajador} recibe 30 dias de vacaciones. ")
    else:
        print("no tiene derecho a vacaciones")

  