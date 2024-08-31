#importing important modules
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import pyttsx3

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)

def say(audio):
    engine.say(audio)
    engine.runAndWait()

def wishUser():
    hour = int(datetime.datetime.now().hour)
    if hour >=0 and hour<12:
        say("Good Morning!")
    elif hour >=12 and hour<18:
        say("Good Afternoon!")
    else:
        say("Good Evening")

    r=sr.Recognizer()
    with sr.Microphone() as  source:
        print("Listening..........")
        r.adjust_for_ambient_noise(source, duration=1)  # Adjust for ambient noise
        r.pause_threshold =1
        audio = r.listen(source)
    
