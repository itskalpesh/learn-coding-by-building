# 📄 `07_seeing_computer/README.md`

⬅️ **Previous:** [06. Listening Computer](../06_listening_computer/README.md)  

---

# 👁️ 07. Seeing Computer

Until now, the computer could:
- Talk
- Listen

Now it will see.

We will open your webcam and detect faces in real time.

This is the beginning of computer vision.

---

## 🧰 One-Time Setup

Install OpenCV:

```

pip install opencv-python

```

---

## ▶️ Run the Program

Go to the `project/` folder and run:

```

python main.py

````

A camera window will open.

If a face appears in front of the camera,
a box will be drawn around it.

Press `q` to close the window.

---

## 🧠 Read the Code

Open `project/main.py`.

---

### Step 1 — Import OpenCV

```python
import cv2
````

OpenCV is a powerful computer vision library.

---

### Step 2 — Load Face Detection Model

```python
face_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
)
```

This loads a built-in face detection model.

---

### Step 3 — Start Camera

```python
cap = cv2.VideoCapture(0)
```

`0` means your default webcam.

---

### Step 4 — Detect Faces

Inside a loop, the program:

* reads each frame
* converts it to grayscale
* detects faces
* draws rectangles

---

## 🧠 What You Learned

* How to open a webcam
* How real-time detection works
* How AI can detect faces
* Basic image processing

You just built a simple computer vision system.

---

## 📝 Practice Time

👉 Go to: [TASKS.md](./TASKS.md)

---
⬅️ **Previous:** [06. Listening Computer](../06_listening_computer/README.md)

➡️ **Next:** [08. Gesture Control](../08_gesture_control/README.md)

---
