⬅️ Back: [03. VED Tools](../03_ved_tools/README.md)  
➡️ Next: [05. VED Vision](../05_ved_vision/README.md)

---

# 🎤 04. VED Voice

Now we give VED the ability to:

- Speak
- Listen

This module handles all voice operations.

The brain should not manage microphone or speakers directly.

Voice module = input + output layer.

---

## 🧠 Responsibilities of voice.py

It will contain:

- speak(text)
- listen()

These functions will later be called by the brain.

---

## 🧰 Install Requirements

Install once:

pip install pyttsx3
pip install SpeechRecognition
pip install pyaudio

(Windows users may need pipwin for pyaudio.)

---

## 🎯 What You Will Build

VED will:

- Speak responses
- Listen for voice input
- Return recognized text to brain

---

👉 Practice: [TASKS.md](./TASKS.md)

---

When ready:

➡️ Continue to:
[05. VED Vision](../05_ved_vision/README.md)
