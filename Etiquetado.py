import cv2
import numpy as np

image = cv2.imread("personas.jpg")
img_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

umbral,imgMethod = cv2.threshold(img_gray, 0, 255, cv2.THRESH_OTSU)
mask = np.uint8((img_gray<umbral)*255)
cv2.imshow("mascara",mask)

numLabels, labels, stats, centroids = cv2.connectedComponentsWithStats(mask,4,cv2.CV_32S)

val_max_pix = (np.max(stats[:4][1:]))/2
pin = np.where((stats[:,4][1:]) > val_max_pix)
pin = pin[0]+1

print("Hay "+ str(len(pin))+ " objetos")
masks = []
maskf = 0;
img = image.copy()
msk = mask.copy()


for i in range(0, len(pin)):
    mask = pin[i] == labels
    masks.append(mask)
    maskf = maskf + masks[i]
    
    x = stats[pin[i], cv2.CC_STAT_LEFT]
    y = stats[pin[i], cv2.CC_STAT_TOP]
    w = stats[pin[i], cv2.CC_STAT_WIDTH]
    h = stats[pin[i], cv2.CC_STAT_HEIGHT]
    area = stats[pin[i], cv2.CC_STAT_AREA]
    (cX, cY) = centroids[pin[i]]

    cv2.rectangle(img, (x,y), (x+w, y+h), (0,255,0), 3)
    cv2.putText(img, str(i+1), (int(cX), int(cY)), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,255,0), 2, cv2.LINE_AA)
    cmask = (labels == i).astype("uint8")*255
    
    cv2.rectangle(msk, (x,y), (x+w, y+h), (255,255,255), 3)
    cv2.putText(msk, str(i+1), (int(cX), int(cY)), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,0), 2, cv2.LINE_AA)
    
cv2.imshow("Final",img)
cv2.imshow("mascara", msk)
cv2.waitKey(0)
cv2.destroyAllWindows()