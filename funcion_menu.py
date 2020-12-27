def menu():
    option = ''
    while len(option) != 1 or option not in 'abc':
        print('\nAutomated teller machine (ATM):')
        print('a) Deposit money')
        print('b) Withdraw money')
        print('c) Check balance')

        option = input('Please, choose an option: ')

        if len(option) != 1 or option not in 'abc':
            print('\nYou only can choose a), b) or c). Please, try again.\n')
    return option


option = menu()

if option == 'a':
    print('\nOption selected: Deposit money')
elif option == 'b':
    print('\nOption selected: Withdraw money')
elif option == 'c':
    print('\nOption selected: Check balance')
else:
    print('Error!')