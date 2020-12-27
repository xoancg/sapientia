def is_perfect(n):
    summation = 0
    for i in range(1, n):
        if n % i == 0:
            summation += i
    return summation == n


x = int(input(' Enter a Number: '))

is_perfect(x)

if is_perfect(x):
    print('{0} is a perfect number! ;)'.format(x))
else:
    print('{0} is not a perfect number. :('.format(x))
