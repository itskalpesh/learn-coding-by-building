import pyttsx3
import speech_recognition as sr

# Initialize speech engine once
engine = pyttsx3.init()
engine.setProperty("rate", 170)

def speak(text):
    try:
        engine.say(text)
        engine.runAndWait()
    except Exception as e:
        print("TTS Error:", e)

def listen():
    recognizer = sr.Recognizer()

    try:
        with sr.Microphone() as source:
            print("Listening...")
            audio = recognizer.listen(source)

        text = recognizer.recognize_google(audio)
        return text.lower()

    except sr.UnknownValueError:
        return "I did not understand."

    except sr.RequestError:
        return "Speech service unavailable."

    except Exception as e:
        return f"Microphone error: {e}"
