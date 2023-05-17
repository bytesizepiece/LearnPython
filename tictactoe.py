def printBoard():
    print()  # print board layout / update to inc moves
    print(' ' + game['topL'] + ' | ' + game['topM'] + ' | ' + game['topR'])
    print('-----------')
    print(' ' + game['midL'] + ' | ' + game['midM'] + ' | ' + game['midR'])
    print('-----------')
    print(' ' + game['lowL'] + ' | ' + game['lowM'] + ' | ' + game['lowR'])


def formatMoveInput():
    # slice and format input to match game-keys
    global playerMove
    playerMoveLevel = playerMove[0:3].lower()
    playerMoveSide = playerMove[3:4].upper()
    playerMove = playerMoveLevel + playerMoveSide


def oppMove():
    # winning combos to make nested dict list
    winCheck1 = {'topL': 0, 'topM': 0, 'topR': 0}
    winCheck2 = {'midL': 0, 'midM': 0, 'midR': 0}
    winCheck3 = {'lowL': 0, 'lowM': 0, 'lowR': 0}
    winCheck4 = {'topL': 0, 'midL': 0, 'lowL': 0}
    winCheck5 = {'topM': 0, 'midM': 0, 'lowM': 0}
    winCheck6 = {'topR': 0, 'midR': 0, 'lowR': 0}
    winCheck7 = {'topL': 0, 'midM': 0, 'lowR': 0}
    winCheck8 = {'lowL': 0, 'midM': 0, 'topR': 0}
# nested dict list to loop
    winChecker = [winCheck1, winCheck2, winCheck3, winCheck4,
                  winCheck5, winCheck6, winCheck7, winCheck8]
# check if X move, add 1

    for winCheck in winChecker:
        for key in winCheck.keys():
            if game[key] == 'X':
                winCheck[key] = 1
            else:
                winCheck[key] = 0
        for key in winCheck.keys():
            if game[key] == 'X':
                winCheck[key] = 1
            else:
                winCheck[key] = 0

    oppBestMoveList = {}
    # create new dict to tally where winning rows need to be blocked.
    for winCheck in winChecker:
        if sum(winCheck.values()) == 2:
            for key, value in winCheck.items():
                if value == 0:
                    oppBestMoveList.setdefault(key, 0)
                    oppBestMoveList[key] = oppBestMoveList[key] + 1
                else:
                    continue

    compMove = ' '
    if playerChoice == 'X':
        compMove = 'O'
    else:
        compMove = 'X'

    try:
        compMovePosition = max(oppBestMoveList.values())
    except:
        for key in game:
            if key != ' ':
                continue
            else:
                key = compMove

    game[compMovePosition] = compMove


def makeYourMove():
    # ask for a move
    global playerMove
    print('Pick a move!')
    playerMove = input()
    formatMoveInput()

    # if not valid, ask again
    while playerMove not in game.keys():
        print('Pick a valid move!')
        playerMove = input()
        formatMoveInput()

    # if the move is already taken, ask again
    while game[playerMove] == 'X' or game[playerMove] == 'O':
        print('Pick a different position!')
        playerMove = input()
        formatMoveInput()

    # once valid, assign move to game
    game[playerMove] = playerChoice
    printBoard()

    # while there are spaces on the board, check if any combos win, otherwise ask for next move
    for gap in game:
        while game[gap] == ' ':
            checkWin(playerChoice)
            oppMove()
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


makeYourMove()

print('game over')
