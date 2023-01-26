
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