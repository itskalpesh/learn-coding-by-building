⬅️ Back: [04. VED Voice](../04_ved_voice/README.md)  
➡️ Next: [06. VED UI](../06_ved_ui/README.md)

---

# 👁️ 05. VED Vision

Now we give VED the ability to see.

This module handles:

- Opening camera
- Detecting faces
- Returning results to brain

Vision is part of the input layer.

The brain should not manage camera directly.

---

## 🧰 Install Requirement

pip install opencv-python

---

## 🎯 What You Will Build

Functions inside vision.py:

- detect_faces()
- start_camera()

Later the brain can call these functions.

---

## 🧠 Why Separate Vision?

If camera code lives inside main,
it becomes messy.

Separation makes it:

- Reusable
- Maintainable
- Replaceable

---

👉 Practice: [TASKS.md](./TASKS.md)

---

When ready:

➡️ Continue to:
[06. VED UI](../06_ved_ui/README.md)
