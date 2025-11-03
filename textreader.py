import pyttsx3

engine = pyttsx3.init()

engine.setProperty('rate', 150)
engine.setProperty('volume', 1.0)

text = input("enter the text you wan to hear: ")

engine.say(text)

engine.runAndWait()

