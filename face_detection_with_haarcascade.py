import cv2

# Use a raw string to specify the correct file path to the Haar Cascade XML file
cascade_face = cv2.CascadeClassifier(r"D:/Project Archive/Python Mini Projects/Face Recognition Project/haarcascade_frontalface_default.xml")

# Initialize the video capture
cap = cv2.VideoCapture(0)

# Check if the cascade classifier loaded correctly
if cascade_face.empty():
    print("Error: Could not load face cascade classifier.")
    exit()

# Main loop to capture frames and detect faces
while True:
    ret, img = cap.read()
    if not ret:
        print("Failed to capture image")
        break
    
    # Convert the image to grayscale
    g = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    # Detect faces
    f = cascade_face.detectMultiScale(g, 1.3, 6)
    
    # Draw rectangles around detected faces
    for (x, y, w, h) in f:
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
    
    # Display the image with detected faces
    cv2.imshow('Face Detection', img)
    
    # Break the loop if the 'Esc' key is pressed
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break

# Release resources and close windows
cap.release()
cv2.destroyAllWindows()
