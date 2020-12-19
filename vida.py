rows = 10
columns = 10
board = []
pulses = 6

for i in range(rows):
    board.append([False] * columns)

board[4][5] = True
board[5][5] = True
board[6][5] = True

# Representing the board
print('Initial status')
for y in range(rows):
    for x in range(columns):
        if board[y][x]:
            print('*', end='')
        else:
            print('.', end='')
    print()

# Pulses
for t in range(pulses):
    # Preparing a new board
    newboard = []

    for i in range(rows):
        newboard.append([False] * columns)

    # Updating the board
    for y in range(rows):
        for x in range(columns):
            # Calculate the number of cell neighbors we are visiting

            n = 0
            if y > 0 and x > 0 and board[y - 1][x - 1]:
                n += 1
            if x > 0 and board[y][x - 1]:
                n += 1
            if y < rows - 1 and x > 0 and board[y + 1][x - 1]:
                n += 1
            if y > 0 and board[y - 1][x]:
                n += 1
            if y < rows - 1 and board[y + 1][x]:
                n += 1
            if y > 0 and x < columns - 1 and board[y - 1][x + 1]:
                n += 1
            if x < columns - 1 and board[y][x + 1]:
                n += 1
            if y < rows - 1 and x < columns - 1 and board[y + 1][x + 1]:
                n += 1

            # Applying rules
            if board[y][x] and (n == 2 or n == 3):  # Survival
                newboard[y][x] = True
            elif not board[y][x] and n == 3:  # Birth
                newboard[y][x] = True
            else:  # Overcrowding and insulation
                newboard[y][x] = False

    # Updating board
    boar = newboard

    # Representing the board
    print('Pulse', t + 1)
    for y in range(rows):
        for x in range(columns):
            if board[y][x]:
                print('*', end='')
            else:
                print('.', end='')
        print()
