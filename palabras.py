string = input('Write a sentence: ')

while string != '':
    changes = 0
    #previous = ' '

    for i in range(0, len(string)):
        if string[i] == ' ' and string[i-1] != ' ':
            changes += 1
            #previous = char

    if string[-1] == ' ':
        changes -= 1
    # There is one more word than changes from letter to space
    words = changes + 1
    print('Words: ', words)

    string = input('Write a sentence: ')