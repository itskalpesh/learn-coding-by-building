⬅️ Back: [01. VED Text Brain](../01_ved_text_brain/README.md)  
➡️ Next: [03. VED Tools](../03_ved_tools/README.md)

---

# 🧠 02. VED Memory

Now we give VED memory.

Memory allows VED to:

- Remember your name
- Store preferences
- Save data between sessions

This is the first real separation of modules.

Memory will live in:

memory.py

Later, the brain will import and use it.

---

## 🎯 What You Will Build

Example:

You: remember my name is Kalpesh  
VED: I will remember that.

Restart program.

You: what is my name  
VED: Your name is Kalpesh.

That is persistent memory.

---

## 🧠 Architecture Goal

We separate memory into its own file:

memory.py

This file handles:

- Saving data
- Loading data
- Updating memory

The brain should not manage files directly.

---

## ▶️ How It Works

Memory will store data in:

ved_memory.json

This file keeps information even after program closes.

---

👉 Practice: [TASKS.md](./TASKS.md)

---

When ready:

➡️ Continue to:
[03. VED Tools](../03_ved_tools/README.md)
