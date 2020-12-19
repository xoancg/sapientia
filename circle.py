from math import pi

radius = float(input('Enter the radius of a circle: '))

# Variable initialization is needed for loop execution!
option = ''

while option < 'a' or option > 'd':
    print('Choose an option:')
    print('a) Calculate diameter')
    print('b) Calculate perimeter')
    print('c) Calculate area')
    print('d) Exit')

    option = input('Type the option and press Enter: ')

    if option == 'a':
        diameter = 2 * radius
        print('Diameter is', diameter)
    elif option == 'b':
        perimeter = 2 * pi * radius
        print('Perimeter is', perimeter)
    elif option == 'c':
        area = pi * radius ** 2
        print('Area is', area)
    elif option != 'd':
        print('There are only three options: a, b or c. You have typed:', option)

print("That's all. Thank you!")
