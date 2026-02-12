# 🧠 `09_smart_ai_brain`
---
Until now, your computer can:
- Talk
- Listen
- See
- Track gestures

But it doesn’t think.

Now we build a simple AI brain.

The brain will:
- take user input
- understand intent
- decide what action to perform

This is the beginning of real AI structure.

---

## 🎯 What You Will Build

Example interaction:

```

You: time
AI: Current time is 14:35

You: hello
AI: Hello there!

You: add 5 7
AI: Result is 12

```

The program understands commands
and routes them to the correct function.

---

## ▶️ Run the Program

Go to the `project/` folder and run:

```

python main.py

````

Try different inputs like:
- hello
- time
- add 3 8
- something random

---

## 🧠 How It Works

Open `project/main.py`.

---

### Step 1 — Define Tools

We create small functions:

```python
def say_hello():
    print("Hello there!")

def show_time():
    from datetime import datetime
    now = datetime.now()
    print("Current time is", now.strftime("%H:%M"))
````

Each function does one job.

---

### Step 2 — Simple Router

```python
if command == "hello":
    say_hello()
elif command == "time":
    show_time()
```

This is the brain deciding what to call.

---

### Step 3 — Parsing Math Input

For:

```
add 5 7
```

We split the text and calculate.

---

## 🧠 What You Learned

* Breaking logic into functions
* Routing input to actions
* Basic command parsing
* How simple AI assistants are structured

This is how real assistants start.

---

## 📝 Practice Time

👉 Go to: [09_TASKS](09_smart_ai_brain/TASKS.md)

---
⬅️ **Previous:** [08_gesture_control](08_gesture_control/README.md) 
 
➡️ **Next:** [10_real_world_apps](10_real_world_apps/README.md)
