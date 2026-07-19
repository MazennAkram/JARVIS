import speech_recognition as sr


State = 0
# States:
# sleeping = 0
# Awake and listening = 1
# Talking = 2


def Listen_for_commands():
    recognizer = sr.Recognizer()

    with sr.Microphone() as source: 
        print("Listening......")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
    try:
        command = recognizer.recognize_google(audio)
        return command.lower()
    except sr.UnknownValueError:
        print("Couldn't understand command")
        return None
    except sr.RequestError:
        print("Couldn't access API")
        return None

def controller(Command):
    global State
    if State == 0:
        if "jarvis" in Command:
            print("Yes sir")
            State = 1
            controller(Listen_for_commands())
        else:
            controller(Listen_for_commands())
    elif State == 1:
        print("taking commands and all")
        print(Command)
        State = 2
        controller(Command)
    elif State == 2:
        print("doing the task and saying his reply")
        State = 0

controller(Listen_for_commands())