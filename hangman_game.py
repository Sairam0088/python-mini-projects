# Hangman game using python
import random

words = ['apple', 'banana', 'orange', 'grape', 'pear', 'pineapple', 'strawberry', 'watermelon']
choosed_word = random.choice(words)

def intialize_word(choosed_word):
    display = ["_"] * len(choosed_word)
    return display

def update_display(word, display, letter):
    for i in range(len(word)):
        if word[i] == letter:
            display[i] = letter
    return display

def is_correct_word(display):
    return "_" not in display

def hangman_display(chances):
    stages = [
        '''
           --------
           |      |
           |      O
           |     \\|/
           |      |
           |     / \\
          ---
        ''',
        '''
           --------
           |      |
           |      O
           |     \\|/
           |      |
           |     /
          ---
        ''',
        '''
           --------
           |      |
           |      O
           |     \\|/
           |      |
           |
          ---
        ''',
        '''
           --------
           |      |
           |      O
           |     \\|
           |      |
           |
          ---
        ''',
        '''
           --------
           |      |
           |      O
           |      |
           |      |
           |
          ---
        ''',
        '''
           --------
           |      |
           |      O
           |
           |
           |
          ---
        ''',
        '''
           --------
           |      |
           |
           |
           |
           |
          ---
        '''
    ]
    if len(stages) < chances:
        return stages[-1]
    return stages[chances]

def play():
    display = intialize_word(choosed_word)
    chances = len(display)
    guessed_letters = []
    print("Let's play Hangman!")
    
    while chances > 0:
        print(hangman_display(chances))
        print(*display)
        guess = input("Enter a letter: ").lower()
        if guess in guessed_letters:
            print("You already guessed this letter. Try again!")
            continue
        elif len(guess) > 1 or not guess.isalpha():
            print("Enter a single letter")
            continue
        guessed_letters.append(guess)
        if guess in choosed_word:
            display = update_display(choosed_word, display, guess)
            if is_correct_word(display):
                print(hangman_display(chances))
                print(*display)
                print("Congratulations! You guessed the correct word!")
                break
        else:
            print("Incorrect guess!")
            chances -= 1
    if chances == 0:
        print(hangman_display(chances))
        print("Sorry, you ran out of chances. The correct word was: ", choosed_word)

play()