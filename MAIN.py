import pyaudio
import speech_recognition as sr
import time

# Variables
r = sr.Recognizer()
m = sr.Microphone()
Spoken_text = ""


def Controller(Text):
    if "jarvis" in Text:
        print("Awake")
        

def callback(recognizer, audio):
    try:
        Controller(recognizer.recognize_google(audio).lower())
        print(recognizer.recognize_google(audio).lower())
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))

with m as source:
    r.adjust_for_ambient_noise(source)

stop_listening = r.listen_in_background(m, callback)

while True: 
    time.sleep(0.1)
