import cv2
import mediapipe as mp
import json

def extract_hand_landmarks(video_path, output_json="hand_data.json"):
    mp_hands = mp.solutions.hands
    hands = mp_hands.Hands(static_image_mode=False, max_num_hands=1, min_detection_confidence=0.7)
    
    cap = cv2.VideoCapture(video_path)
    frame_idx = 0
    data = {}

    while cap.isOpened():
        success, frame = cap.read()
        if not success:
            break

        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = hands.process(frame_rgb)

        frame_data = []
        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:
                landmarks = []
                for lm in hand_landmarks.landmark:
                    landmarks.append({
                        'x': lm.x,
                        'y': lm.y,
                        'z': lm.z
                    })
                frame_data.append(landmarks)

        data[str(frame_idx)] = frame_data
        frame_idx += 1

    cap.release()

    with open(output_json, 'w') as f:
        json.dump(data, f, indent=2)

    print(f"Save the coordinate hand to: {output_json}")
extract_hand_landmarks("something.mp4")
