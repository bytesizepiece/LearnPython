# ask do you want to play? Y or no?
#  if X or O?
# easy or hard??
# draw a grid, assign key,value pairs to each space


def printBoard():
    print()
    print(' ' + game['topL'] + ' | ' + game['topM'] + ' | ' + game['topR'])
    print('-----------')
    print(' ' + game['midL'] + ' | ' + game['midM'] + ' | ' + game['midR'])
    print('-----------')
    print(' ' + game['lowL'] + ' | ' + game['lowM'] + ' | ' + game['lowR'])


game = {'topL': ' ', 'topM': ' ', 'topR': ' ', 'midL': ' ',
        'midM': ' ', 'midR': ' ', 'lowL': ' ', 'lowM': ' ', 'lowR': ' '}


print('Would you like to play? Y or N')
playInput = input().upper()

if playInput != 'Y':
    exit

print()
print('X goes first')
print('Play as X or O?')
playerChoice = input().upper()

while playerChoice != 'X' and playerChoice != 'O':
    print('Play as X or O?')
    playerChoice = input().upper()


print()
print('''Great, let's play''')

print(printBoard())

print('Pick a move!')
playerMove = input()



while game.values(playerMove):
    print('Pick a move!')
    playerMove = input()
