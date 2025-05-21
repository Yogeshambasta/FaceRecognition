Project Features :

a.Accesses your system’s webcam using OpenCV

b. Detects faces in real-time

c.Draws a bounding box around detected faces

d.Uses pre-trained Haar Cascade model for face detection

e.Live video feed with face annotations

f. Exits safely on pressing q

# Live Face Detection with OpenCV

This project demonstrates real-time face detection using a webcam and OpenCV's pre-trained Haar Cascade Classifier. It captures video from your webcam, detects faces in each frame, and displays a live video feed with rectangles drawn around detected faces.

## 🔍 Features

- Real-time face detection using OpenCV
- Uses Haar Cascade Classifier (`haarcascade_frontalface_default.xml`)
- Highlights detected faces with green rectangles
- Lightweight and easy to set up


> Press `q` to quit the application

## 🛠️ Requirements

- Python 3.6+
- OpenCV (`cv2`)

## 📦 Installation

1. Clone the repository:

```bash
git clone https://github.com/your-username/face-detection-opencv.git
cd face-detection-opencv

 How It Works
The webcam is accessed using cv2.VideoCapture(0).

Each frame is converted to grayscale for face detection.

Faces are detected using haarcascade_frontalface_default.xml.

Detected faces are highlighted with green rectangles.

 Algorithm
Face Detection: Uses Haar Cascades – a machine learning-based approach where a cascade function is trained from a set of positive and negative images.


