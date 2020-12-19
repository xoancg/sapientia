n = int(input('Enter the maximum value: '))

primes = []

for number in range(2, n+1):
    # Check if it's a prime number
    isprime = True

    for divisor in range(2, number):
        if number % divisor == 0:
            isprime = False
            break
    # If it's a prime number, it's added to the list
    if isprime:
        primes.append(number)

# Print list of prime numbers
print(primes)