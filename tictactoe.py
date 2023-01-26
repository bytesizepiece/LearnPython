def printBoard():
    print()
    print(' ' + game['topL'] + ' | ' + game['topM'] + ' | ' + game['topR'])
    print('-----------')
    print(' ' + game['midL'] + ' | ' + game['midM'] + ' | ' + game['midR'])
    print('-----------')
    print(' ' + game['lowL'] + ' | ' + game['lowM'] + ' | ' + game['lowR'])


def formatMoveInput():
    global playerMove
    playerMoveLevel = playerMove[0:3].lower()
    playerMoveSide = playerMove[3:4].upper()
    playerMove = playerMoveLevel + playerMoveSide


def makeYourMove():
    global playerMove
    print('Pick a move!')
    playerMove = input()
    formatMoveInput()

    while playerMove not in game.keys():
        print('Pick a valid move!')
        playerMove = input()
        formatMoveInput()

    while game[playerMove] == 'X' or game[playerMove] == 'O':
        print('Pick a different position!')
        playerMove = input()
        formatMoveInput()

    game[playerMove] = playerChoice
    printBoard()

    for gap in game:
        while game[gap] == ' ':
            checkWin(playerChoice)
            makeYourMove()


def checkWin(i):
    if game['topL'] == i and game['topM'] == i and game['topR'] == i:
        print('you win!')
        exit()
    elif game['midL'] == i and game['midM'] == i and game['midR'] == i:
        print('you win!')
        exit()
    elif game['lowL'] == i and game['lowM'] == i and game['lowR'] == i:
        print('you win!')
        exit()
    elif game['topL'] == i and game['midL'] == i and game['lowL'] == i:
        print('you win!')
        exit()
    elif game['topM'] == i and game['midM'] == i and game['lowM'] == i:
        print('you win!')
        exit()
    elif game['topR'] == i and game['midR'] == i and game['lowR'] == i:
        print('you win!')
        exit()
    elif game['topL'] == i and game['midM'] == i and game['lowR'] == i:
        print('you win!')
        exit()
    elif game['lowL'] == i and game['midM'] == i and game['topR'] == i:
        print('you win!')
        exit()


game = {'topL': ' ', 'topM': ' ', 'topR': ' ', 'midL': ' ',
        'midM': ' ', 'midR': ' ', 'lowL': ' ', 'lowM': ' ', 'lowR': ' '}


print('X goes first')
print('Play as X or O?')
playerChoice = input().upper()

while playerChoice != 'X' and playerChoice != 'O':
    print('Play as X or O?')
    playerChoice = input().upper()


print()
print('''Great, let's play''')

printBoard()

# for gap in game:
#     while game[gap] == ' ':
#         checkWin(playerChoice)
makeYourMove()

print('game over')


# !!! function computer move
# check board for space
# if empty position, use it


# check if game won
# take input to check either x or o, then run function on:
# check if 3 same on:
# across top row
# across mid row
# across low row
# down left
# down mid
# down right
# diaganal lefttop
# diaganal leftlow


# if one space left, coputer defend position
