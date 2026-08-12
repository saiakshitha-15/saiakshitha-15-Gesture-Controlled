# 🎮 Hill Climb Gesture Control

Control the **Hill Climb Racing** game using real-time hand gestures through your webcam.

This project uses **Computer Vision and Hand Tracking** to detect hand movements and convert them into keyboard controls, allowing the player to control the vehicle without touching the keyboard.

## ✨ Features

- 🎥 Real-time webcam-based hand tracking
- ✋ Gesture recognition using MediaPipe
- 🎮 Keyboard control using PyAutoGUI
- 🚗 Control the game using hand movements
- ⚡ Real-time gesture detection
- 🖥️ Touch-free gaming experience

## 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| **Python** | Main programming language |
| **OpenCV** | Webcam access and image processing |
| **MediaPipe** | Hand tracking and landmark detection |
| **PyAutoGUI** | Keyboard automation |
| **NumPy** | Numerical processing |

## ⚙️ How It Works

```text
Webcam
   ↓
OpenCV
   ↓
MediaPipe Hand Tracking
   ↓
Hand Landmark Detection
   ↓
Gesture Recognition
   ↓
PyAutoGUI
   ↓
Hill Climb Racing
```

The webcam captures the user's hand movements in real time.

**OpenCV** processes the webcam frames, while **MediaPipe** detects hand landmarks. The detected hand movements are then interpreted as gestures.

The recognized gestures are converted into keyboard inputs using **PyAutoGUI**, allowing the player to control the game without directly using the keyboard.

## 📂 Project Structure

```text
HillClimbGestureControl/
│
├── main.py              # Main program
├── gesture.py           # Hand gesture detection
├── controller.py        # Game keyboard control
├── camera_test.py       # Webcam testing
├── test_key.py          # Keyboard control testing
├── requirements.txt     # Required Python packages
├── .gitignore           # Ignored files and folders
└── README.md            # Project documentation
```

## 🚀 Installation

### 1. Clone the Repository

```bash
git clone https://github.com/saiakshitha-15/saiakshitha-15-Gesture-Controlled.git
```

### 2. Navigate to the Project Folder

```bash
cd saiakshitha-15-Gesture-Controlled
```

### 3. Create a Virtual Environment

```bash
python -m venv venv
```

### 4. Activate the Virtual Environment

For Windows:

```bash
venv\Scripts\activate
```

### 5. Install the Required Packages

```bash
pip install -r requirements.txt
```

## ▶️ How to Run

1. Connect your webcam.
2. Open the Hill Climb Racing game.
3. Activate the virtual environment.
4. Run the main program:

```bash
python main.py
```

5. Position your hand in front of the webcam.
6. Use the supported hand gestures to control the game.

## 🧪 Testing

### Test the Webcam

To check whether the webcam is working correctly:

```bash
python camera_test.py
```

### Test Keyboard Control

To test keyboard input:

```bash
python test_key.py
```

## 💡 Applications

The concept can be extended to:

- 🎮 Gesture-controlled games
- 🖥️ Touchless computer interfaces
- 🤖 Human-computer interaction systems
- ♿ Assistive technologies
- 🏠 Gesture-controlled smart systems

## ⭐ Acknowledgements

This project uses open-source technologies including:

- **OpenCV**
- **MediaPipe**
- **PyAutoGUI**
- **NumPy**

---

