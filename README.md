# Real-Time Face Detection with OpenCV

This project performs real-time face detection using OpenCV's Haar Cascade Classifier. It captures video from a webcam, detects faces in each frame, and highlights them with green rectangles.

## Features

- Uses the **Haar Cascade Classifier** for face detection.
- Processes frames in real-time from the webcam.
- Highlights detected faces with rectangles for easy visualization.

## Prerequisites

- Python 3.x
- OpenCV (`opencv-python`)

## Usage

1. Make sure your webcam is connected.
2. Run the script, and a window will open, showing the webcam feed with detected faces highlighted.
3. Press the **Esc key** to exit the program.

## Code Description

- `cv2.CascadeClassifier` loads the pre-trained Haar Cascade model for face detection.
- `cv2.VideoCapture(0)` initializes the webcam for capturing video.
- The program converts each frame to grayscale for better detection accuracy.
- `detectMultiScale` detects faces and returns the coordinates, which are used to draw rectangles around each detected face.

## Screenshot

![Face Detection in Action](https://github.com/beraswapnil/Face-Recognition-Project/blob/8047514ee9262917b33becee8fe33bfa7b86d13b/face_detection_output.png)

## Troubleshooting

- **Unable to load Haar Cascade file**: Ensure that `haarcascade_frontalface_default.xml` is in the correct directory and that the path is correctly specified in the script.
- **No webcam detected**: Make sure your webcam is properly connected and enabled.

## Acknowledgments

- OpenCV team for providing pre-trained Haar Cascades.
- [OpenCV Documentation](https://docs.opencv.org/) for in-depth explanations and guides.
