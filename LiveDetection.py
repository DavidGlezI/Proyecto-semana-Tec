
import cv2

def resize(img,new_width=500):
    height,width,_ = img.shape
    ratio = height/width
    new_height = int(ratio*new_width)
    return cv2.resize(img,(new_width,new_height)) #Función para ajustar el tamaño del rectángulo a tiempo real frame por frame

face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_alt.xml") #Utilizamos el algoritmo de haarcascade en la variable

cap = cv2.VideoCapture(0)

while True:
    _,frame = cap.read()
    frame = resize(frame)
    detections = face_cascade.detectMultiScale(frame,scaleFactor=1.1,minNeighbors=6) #Leemos y detectamos la cara en tiempo real 

    for face in detections:
        x,y,w,h = face #Obtenemos la posición y medidas del rectángulo formado al detectar la cara 

        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,0,0),-1) #Utilizamos la misma línea de código que modificamos en la de detección de fotos para modificar el GaussianBlur original

        cv2.imshow("output",frame)

    if cv2.waitKey(1) & 0xFF == ord("a"):
        break

cap.release()
cv2.destroyAllWindows() #Cerramos todas las ventanas y liberamos la webcam al salir del loop.
