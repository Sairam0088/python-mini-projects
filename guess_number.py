#guess the correct number game
import random

lowest = int(input('Enter lowest number: '))
highest = int(input('Enter highest number: '))
random_num = random.randint(lowest,highest)
print('Your would get 5 chances to guess the correct number')
chances = 0

while chances<5:
    user_guess= int(input('Enter your guess: '))
    chances += 1
    if user_guess==random_num:
        print(f'Yayy! you guessed the correct number in {chances} chances')
        break
    elif user_guess>random_num:
        print('Too high! Try again')
    else:
        print('Too low! Try again')
    if chances>=5:
        print(f'The correct number is {random_num}\nBetter luck next time')
