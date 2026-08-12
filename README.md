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

The webcam captures the user's hand movements in real time.

OpenCV processes the webcam frames, while MediaPipe detects hand landmarks. The detected hand movements are then interpreted as gestures.

The recognized gestures are converted into keyboard inputs using PyAutoGUI, allowing the player to control the game without directly using the keyboard.

📂 Project Structure
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

Installation
1. Clone the Repository
git clone https://github.com/saiakshitha-15/saiakshitha-15-Gesture-Controlled.git
2. Navigate to the Project Folder
cd saiakshitha-15-Gesture-Controlled
3. Create a Virtual Environment
python -m venv venv
4. Activate the Virtual Environment

For Windows:

venv\Scripts\activate
5. Install the Required Packages
pip install -r requirements.txt
▶️ How to Run
Connect your webcam.
Open the Hill Climb Racing game.
Activate the virtual environment.
Run the main program:
python main.py
Position your hand in front of the webcam.
Use the supported hand gestures to control the game.
🧪 Testing
Test the Webcam

To check whether the webcam is working correctly:

python camera_test.py
Test Keyboard Control

To test keyboard input:

python test_key.py

⭐ Acknowledgements

This project uses open-source technologies including:

OpenCV
MediaPipe
PyAutoGUI
NumPy