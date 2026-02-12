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

👉 Practice: [Ved_Memory_TASKS](12_build_ved_ai_capstone/02_ved_memory/TASKS.md)

---

When ready:

➡️ Continue to:
[03. VED Tools](12_build_ved_ai_capstone/03_ved_tools/README.md)

➡️ Back to:
[01_ved_text_brain](12_build_ved_ai_capstone/01_ved_text_brain/README.md)
