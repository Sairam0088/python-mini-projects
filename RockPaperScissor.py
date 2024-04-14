#Rock, Paper, Scissors using python
import random

def play_game(player_choice):
    choices = ['rock','paper','scissor']
    computer_choice = random.choice(choices)
    if player_choice == computer_choice:
        print("It's a tie!")
    elif (player_choice == 'rock' and computer_choice == 'scissor') or \
         (player_choice == 'paper' and computer_choice == 'rock') or \
         (player_choice == 'scissor' and computer_choice == 'paper'):
            print('You win!')
    else:
        print('Computer wins!')

while True:
    player_choice = input('Enter your choice from [rock, paper, scissor] or quit to exit: ').lower()
    if player_choice == 'quit':
        print('Good bye!')
        break
    if player_choice not in ['rock','paper','scissor']:
        print('Invalid choice. Enter a correct choice from [rock, paper, scissor]')
        continue
    play_game(player_choice)