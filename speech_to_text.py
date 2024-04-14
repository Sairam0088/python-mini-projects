# speech to text using python
# pip install SpeechRecognition
# pip install pyaudio

import speech_recognition as sr

recogniser = sr.Recognizer()

with sr.Microphone() as source:
    print("Speak something..")
    audio = recogniser.listen(source)

try:
    text = recogniser.recognize_google(audio)
    print("You said:",text)
except sr.UnknownValueError:
    print("Sorry couldn't understand the audio.")
except sr.RequestError as e:
    print("Could not reuqest results;",e)
