donacion=float(input('cual es el valor de la donacion = '))
sistemas=0.4
administracion=0.6
parte_sistema=donacion*sistemas
parte_admin=parte_sistema*administracion
contabilidad=donacion-parte_sistema
print('cantidad para sistemas:',parte_sistema)
print('cantidad para administracion:',parte_admin)
print('cantidad para contabilidad:',contabilidad)
