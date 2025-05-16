import cv2

# Open the webcam
video_cap = cv2.VideoCapture(0)
face_cap = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

while True:
    # Read a frame from the webcam
    ret, frame = video_cap.read()
    col = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    faces = face_cap.detectMultiScale(
        col,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30, 30),
        flags = cv2.CASCADE_SCALE_IMAGE
    )
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
    # Check if the frame was successfully captured
    if not ret:
        print("Failed to grab frame")
        break

    # Display the frame
    cv2.imshow("video_live", frame)

    # Exit on 'q' key
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the camera and close all OpenCV windows
video_cap.release()


