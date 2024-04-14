#typing speed tester using python

import time

def typing(text):
    print("Type the following text..")
    print(text)
    print("\nPress enter to start the typing..")
    input()
    start_time = time.time()
    typed_text = input("Start typing: ")
    end_time = time.time()
    time_taken = end_time - start_time
    word_count = len(typed_text.split())
    speed = calculate_speed(word_count, time_taken)
    accuracy = calculate_accuracy(text, typed_text)
    accurate_speed = speed * accuracy
    print(f"\nYour typing speed is {speed:.2f} words per minute")
    print(f"Your accuracy is {accuracy*100:.2f}%")
    print(f"\nYour accurate typing speed is {accurate_speed:.2f} words per minute\n")
    
def calculate_accuracy(actual_text, typed_text):
    actual_text = actual_text.split()
    typed_text = typed_text.split()
    correct_words = sum(1 for a, t in zip(actual_text, typed_text) if a==t)
    total_words = max(len(actual_text), len(typed_text))
    accuracy = correct_words/total_words
    return accuracy

def calculate_speed(word_count, time_taken):
    minutes = time_taken/60
    speed = word_count / minutes
    return speed

text = "The quick brown fox jumps over the lazy dog."
typing(text)
