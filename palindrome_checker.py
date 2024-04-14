# Palindrome checker using python
def is_palindrome(s):
    p = ''
    for i in s:
        if i.isalnum():
            p += i
    return p == p[::-1]

while True:
    string = input('Enter a word (enter quit to exit): ').lower()
    if string == 'quit':
        print('Thankyou!')
        break
    if is_palindrome(string):
        print("Yes, it's a Palindrome")
    else:
        print("No, it's not a Palindrome")
        

