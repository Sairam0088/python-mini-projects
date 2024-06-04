#email slicer

import re

def is_valid_email(email):
    regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    
    if re.fullmatch(regex, email):
        return True
    else:
        return False

email = input("Enter your email: ")
if is_valid_email(email):
    username = email[0:email.index('@')]
    domain = email[email.index('@')+1:]
    print("Username:",username)
    print("Domain:",domain)
else:
    print("Invalid Email")
    