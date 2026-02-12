# 🗣️ `05_talking_computer`

---

Until now, the computer showed text.

Now it will speak.

Yes — your program will talk out loud.

---

## 🎯 What You Will Build

When you run the program:

The computer says:
"Hello! I can speak now."

And you hear it.

---

## 🧰 One-Time Setup

We need a small library called `pyttsx3`.

Install it once using:

```

pip install pyttsx3

```

If you get an error, try:

```

python -m pip install pyttsx3

```

---

## ▶️ Run the Program

Go to the `project/` folder and run:

```

python main.py

```

You should hear your computer speak.

---

## 🧠 Read the Code

Open `project/main.py`.

### Step 1 — Import Library

```python
import pyttsx3
```

This loads the speech engine.

---

### Step 2 — Create Engine

```python
engine = pyttsx3.init()
```

This starts the voice system.

---

### Step 3 — Make It Speak

```python
engine.say("Hello! I can speak now.")
engine.runAndWait()
```

* `say()` tells it what to speak
* `runAndWait()` makes it actually talk

---

## 🧠 What You Learned

* How to install a Python package
* How to use external libraries
* How to convert text to speech

This is called **Text-to-Speech (TTS)**.

---

## 📝 Practice Time

👉 Go to: [05_TASKS](05_talking_computer/TASKS.md)

---

## 🚀 Next Lesson
⬅️ **Previous:** [04. Useful Tools](04_useful_tools/README.md)

➡️ **Next:** [06. Listening Computer](06_listening_computer/README.md)
