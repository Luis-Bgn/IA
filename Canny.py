import numpy as np
import cv2

img = cv2.imread('manos.jpg', cv2.IMREAD_GRAYSCALE)

#trackbar callback fucntion does nothing but required for trackbar
def nothing(x):
	pass

#create a seperate window named 'controls' for trackbar
cv2.namedWindow('controls')
#create trackbar in 'controls' window with name 'r''
cv2.createTrackbar('minx','controls',15,300,nothing)
cv2.createTrackbar('maxx','controls',15,300,nothing)

#create a while loop act as refresh for the view 
while(1):
	#returns current position/value of trackbar 
    minx= int(cv2.getTrackbarPos('minx','controls'))
    maxx= int(cv2.getTrackbarPos('maxx','controls'))
    
    edges = cv2.Canny(img,minx,maxx)
    imagen=cv2.hconcat([img,edges]) 
    
    ctns, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
    cv2.drawContours(imagen, ctns, -1, (0,0,255), 2)
    texto = 'Contornos: '+ str(len(ctns))
    cv2.putText(imagen, texto, (10,20), cv2.FONT_HERSHEY_SIMPLEX, 0.7,(0, 0, 0), 1)
    
    cv2.imshow('canny',imagen)
	# waitfor the user to press escape and break the while loop 
    k = cv2.waitKey(1) & 0xFF
    if k == 27:
        break
		
#destroys all window
cv2.destroyAllWindows()
