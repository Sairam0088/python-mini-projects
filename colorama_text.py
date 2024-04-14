# colorama game using python
from colorama import init, Fore
import random

init(autoreset=True)

COLORS = [Fore.RED, Fore.GREEN, Fore.YELLOW, Fore.BLUE, Fore.MAGENTA, Fore.CYAN]

def print_colored(text):
    global target_color
    target_color = random.choice(COLORS)
    print(target_color + text)

print("Welcome to Colorama game")

while True:
    text = "Develop with Python"
    print_colored(text)
    guess = input("Enter the color of above text: ").upper()
    
    for name, color in Fore.__dict__.items():
        if color == target_color:
            target_color_name = name
            break
    
    if guess == target_color_name:
        print("Congratulations! You guessed correctly")
    else:
        print("Oops! incorrect guess. The correct color was:",target_color_name)
    
    play_again = input("Do you want to play again (yes/no): ").lower()
    if play_again != "yes":
        print("Thanks for playing")
        break
        


