import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser
import wikipedia
import pywhatkit
import pyjokes
import os
import music_Library

# Initialize recognizer and TTS engine
recognizer = sr.Recognizer()
engine = pyttsx3.init()

def speak(text):
    print("Abrar:", text)
    engine.say(text)
    engine.runAndWait()

def listen():
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        command = recognizer.recognize_google(audio)
        print("You said:", command)
        return command.lower()
    except sr.UnknownValueError:
        speak("Sorry, I didn't catch that.")
        return ""
    except sr.RequestError:
        speak("Speech service is unavailable.")
        return ""

def run_abrar():
    speak("Hello! I am Abrar, your virtual assistant. How can I help you?")
    
    while True:
        command = listen()

        if "time" in command:
            current_time = datetime.datetime.now().strftime('%I:%M %p')
            speak(f"The current time is {current_time}")

        elif "date" in command:
            current_date = datetime.date.today().strftime('%B %d, %Y')
            speak(f"Today's date is {current_date}")

        elif "who is" in command or "what is" in command:
            topic = command.replace("who is", "").replace("what is", "")
            try:
                summary = wikipedia.summary(topic, sentences=2)
                speak(summary)
            except:
                speak("I couldn't find anything on that topic.")

        elif "open youtube" in command:
            webbrowser.open("https://www.youtube.com")
            speak("Opening YouTube")

        elif "open google" in command:
            webbrowser.open("https://www.google.com")
            speak("Opening Google")

        elif "open facebook" in command:
            webbrowser.open("https://www.facebook.com")
            speak("Opening facebook")

        elif "play" in command:
            song = command.replace("play", "")
            speak(f"Playing {song}")
            pywhatkit.playonyt(song)

        elif command.lower().startswith("play"):
            song =command.lower().split(" ")[1]
            link =music_Library.music[song]
            webbrowser.open(link)

        elif "joke" in command:
            joke = pyjokes.get_joke()
            speak(joke)

        elif "open code" in command:
            os.system("code")  # Works if VS Code is added to PATH
            speak("Opening Visual Studio Code")

        elif "stop" in command or "exit" in command or "quit" in command:
            speak("Goodbye from Abrar!")
            break

        elif command.strip() == "":
            continue  # Ignore empty input
        
        else:
            speak("I didn't understand. Can you say that again?")

if __name__ == "__main__":
    run_abrar()
