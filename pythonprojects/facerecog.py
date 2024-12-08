import cv2
import face_recognition
from deepface import DeepFace
import numpy as np

# Load a sample picture and learn how to recognize it.
known_face_encodings = []
known_face_names = []

# Add sample images of known faces
known_face_encodings.append(face_recognition.face_encodings(face_recognition.load_image_file("your_face.jpg"))[0])
known_face_names.append("Your Name")

# Start webcam feed
video_capture = cv2.VideoCapture(0)

while True:
    ret, frame = video_capture.read()
    rgb_frame = frame[:, :, ::-1]  # Convert from BGR to RGB
    
    # Find all face locations and face encodings in the current frame
    face_locations = face_recognition.face_locations(rgb_frame)
    face_encodings = face_recognition.face_encodings(rgb_frame, face_locations)

    # Loop through each face found in the frame
    for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
        matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
        name = "Unknown"

        if True in matches:
            first_match_index = matches.index(True)
            name = known_face_names[first_match_index]

        # Emotion detection with DeepFace
        try:
            result = DeepFace.analyze(frame, actions=['emotion'], enforce_detection=False)
            dominant_emotion = result[0]['dominant_emotion']
            cv2.putText(frame, f"Emotion: {dominant_emotion}", (left, top-20), cv2.FONT_HERSHEY_DUPLEX, 0.6, (0, 255, 0), 1)
        except Exception as e:
            print("Error in emotion detection:", e)

        # Draw a box around the face and label it with the name
        cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)
        font = cv2.FONT_HERSHEY_DUPLEX
        cv2.putText(frame, f"{name} ({dominant_emotion})", (left + 6, bottom - 6), font, 0.5, (255, 255, 255), 1)

    # Display the resulting frame
    cv2.imshow('Video', frame)

    # Press 'q' to quit the program
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

video_capture.release()
cv2.destroyAllWindows()
