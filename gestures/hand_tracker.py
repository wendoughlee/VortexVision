# gestures/hand_tracker.py

import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import cv2
import mediapipe as mp
from osc.send_gestures import send_gesture

# 👇 everything else stays the same
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(max_num_hands=1)
mp_draw = mp.solutions.drawing_utils

cap = cv2.VideoCapture(0)
prev_x = None

while cap.isOpened():
    success, frame = cap.read()
    if not success:
        continue

    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = hands.process(rgb)

    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            mp_draw.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

            x = hand_landmarks.landmark[0].x
            
            if prev_x is not None:
                delta_x = x - prev_x
                if delta_x < -0.05:
                    print("Swipe Left")
                    send_gesture("swipe_left")
                    prev_x = None
                elif delta_x > 0.05:
                    print("Swipe Right")
                    send_gesture("swipe_right")
                    prev_x = None
            prev_x = x

    cv2.imshow('Hand Tracking', frame)
    if cv2.waitKey(5) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()
