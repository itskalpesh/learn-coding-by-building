import pyttsx3

engine = pyttsx3.init()
engine.setProperty("rate", 170)

def speak(text):
    try:
        engine.say(text)
        engine.runAndWait()
    except Exception as e:
        print("Voice Error:", e)
