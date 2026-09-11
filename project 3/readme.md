# 🖐️ Finger Counter using MediaPipe Tasks API

A real-time **Finger Counter** application built using **Python, OpenCV, and MediaPipe Tasks API**.

The application uses a webcam to detect one or two hands and counts the number of raised fingers.

---

## 📌 Features

* Real-time hand detection
* Supports up to two hands
* Counts fingers from 0 to 10
* Detects left and right hands
* Displays hand landmarks
* Displays hand connections
* Uses MediaPipe Tasks API
* Uses OpenCV for webcam processing
* Simple keyboard control

---

## 🛠️ Technologies Used

* Python
* OpenCV
* MediaPipe Tasks API

---

## 📁 Project Structure

```text
Finger-Counter/
├── requirements.txt
├── README.md
│
└── models/
    └── hand_landmarker.task
```

---

# ⚙️ Installation

## 1. Install Python

Make sure Python 3.9 or later is installed.

Check your Python version:

```bash
python --version
```

---

## 2. Clone or Download the Project

Open a terminal and move into the project directory:

```bash
cd Finger-Counter
```

---

## 3. Create a Virtual Environment

Windows:

```bash
python -m venv venv
```

Activate it:

```bash
venv\Scripts\activate
```

Linux/macOS:

```bash
python3 -m venv venv
```

Activate it:

```bash
source venv/bin/activate
```

---

# 📦 Install Dependencies

Install the required Python packages:

```bash
pip install -r requirements.txt
```

The project requires:

```text
opencv-python
mediapipe
```

---

# 🤖 MediaPipe Model Setup

The MediaPipe Tasks API requires a trained hand-landmarker model.

You need the following model file:

```text
hand_landmarker.task
```

Create a `models` folder inside your project:

```text
Finger-Counter/
│
└── models/
```

Place the downloaded model inside it:

```text
Finger-Counter/
│
└── models/
    └── hand_landmarker.task
```

The Python program expects the model at:

```text
models/hand_landmarker.task
```

---

# ▶️ Run the Project

After installing the dependencies and placing the model file in the correct location, run:

```bash
python finger_counter.py
```

The webcam window should open automatically.

---

# 🖐️ How It Works

The program follows these steps:

```text
Webcam
   ↓
Capture Frame
   ↓
Convert BGR → RGB
   ↓
MediaPipe Image
   ↓
MediaPipe Hand Landmarker
   ↓
Detect Hand Landmarks
   ↓
Identify Left / Right Hand
   ↓
Check Finger Positions
   ↓
Count Raised Fingers
   ↓
Display Result
```

---

# 🔢 Finger Landmark IDs

MediaPipe provides 21 landmarks for each hand.

Important fingertip landmarks are:

| Finger | Landmark ID |
| ------ | ----------: |
| Thumb  |           4 |
| Index  |           8 |
| Middle |          12 |
| Ring   |          16 |
| Pinky  |          20 |

The program compares the fingertip position with the corresponding finger joint to determine whether a finger is raised.

---

# 👐 Supported Finger Counts

The program supports:

```text
One hand:

0 → Closed fist
1 → One finger
2 → Two fingers
3 → Three fingers
4 → Four fingers
5 → Open hand

Two hands:

0 → 0 fingers
...
10 → Both hands fully open
```

---

# 🎮 Controls

| Key | Action               |
| --- | -------------------- |
| Q   | Quit the application |

Press:

```text
Q
```

to close the webcam window.

---

# 🔧 Configuration

You can modify the following settings in `finger_counter.py`:

```python
MODEL_PATH = "models/hand_landmarker.task"

CAMERA_ID = 0

MAX_HANDS = 2

MIN_DETECTION_CONFIDENCE = 0.5
MIN_PRESENCE_CONFIDENCE = 0.5
MIN_TRACKING_CONFIDENCE = 0.5
```

### Camera

If your default webcam does not work, try:

```python
CAMERA_ID = 1
```

or:

```python
CAMERA_ID = 2
```

### Number of Hands

To detect only one hand:

```python
MAX_HANDS = 1
```

For two hands:

```python
MAX_HANDS = 2
```

---

# ❗ Troubleshooting

## Model Not Found

If you see an error related to:

```text
hand_landmarker.task
```

make sure the file exists here:

```text
models/hand_landmarker.task
```

and that the project structure is:

```text
Finger-Counter/
├── finger_counter.py
├── requirements.txt
├── README.md
└── models/
    └── hand_landmarker.task
```

---

## Webcam Not Opening

Check whether another application is using the webcam.

You can also change:

```python
CAMERA_ID = 0
```

to:

```python
CAMERA_ID = 1
```

---

## MediaPipe Installation Error

Upgrade pip:

```bash
python -m pip install --upgrade pip
```

Then reinstall:

```bash
pip install -r requirements.txt
```

---

# 🚀 Future Improvements

Possible improvements include:

* Add gesture recognition
* Add difficulty levels
* Add a GUI
* Add FPS counter
* Add voice output
* Add screenshot functionality
* Detect specific hand gestures
* Use video/live-stream mode
* Create a virtual mouse
* Control applications using hand gestures

---

# 📄 License

This project is intended for educational and demonstration purposes.

---

# 👨‍💻 Project

**Finger Counter using MediaPipe Tasks API**

Built with:

```text
Python + OpenCV + MediaPipe
```
