number = int(input('Type a number: '))

if number > 1:
    isprime = True
    divisor = 2

    while divisor < number:
        if number % divisor == 0:
            isprime = False
            break
        divisor += 1
else:
    isprime = False

if isprime:
    print('{0} is a prime number! ;)'.format(number))
else:
    print('{0} is not a prime number! :('.format(number))