# 📄 `08_gesture_control/README.md`

⬅️ **Previous:** [07. Seeing Computer](../07_seeing_computer/README.md)  

---

# ✋ 08. Gesture Control

Now your computer can:
- Talk
- Listen
- See faces

Next step:
It will track your **hand**.

We will detect:
- When a hand appears
- Basic finger counting

This is the beginning of gesture-based control.

---

## 🧰 One-Time Setup

Install required libraries:

```

pip install mediapipe
pip install opencv-python

```

---

## ▶️ Run the Program

Go to the `project/` folder and run:

```

python main.py

````

A webcam window will open.

Move your hand in front of the camera.
You will see landmarks drawn on your hand.

Press `q` to exit.

---

## 🧠 How This Works

Open `project/main.py`.

---

### Step 1 — Import Libraries

```python
import cv2
import mediapipe as mp
````

OpenCV handles camera.
MediaPipe handles hand tracking.

---

### Step 2 — Setup Hand Detection

```python
mp_hands = mp.solutions.hands
hands = mp_hands.Hands()
mp_draw = mp.solutions.drawing_utils
```

This prepares the hand detection system.

---

### Step 3 — Process Frames

Each frame from camera is:

* converted to RGB
* processed by MediaPipe
* landmarks drawn

---

## 🧠 What You Learned

* Real-time landmark tracking
* How AI detects body parts
* Basic gesture detection system
* Combining OpenCV + MediaPipe

Now your computer can track hands.

---

## 📝 Practice Time

👉 Go to: [TASKS.md](./TASKS.md)

---
⬅️ **Previous:** [07. Seeing Computer](../07_seeing_computer/README.md)  

➡️ **Next:** [09. Smart AI Brain](../09_smart_ai_brain/README.md)

