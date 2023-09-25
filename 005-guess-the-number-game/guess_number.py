# this is a guess the number game

import random

print('Hello. What is your name?')
name = input()

print('Well, ' + name + ' I am thinking of a number between 1 and 20. You have 6 guesses')

secretNumber = random.randint(1, 20)

for guessesTaken in range(1, 7):
    print('Take a guess: ')
    try:
        guessNumber = int(input())

        if guessNumber < secretNumber:
            print('Your guess is too low')
        elif guessNumber > secretNumber:
            print('Your guess is too high')
        else:
            print('Good job ! Congratulations')
            break
    except ValueError:
        print('Invalid number, enter a digit')

print('You took ' + str(guessesTaken) + ' guesses.')
print('The number I was thinking of was ' + str(secretNumber))