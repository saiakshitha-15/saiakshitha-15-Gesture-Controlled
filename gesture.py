def detect_gesture(hand_landmarks):

    landmarks = hand_landmarks.landmark

    # Finger tip points
    tips = [
        8,   # index
        12,  # middle
        16,  # ring
        20   # pinky
    ]

    fingers = []

    for tip in tips:

        if landmarks[tip].y < landmarks[tip-2].y:
            fingers.append(1)

        else:
            fingers.append(0)


    # Count open fingers
    total_fingers = sum(fingers)


    if total_fingers == 4:
        return "ACCELERATE"

    elif total_fingers == 0:
        return "BRAKE"

    else:
        return "NONE"