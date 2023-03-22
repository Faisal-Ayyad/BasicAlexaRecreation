import speech_recognition as sr
import pyttsx3

r = sr.Recognizer()
engine = pyttsx3.init()


def speak(text):
    engine.say(text)
    engine.runAndWait()


while True:

    with sr.Microphone() as source:
        print("Say something!")
        audio = r.listen(source)

    try:

        text = r.recognize_google(audio)
        print("You said:", text)

        if "hello" in text.lower():
            speak("Hello, how can I help you?")
        elif "goodbye" in text.lower():
            speak("Goodbye!")
            break
        else:
            speak("I'm sorry, I didn't understand what you said.")

    except sr.UnknownValueError:
        print("Sorry, I could not understand what you said.")
