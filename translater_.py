# google translator using python

from googletrans import Translator

translator = Translator()

while True:
    text = input("Enter a text or quit: ")
    if text == "quit":
        break
    translated_text = translator.translate(text, dest="hi")
    print("Translated text:",translated_text.text)