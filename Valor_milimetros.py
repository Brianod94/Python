valor = int(input('Ingrese el valor en milimetros'))

metros = valor//1000
centimetros = (valor%1000) //10
milimetros = valor %10

print('Valor ingresado en milimetros', valor, ' equivale a: ')
print(' metros: ', metros)
print(' centimetros: ', centimetros)
print(' milimetros: ', milimetros)
