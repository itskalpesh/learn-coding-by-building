# 📄 `02_making_decisions/README.md`

⬅️ **Previous:** [01. Your First Program](../01_first_program/README.md)  

---

# 🟢 02. Making Decisions

In the last lesson, the computer talked to you.

Now we will teach the computer to **make decisions**.

This is where programming starts to feel powerful.

---

## 🎯 What You Will Build

When you run the program:

What is your name?
You: admin
Welcome back, admin!

But if you type something else:

```
What is your name?
You: Kalpesh
Nice to meet you, Kalpesh!

```

The computer now reacts differently.

---

## ▶️ Run the Program

Go to the `project/` folder and run:

```
python main.py

```

Try typing:
- admin
- your name
- random text

See what changes.

---

## 🧠 Read the Code Slowly

Open `project/main.py`.

### Step 1 — Ask the Name

```python
print("What is your name?")
name = input()
```

This is the same as Lesson 01.

---

### Step 2 — Decision Part

```python
if name == "admin":
    print("Welcome back, admin!")
```

This means:

IF the name is exactly `"admin"`
THEN print this message.

The `==` means “is equal to”.

---

### Step 3 — Otherwise

```python
else:
    print("Nice to meet you,", name)
```

If the name is NOT "admin",
the computer runs this instead.

---

## 🧠 What You Just Learned

* How the computer checks a condition
* How it chooses between two paths
* That programs are not just linear

This is called **decision making**.

---

## 📝 Practice Time

👉 Go to: [TASKS.md](./TASKS.md)

---

## 🚀 When You're Done
⬅️ **Previous:** [01. Your First Program](../01_first_program/README.md)  

➡️ **Next Lesson:**
📘 [03. Remembering Things](../03_remembering_things/README.md)

