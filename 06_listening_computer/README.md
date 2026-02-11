# 📄 `06_listening_computer/README.md`

⬅️ **Previous:** [05. Talking Computer](../05_talking_computer/README.md)  

---

# 🎤 06. Listening Computer

In the last lesson, the computer learned to speak.

Now it will listen.

You will speak into your microphone,
and the computer will convert your voice into text.

This is called **Speech-to-Text (STT)**.

---

## 🧰 One-Time Setup

Install required libraries:

```

pip install SpeechRecognition
pip install pyaudio

```

⚠️ If PyAudio fails on Windows, try:

```

pip install pipwin
pipwin install pyaudio

```

---

## ▶️ Run the Program

Go to the `project/` folder and run:

```

python main.py

````

When prompted:
- Speak clearly
- Wait a moment
- See your words appear as text

---

## 🧠 Read the Code

Open `project/main.py`.

---

### Step 1 — Import Library

```python
import speech_recognition as sr
````

This loads the speech recognition system.

---

### Step 2 — Create Recognizer

```python
recognizer = sr.Recognizer()
```

This prepares the system to process sound.

---

### Step 3 — Use Microphone

```python
with sr.Microphone() as source:
    print("Listening...")
    audio = recognizer.listen(source)
```

* The microphone records your voice
* The audio is stored in a variable

---

### Step 4 — Convert Speech to Text

```python
text = recognizer.recognize_google(audio)
print("You said:", text)
```

This sends the audio to Google’s speech recognition service
and returns the text.

---

## 🧠 What You Learned

* How to capture audio from microphone
* How speech recognition works
* How AI can convert sound into text

---

## 📝 Practice Time

👉 Go to: [TASKS.md](./TASKS.md)

---
⬅️ **Previous:** [05. Talking Computer](../05_talking_computer/README.md)


➡️ **Next :** [07. Seeing Computer](../07_seeing_computer/README.md)

