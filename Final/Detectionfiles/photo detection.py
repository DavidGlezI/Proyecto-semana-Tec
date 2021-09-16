
import cv2
import numpy as np

face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_alt.xml")

img = cv2.imread("group.jpeg")

detections = face_cascade.detectMultiScale(img,scaleFactor=1.1, minNeighbors=6)

for face in detections:
    x,y,w,h = face
    cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,0),-1)

    cv2.imshow("output", img)

k = cv2.waitKey(0)
if k==27:  
    cv2.destroyAllWindows()