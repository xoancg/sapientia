number = int(input('Type a number: '))

#for power in [2, 3, 4, 5]:

# Note: 'b' parameter is not included in range(a, b)
for power in range(2, 5):
    print('{0} to the power of {1} is {2}'.format(number, power, number ** power))