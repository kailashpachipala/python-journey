import cv2
import mediapipe as mp

from mediapipe.tasks import python
from mediapipe.tasks.python import vision


# ============================================
# 1. Hand Landmarker Model
# ============================================

MODEL_PATH = "hand_landmarker.task"


# ============================================
# 2. Create Hand Landmarker
# ============================================

base_options = python.BaseOptions(
    model_asset_path=MODEL_PATH
)

options = vision.HandLandmarkerOptions(
    base_options=base_options,
    running_mode=vision.RunningMode.IMAGE,
    num_hands=2,
    min_hand_detection_confidence=0.5,
    min_hand_presence_confidence=0.5,
    min_tracking_confidence=0.5
)

detector = vision.HandLandmarker.create_from_options(options)


# ============================================
# 3. Finger Tip IDs
# ============================================

# Thumb  = 4
# Index  = 8
# Middle = 12
# Ring   = 16
# Pinky  = 20

tip_ids = [4, 8, 12, 16, 20]


# ============================================
# 4. Open Webcam
# ============================================

cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Error: Cannot open webcam")
    exit()


# ============================================
# 5. Main Loop
# ============================================

while True:

    success, frame = cap.read()

    if not success:
        print("Error: Cannot read webcam frame")
        break

    # Mirror the webcam
    frame = cv2.flip(frame, 1)

    # Get frame dimensions
    height, width, _ = frame.shape

    # ========================================
    # Convert OpenCV BGR -> RGB
    # ========================================

    rgb_frame = cv2.cvtColor(
        frame,
        cv2.COLOR_BGR2RGB
    )


    # ========================================
    # Convert to MediaPipe Image
    # ========================================

    mp_image = mp.Image(
        image_format=mp.ImageFormat.SRGB,
        data=rgb_frame
    )


    # ========================================
    # Detect Hands
    # ========================================

    result = detector.detect(mp_image)


    # Total fingers from both hands
    total_fingers = 0


    # ========================================
    # Check if hands are detected
    # ========================================

    if result.hand_landmarks:

        for hand_index, hand_landmarks in enumerate(
            result.hand_landmarks
        ):

            # --------------------------------
            # Get hand label
            # --------------------------------

            hand_label = result.handedness[
                hand_index
            ][0].category_name


            # --------------------------------
            # Store landmark coordinates
            # --------------------------------

            landmarks = []

            for landmark in hand_landmarks:

                x = int(landmark.x * width)
                y = int(landmark.y * height)

                landmarks.append((x, y))


            # =================================
            # Thumb Detection
            # =================================

            if hand_label == "Right":

                if landmarks[4][0] < landmarks[3][0]:
                    total_fingers += 1

            else:

                if landmarks[4][0] > landmarks[3][0]:
                    total_fingers += 1


            # =================================
            # Index, Middle, Ring, Pinky
            # =================================

            for finger in range(1, 5):

                tip = tip_ids[finger]

                pip = tip - 2

                if landmarks[tip][1] < landmarks[pip][1]:
                    total_fingers += 1


            # =================================
            # Draw Hand Landmarks
            # =================================

            for landmark in hand_landmarks:

                x = int(landmark.x * width)
                y = int(landmark.y * height)

                cv2.circle(
                    frame,
                    (x, y),
                    5,
                    (0, 255, 0),
                    -1
                )


            # =================================
            # Draw Connections
            # =================================

            connections = [
                (0, 1), (1, 2), (2, 3), (3, 4),
                (0, 5), (5, 6), (6, 7), (7, 8),
                (0, 9), (9, 10), (10, 11), (11, 12),
                (0, 13), (13, 14), (14, 15), (15, 16),
                (0, 17), (17, 18), (18, 19), (19, 20),
                (5, 9), (9, 13), (13, 17)
            ]

            for start, end in connections:

                x1, y1 = landmarks[start]
                x2, y2 = landmarks[end]

                cv2.line(
                    frame,
                    (x1, y1),
                    (x2, y2),
                    (255, 0, 0),
                    2
                )


            # =================================
            # Display Left / Right
            # =================================

            wrist_x, wrist_y = landmarks[0]

            cv2.putText(
                frame,
                hand_label,
                (wrist_x - 30, wrist_y - 20),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.8,
                (255, 255, 0),
                2
            )


    # =========================================
    # Display Finger Count
    # =========================================

    cv2.putText(
        frame,
        f"Fingers: {total_fingers}",
        (20, 60),
        cv2.FONT_HERSHEY_SIMPLEX,
        1.8,
        (0, 255, 0),
        3
    )


    # =========================================
    # Display Instructions
    # =========================================

    cv2.putText(
        frame,
        "Press Q to Quit",
        (20, height - 20),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.7,
        (255, 255, 255),
        2
    )


    # =========================================
    # Show Webcam
    # =========================================

    cv2.imshow(
        "MediaPipe Tasks - Finger Counter",
        frame
    )


    # =========================================
    # Quit
    # =========================================

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break


# ============================================
# 6. Release Resources
# ============================================

cap.release()

cv2.destroyAllWindows()

detector.close()