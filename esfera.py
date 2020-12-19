from math import pi

print('PROGRAMA PARA O CÁLCULO DO VOLUME DUNHA ESFERA')

cadena_leida = input('Introduce o radio: ')
radio = float(cadena_leida)

volumen = 4 / 3 * pi * radio ** 3

print('Volume:', volumen, 'metros cúbicos')
print('Fin do programa')
