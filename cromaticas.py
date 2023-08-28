
import cv2
import numpy as np   #Librerias utilizadas

img = cv2.imread("manos.jpg")
img = cv2.resize(img,(400,400))

img1 = np.asarray(img,dtype = np.float64)
img2 = np.asarray(img,dtype = np.float64)
img3 = np.asarray(img,dtype = np.float64)

b = img.shape[0]
g = img.shape[1]
r = img.shape[2]

crom1 = np.zeros((b, g, r),dtype = np.float64)
crom2 = np.zeros((b, g, r),dtype = np.float64)
crom3 = np.zeros((b, g, r),dtype = np.float64)

matriz1 = np.ones((img.shape[0],img.shape[1]))
matriz2 = np.ones((img.shape[0],img.shape[1]))
matriz3 = np.ones((img.shape[0],img.shape[1]))

for x in range (0,b):
    for y in range (0,g):
        for z in range(0, r):
            img2[x][y][z]=img2[x][y][z]*.5
            img3[x][y][z]=img3[x][y][z]*.3
            
            
for x in range (0,b):
    for y in range(0, g):
        for z in range(0, r):
                    
            crom1[x,y,z] = (img1[x,y,z]/(img1[x,y,0] + img1[x,y,1] + img1[x,y,2]) )*255                         
            crom2[x,y,z] = (img2[x,y,z]/(img2[x,y,0] + img2[x,y,1] + img2[x,y,2]))*255
            crom3[x,y,z] = (img3[x,y,z]/(img3[x,y,0] + img3[x,y,1] + img3[x,y,2]))*255

img1 = np.asarray(img,dtype = np.uint8)
img2 = np.asarray(img2,dtype = np.uint8)
img3 = np.asarray(img3,dtype = np.uint8)


crom1 = np.asarray(crom1,dtype = np.uint8)
crom2 = np.asarray(crom2,dtype = np.uint8)
crom3 = np.asarray(crom3,dtype = np.uint8)

#108,76,60
#108,77,72
minncb1 = np.amin(crom1[:,:,0])
maxncb1 = np.amax(crom1[:,:,0])
minncg1 = np.amin(crom1[:,:,1])
maxncg1 = np.amax(crom1[:,:,1])
minncr1 = np.amin(crom1[:,:,2])
maxncr1 = np.amax(crom1[:,:,2])

for x in range (0,b):
    for y in range(0, g):
       
       
        if(crom1[x,y,0] > maxncb1 -6 or crom1[x,y,1] > maxncg1 -4 or crom1[x,y,2] < minncr1 + 2):
            matriz1[x,y]  = 0
            
        if(crom2[x,y,0] > maxncb1 -4 or crom2[x,y,1] > maxncg1 -4 or crom2[x,y,2] < minncr1 + 2):
            matriz2[x,y]  = 0
            
        if(crom3[x,y,0] > maxncb1 -4 or crom3[x,y,1] > maxncg1 -4 or crom3[x,y,2] < minncr1 + 2):
            matriz3[x,y]  = 0
        
original = cv2.hconcat([img1,img2,img3])
cv2.imwrite("original.jpg",original)

cromatica = cv2.hconcat([crom1, crom2, crom3])
cv2.imwrite("cromatica.jpg",cromatica)

filtro = cv2.hconcat([matriz1, matriz2, matriz3])
cv2.imshow("filtro", filtro)
cv2.imwrite("filtro.jpg", filtro)

f1 = cv2.vconcat([original, cromatica])
cv2.imshow("final", f1)

cv2.waitKey(0)                         
cv2.destroyAllWindows()  