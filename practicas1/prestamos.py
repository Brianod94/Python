prestamo=int(input('digite valor del prestamo'))
num_de_años=int(input('digite cantidad de años'))
interes=0.12
total_pagar=prestamo*(interes*num_de_años)
cuota_esp=(total_pagar/2)/4
cuota_ord=(total_pagar/2)/20
print('el usuario debe pagar = ' ,total_pagar)
print('valor cuota especial' ,cuota_esp)
print('valor couta ordinaria' ,cuota_ord)
