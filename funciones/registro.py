def registrar(r):
    t=int(input('en que tienda se realizó la venta? '))
    d=input('digite el deporte')
    v=float(input('digite el valor'))
    r.append([t,d,v])
    return r

def consultartienda(r):
    sum=0
    t=int(input('que tienda desea consultar'))
    for i in range (len(r)):
        if r[i][0]==t:
            sum=sum+r[i][2]
    print('el valor de las ventas de la tienda ', t, 'es ', sum)
   
    
def consultardeporte(r):
    sum=0
    d=(input('que deporte desea consultar'))
    for i in range (len(r)):
        if r[i][1]==d:
            sum=sum+r[i][2]
    print('el valor de las ventas del deporte ', d, 'es ', sum)
    
    
registro=[]
opc = 1
while opc != 4:
  print ('1. Registrar Venta')
  print ('2. Consultar por tienda')
  print ('3. Consultar por deporte')
  print ('4. salir')
  opc = int(input ('digite opcion: '))
  if opc == 1:
    registro=registrar(registro)
    print(registro)
  elif opc == 2:
    consultartienda(registro)
  elif opc == 3:
    consultardeporte(registro)
  elif opc == 4:
    print ('gracias por utilizar nuestros servicios')
  else:
    print ('digite una opc valida')