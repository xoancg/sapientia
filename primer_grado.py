#Reformat Code: Ctrl+Alt+L

print('Programa para a resolución da ecuación ax + b = 0')

a = float(input('Valor de a: '))
b = float(input('Valor de b: '))

if a != 0:
    x = -b / a
    print('Solución:', x)

if a == 0:
    if b != 0:
        print('A ecuación non ten solución!')
    if b == 0:
        print('A ecuación ten infinitas solucións!')
