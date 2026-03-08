import cv2
import face_recognition
import numpy as np

def capture_face_encoding(emp_name):
    cap = cv2.VideoCapture(0)
    encoding = None

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        cv2.imshow(f"Capturing Face - {emp_name}", frame)

        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        faces = face_recognition.face_locations(rgb_frame)

        if faces:
            encodings = face_recognition.face_encodings(rgb_frame, faces)
            encoding = encodings[0]
            break  # ✅ AUTO STOP ON FACE DETECTED

        if cv2.waitKey(1) & 0xFF == 27:
            break

    cap.release()
    cv2.destroyAllWindows()
    return encoding