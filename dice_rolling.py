#Dice rolling simulator using python
import random

def roll_dice():
    while True:
        input('Press enter to roll the dice..')
        result = random.randint(1,6)
        print(f'you rolled: {result}')
        play_again = input('Do you want to play again? yes/no: ').lower()
        if play_again != 'yes':
            print('Thanks for playing! Goodbye!')
            break
roll_dice()
