string = input('Enter a string: ')

reverse = ''

for i in string:
    reverse = i + reverse

print('Reverse is: ', reverse)

# What the code does is to read the characters of the string one by one and save them in the variable 'reverse'. Each new character is saved to the left of the previously saved one.
