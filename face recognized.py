import cv2
import face_recognition

known_image = face_recognition.load_image_file("c:\Users\ASUS\OneDrive\Pictures\Camera Roll\WIN_20250412_22_03_18_Pro.jpg")
known_encoding = face_recognition.face_encodings(known_image)[0]

video_capture = cv2.VideoCapture(0)

while True:
    # Capture frame-by-frame
    ret, frame = video_capture.read()

    if not ret:
        print("Failed to capture frame. Exiting...")
        break

    # Inside the detection loop:
    rgb_frame = frame[:, :, ::-1]  # Convert BGR to RGB
    face_locations = face_recognition.face_locations(rgb_frame)
    face_encodings = face_recognition.face_encodings(rgb_frame, face_locations)
    for (top, right, bottom, left), encoding in zip(face_locations, face_encodings):
        match = face_recognition.compare_faces([known_encoding], encoding)
        if match[0]:
            cv2.putText(frame, "Known Person", (left, top-10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)
    for encoding in face_encodings:
        match = face_recognition.compare_faces([known_encoding], encoding)
        if match[0]:
            cv2.putText(frame, "Known Person", (left, top-10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)

while True:
    # Capture frame-by-frame
    ret, frame = video_capture.read()

    if not ret:
        print("Failed to capture frame. Exiting...")
        break

    # Display the frame
    cv2.imshow("Video", frame)

    # Break the loop on 'q' key press
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the capture and close windows
video_capture.release()
cv2.destroyAllWindows()