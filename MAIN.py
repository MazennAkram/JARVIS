import speech_recognition as sr


SLEEPING = 0
LISTENING = 1
BUSY = 2
STATE = SLEEPING

UnknownValueError = "Couldn't understand command"
RequestError = "Couldn't access API"
recognizer = sr.Recognizer()

def Listen_for_commands():
    with sr.Microphone() as source: 
        print("Listening......")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
    try:
        command = recognizer.recognize_google(audio)
        return command.lower()
    except sr.UnknownValueError:
        return UnknownValueError
    except sr.RequestError:
        return RequestError


def Controller(state, command):
    order = command
    if command == RequestError:
        print(RequestError)
    elif command == UnknownValueError:
        print(UnknownValueError)
    else:
        if state == SLEEPING:
            if "jarvis" in command:
                print("Yes sir")
                return LISTENING
        elif state == LISTENING:
                return BUSY
        elif state == BUSY:
            #it should run the order through the AI function
            print(f"yes sir you wanted me to do {order}")

while True:
    if STATE != BUSY:
        Command = Listen_for_commands()
    STATE = Controller(STATE, Command)