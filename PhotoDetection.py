
import cv2
import numpy as np

face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_alt.xml") #Utilizamos el algoritmo de haarcascade en la variable

img = cv2.imread("group2.jpeg")

detections = face_cascade.detectMultiScale(img,scaleFactor=1.1, minNeighbors=6) #Toma la detección de la cara y la ajusta a una escala definida

for face in detections:
    x,y,w,h = face #Obtenemos la posición y medidas del rectángulo formado al detectar la cara 
    cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,0),-1) #Aqui cambiamos esta parte del código para formar el rectángulo negro

    cv2.imshow("output", img) 

k = cv2.waitKey(0)
if k==27:  
    cv2.destroyAllWindows() #Si se presiona la tecla esc se cierran las ventanas