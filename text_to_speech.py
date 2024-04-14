# text to speech using pyttsx3 library

import pyttsx3

engine = pyttsx3.init()

text = "Hello! Welcome to Develop with Python. This is a text-to-speech converter script using pyttsx3"

engine.setProperty('volume', 0.9)
engine.setProperty('rate', 150)

voices = engine.getProperty('voices')
male_voice = voices[0].id
female_voice = voices[1].id
engine.setProperty('voice', female_voice)

engine.say(text)
engine.runAndWait()

print("Completed Successfully!")