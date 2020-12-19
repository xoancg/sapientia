number = int(input('Type a number: '))

isprime = True

for divisor in range(2, number):
    if number % divisor == 0:
        isprime = False
        break

if isprime:
    print('{0} is a prime number! ;)'.format(number))
else:
    print('{0} is not a prime number! :('.format(number))