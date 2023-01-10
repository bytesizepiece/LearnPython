# gamble App
# start with 100 and welcome
# chose amount to wager
# chose number 1-6
# roll dice, show result
# soz you lose / congrats you win, new balance+start again

import random

guess = 0
wager = 0
balance = 100
while balance > 0:
    print('Welcome to the game')
    print('Your balance is: ' + str(balance))
    print('---')
    print('What is your wager?')
    wager = int(input())

    while wager > balance:
        print('Wager must be >= to balance')
        wager = int(input())

    print('Choose a number between 1 and 6')
    print('What is your guess?')
    guess = int(input())

    while guess < 0 or guess > 6:
        print('Try again, it is a dice!')
        wager = int(input())

    # diceRoll = 0
    diceRoll = random.randint(1, 6)

    print('---')
    print('---')
    print('Dice rolled: ' + str(diceRoll))
    print('---')
    print('---')

    if guess == diceRoll:
        print('YOU WIN!')
        balance = balance + wager
        print('Your balance is now: ' + str(balance))
    else:
        print('You lose')
        balance = balance - wager
        print('Your balance is now: ' + str(balance))

print('You have nothing left to wager!')
