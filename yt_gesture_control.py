import cv2
import mediapipe as mp
import pyautogui
import time

# Init MediaPipe
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(max_num_hands=1)
mp_draw = mp.solutions.drawing_utils

# Start Webcam
cap = cv2.VideoCapture(0)

prev_gesture = None
gesture_time = 0

while True:
    success, img = cap.read()
    img = cv2.flip(img, 1)
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    result = hands.process(img_rgb)

    if result.multi_hand_landmarks and result.multi_handedness:
        for hand_landmarks, hand_info in zip(result.multi_hand_landmarks, result.multi_handedness):
            label = hand_info.classification[0].label  # Left or Right

            mp_draw.draw_landmarks(img, hand_landmarks, mp_hands.HAND_CONNECTIONS)
            landmarks = hand_landmarks.landmark

            # Get tip landmarks
            thumb_tip = landmarks[4]
            index_tip = landmarks[8]
            middle_tip = landmarks[12]
            ring_tip = landmarks[16]
            pinky_tip = landmarks[20]

            # Finger state detection
            fingers_up = [
                index_tip.y < landmarks[6].y,   # Index
                middle_tip.y < landmarks[10].y, # Middle
                ring_tip.y < landmarks[14].y,   # Ring
                pinky_tip.y < landmarks[18].y   # Pinky
            ]

            fingers_count = sum(fingers_up)
            current_time = time.time()

            # 👋 Play: all fingers up
            if fingers_count == 4:
                if prev_gesture != "play" and current_time - gesture_time > 1:
                    pyautogui.press('space')
                    print(f"{label} Hand - Play")
                    prev_gesture = "play"
                    gesture_time = current_time

            # ✊ Pause: 0 fingers up
            elif fingers_count == 0:
                if prev_gesture != "pause" and current_time - gesture_time > 1:
                    pyautogui.press('space')
                    print(f"{label} Hand - Pause")
                    prev_gesture = "pause"
                    gesture_time = current_time

            # ☝️ 1 Finger (Index only) → Forward
            elif fingers_up[0] and not any(fingers_up[1:]):
                if current_time - gesture_time > 0.4:
                   pyautogui.press('right')
                   print(f"{label} Hand - Forward 10s")
                   prev_gesture = "forward"
                   gesture_time = current_time

 
               # ✌️ 2 Fingers (Index + Middle) → Rewind
            elif fingers_up[0] and fingers_up[1] and not any(fingers_up[2:]):
                if current_time - gesture_time > 0.4:
                    pyautogui.press('left')
                    print(f"{label} Hand - Rewind 10s")
                    prev_gesture = "rewind"
                    gesture_time = current_time


    # Display Camera Feed
    cv2.imshow("Hand Gesture YouTube Controller", img)

    # Exit on 'q' key
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
