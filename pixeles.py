import cv2
import numpy as np

img = cv2.imread("manos.jpg",cv2.IMREAD_COLOR)
img = cv2.resize(img,(400,300))
kernel = np.ones((5,5), np.uint8)
rmax = np.array([255,255,220])
rmin = np.array([0,0,0])
mask = cv2.inRange(img,rmin,rmax)

dil = cv2.dilate(mask,kernel,iterations = 3)
cont,J = cv2.findContours(dil,cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
cv2.imshow("image",img)

for con in cont:
    x,y,w,h = cv2.boundingRect(con)
    cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,255),2)

cv2.imshow("images",mask)
cv2.imshow("image",img)
cv2.waitKey(0)
cv2.destroyAllWindows