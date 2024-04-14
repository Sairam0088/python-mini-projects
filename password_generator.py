#password generator using python
import string
import random

def generate_password(length=8):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ""
    for i in range(length):
        password += random.choice(characters)
    return password

def check_password(password:str):
    has_digit = any(d.isdigit() for d in password)
    has_letter = any(l.isalpha() for l in password)
    has_punc = any(p in string.punctuation for p in password)
    return has_digit and has_letter and has_punc

while True:
    password = generate_password(12)
    if check_password(password):
        print(password)
        break