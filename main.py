import cv2
import mediapipe as mp
from gesture import detect_gesture
from controller import control_game

# -----------------------------
# Open Webcam
# -----------------------------
cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)

if not cap.isOpened():
    print("❌ Could not open webcam.")
    exit()

print("✅ Webcam opened successfully.")

# -----------------------------
# MediaPipe Hands
# -----------------------------
mp_hands = mp.solutions.hands

hands = mp_hands.Hands(
    max_num_hands=1,
    min_detection_confidence=0.7,
    min_tracking_confidence=0.7
)

mp_draw = mp.solutions.drawing_utils

# -----------------------------
# Camera Window
# -----------------------------
window_name = "Hill Climb Gesture Control"

cv2.namedWindow(window_name, cv2.WINDOW_NORMAL)
cv2.resizeWindow(window_name, 640, 480)

# -----------------------------
# Main Loop
# -----------------------------
while True:

    success, frame = cap.read()

    if not success:
        print("❌ Failed to read frame from webcam.")
        continue

    # Flip camera
    frame = cv2.flip(frame, 1)

    # Convert BGR to RGB
    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Detect hands
    results = hands.process(rgb)

    gesture = "NONE"

    if results.multi_hand_landmarks:

        for hand_landmarks in results.multi_hand_landmarks:

            # Draw hand landmarks
            mp_draw.draw_landmarks(
                frame,
                hand_landmarks,
                mp_hands.HAND_CONNECTIONS
            )

            # Detect gesture
            gesture = detect_gesture(hand_landmarks)

    # Send keyboard command
    # control_game(gesture)

    # Display detected gesture
    cv2.putText(
        frame,
        f"Gesture : {gesture}",
        (20, 40),
        cv2.FONT_HERSHEY_SIMPLEX,
        1,
        (0, 255, 0),
        2
    )

    # Show camera
    cv2.imshow(window_name, frame)

    # Press ESC to exit
    key = cv2.waitKey(1)

    if key == 27:
        break

# -----------------------------
# Cleanup
# -----------------------------
cap.release()
cv2.destroyAllWindows()