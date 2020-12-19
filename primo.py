limit = int(input('Type a number: '))

for number in range(2, limit+1):
    isprime = True

    for divisor in range(2, number):
        if number % divisor == 0:
            isprime = False
            break

    if isprime:
        print(number, end=' ')
#print('.')