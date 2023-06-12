import datetime
import speech_recognition as sr
import pyttsx3


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()
    engine.setProperty("rate", 150)


def greetings():
    hour = int(datetime.datetime.now().hour)
    if 0 <= hour < 12:
        speak("Good morning")
    elif 12 <= hour < 18:
        speak("Good afternoon")
    else:
        speak("Good Evening!")
    speak("I am Friday. What can I do for you?")


def commands():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
        try:
            print("Recognizing...")
            query = r.recognize_google(audio, language='en-in')
            print(f"User: {query}\n")
        except Exception as e:
            print(e)
            print("Please say that again...")
            return "None"
        return query


if __name__ == "__main__":
    greetings()
    commands()
