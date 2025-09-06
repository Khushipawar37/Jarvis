import speech_recognition as sr
import webbrowser
import pyttsx3

recognizer = sr.Recognizer()
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

# Example music library
musicLibrary = {
    "believer": "https://www.youtube.com/watch?v=7wtfhZwyrcc",
    "shapeofyou": "https://www.youtube.com/watch?v=JGwWNGJdvx8"
}

def processCommand(c):
    c = c.lower()
    if "open google" in c:
        webbrowser.open("https://google.com")
    elif "open facebook" in c:
        webbrowser.open("https://facebook.com")
    elif "open youtube" in c:
        webbrowser.open("https://youtube.com")
    elif "open linkedin" in c:
        webbrowser.open("https://linkedin.com")
    elif c.startswith("play"):
        song = c.split(" ")[1]
        if song in musicLibrary:
            webbrowser.open(musicLibrary[song])
        else:
            speak("Sorry, I don’t know that song.")

if __name__ == "__main__":
    speak("Initializing Jarvis....")
    while True:
        r = sr.Recognizer()
        try:
            with sr.Microphone() as source:
                print("Listening for wake word...")
                audio = r.listen(source, timeout=5, phrase_time_limit=3)
            word = r.recognize_google(audio)
            if word.lower() == "jarvis":
                speak("Yes?")
                with sr.Microphone() as source:
                    print("Jarvis Active...")
                    audio = r.listen(source)
                    command = r.recognize_google(audio)
                    processCommand(command)

        except sr.WaitTimeoutError:
            pass
        except sr.UnknownValueError:
            print("Sorry, I didn’t understand.")
        except Exception as e:
            print("Error:", e)
