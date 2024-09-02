import cv2
import dlib
import face_recognition
import numpy as np
from google.colab.patches import cv2_imshow  # for displaying images in Colab



from google.colab import files
uploaded = files.upload()  # This will prompt you to upload files
img_path = 'cr7.jpg'
img = cv2.imread(img_path)
# Load Haar Cascade Classifier
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Convert to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Detect faces
faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)

# Draw rectangles around faces
for (x, y, w, h) in faces:
    cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)

# Display the image
cv2_imshow(img)
# Load dlib's face detector
detector = dlib.get_frontal_face_detector()

# Detect faces
faces = detector(gray)

# Draw rectangles around faces
for face in faces:
    x, y, w, h = (face.left(), face.top(), face.width(), face.height())
    cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)

# Display the image
cv2_imshow(img)
known_image = face_recognition.load_image_file("zidane.jpg")
known_encoding = face_recognition.face_encodings(known_image)[0]

unknown_image = face_recognition.load_image_file("anthony.jpg")
unknown_encoding = face_recognition.face_encodings(unknown_image)[0]

results = face_recognition.compare_faces([known_encoding], unknown_encoding)

if results[0]:
    print("It's a match!")
else:
    print("No match found.")
