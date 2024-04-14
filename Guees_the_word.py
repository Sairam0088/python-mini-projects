# guess the word game

import random 

def random_word():
    words = ["python", "programming", "challenge", "hangman", "coding"]
    word = random.choice(words)
    return word

def display_word(random_word,guessed_word):
    display = ""
    for i in random_word:
        if i in guessed_word:
            display += i
        else:
            display += "_"
    return display

def guess_the_word():
    choosed_word = random_word()
    guessed_word = []
    attempts = 6
    
    while '_' in display_word(choosed_word,guessed_word) and attempts > 0:
        guess = input('Guess a letter: ').lower()
        
        if len(guess)==1 and guess.isalpha():
            if guess in guessed_word:
                print('You already guessed this letter. Try again!')
            elif guess in choosed_word:
                print('Good guess!')
                guessed_word.append(guess)
            else:
                print('Incorrect guess. Try again!')
                attempts -= 1
        else:
            print('Invalid input. Please enter a single letter')
        
        print(display_word(choosed_word,guessed_word))
        print("Attempts left: ",attempts)
    
    if '_' not in (display_word(choosed_word,guessed_word)):
        print('Congratualations! You guessed the word.')
    else:
        print('Sorry you ran out of the attempts. The word is',choosed_word)

guess_the_word()
            