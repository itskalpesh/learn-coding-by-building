⬅️ Back: [02. VED Memory](../02_ved_memory/README.md)  
➡️ Next: [04. VED Voice](../04_ved_voice/README.md)

---

# 🛠️ 03. VED Tools

Now we separate actions into a tools module.

Tools are responsible for:

- Math
- Time
- Date
- Future extensions (weather, etc.)

The brain decides.
Tools execute.

This keeps architecture clean.

---

## 🧠 Why Separate Tools?

Bad structure:
main.py does everything.

Good structure:
main.py routes → tools.py executes.

This makes:

- Easier debugging
- Easy feature expansion
- Clean modular design

---

## 🎯 What You Will Build

Functions inside tools.py:

- get_time()
- get_date()
- add_numbers()
- help_menu()

Later:
brain.py will call these.

---

👉 Practice: [TASKS.md](./TASKS.md)

---

When ready:

➡️ Continue to:
[04. VED Voice](../04_ved_voice/README.md)
