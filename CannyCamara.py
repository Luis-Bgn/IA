import cv2 
import numpy as np  # np es un alias para la libreria de numpy
  
cap = cv2.VideoCapture(0)  

def nothing(x):
	pass

#create a seperate window named 'controls' for trackbar
cv2.namedWindow('controls')
#create trackbar in 'controls' window with name 'r''
cv2.createTrackbar('minx','controls',15,300,nothing)
cv2.createTrackbar('maxx','controls',15,300,nothing)

while True:
    ret, frame = cap.read()
    
    minx= int(cv2.getTrackbarPos('minx','controls'))
    maxx= int(cv2.getTrackbarPos('maxx','controls'))
    
    edges = cv2.Canny(frame,minx,maxx,L2gradient=False) # Argumento imagen de entrada. Argumento2 umbral  minval. Argumento 3: umbral maxVal. Argumento 4: Tipo de norma L2gradient
    
    ctns, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
    cv2.drawContours(frame, ctns, -1, (0,0,255), 2)
    texto = 'Contornos: '+ str(len(ctns))
    cv2.putText(frame, texto, (50,50), cv2.FONT_HERSHEY_SIMPLEX, 1,(0, 0, 0), 2)
    
    cv2.imshow('Original',frame)
    cv2.imshow('Edges',edges)
    if  cv2.waitKey(5) & 0xFF == 27: # Al presionar 'Esc' se sale del While y deja de capturar frames
        break
cap.release()  # Libera (desactiva la camara)
cv2.destroyAllWindows()   # cierra toda las ventanas
