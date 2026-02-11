# 📄 `03_remembering_things/README.md`

⬅️ **Previous:** [02. Making Decisions](../02_making_decisions/README.md)  

---

# 🟢 03. Remembering Things

Until now, the computer forgets everything when the program stops.

Now we will teach it to **remember your name**, even after you close it.

This is where programming starts to feel like AI.

---

## 🎯 What You Will Build

First time running:

```

What is your name?
You: Kalpesh
Nice to meet you, Kalpesh!

```

Close the program.

Run it again:

```

Welcome back, Kalpesh!

```

The computer remembers you.

---

## ▶️ Run the Program

Go to the `project/` folder and run:

```

python main.py

```

Run it twice to see the difference.

---

## 🧠 How This Works (Simple Explanation)

Open `project/main.py`.

---

### Step 1 — Try to Read a File

```python
try:
    file = open("name.txt", "r")
    name = file.read()
    file.close()
    print("Welcome back,", name)
```

This tries to:

* open a file called `name.txt`
* read what’s inside
* print it

If the file exists, the name is remembered.

---

### Step 2 — If File Doesn't Exist

```python
except:
    print("What is your name?")
    name = input()

    file = open("name.txt", "w")
    file.write(name)
    file.close()

    print("Nice to meet you,", name)
```

If the file does NOT exist:

* ask the user for their name
* create `name.txt`
* store the name inside it

Now it’s saved forever (until deleted).

---

## 🧠 What You Learned

* How to create a file
* How to write to a file
* How to read from a file
* How programs can store data

This is called **persistence**.

You just built memory.

---

## 📝 Practice Time

👉 Go to: [TASKS.md](./TASKS.md)

---

## 🚀 When You're Done
⬅️ **Previous:** [02. Making Decisions](../02_making_decisions/README.md)

➡️ **Next Lesson:**
📘 [04. Useful Tools](../04_useful_tools/README.md)

