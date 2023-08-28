import cv2

original = cv2.imread("perro.jpg")
image = original.copy()
template = cv2.imread("CaraPerro.png")

template = cv2.resize(template,(400,300))

image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
template_gray = cv2.cvtColor(template, cv2.COLOR_BGR2GRAY)

methods = [cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED, cv2.TM_CCORR, cv2.TM_CCORR_NORMED, cv2.TM_CCOEFF, cv2.TM_CCOEFF_NORMED]

for method in methods:
    res = cv2.matchTemplate(image_gray, template_gray, method=method)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
    
    if method == cv2.TM_SQDIFF or method == cv2.TM_SQDIFF_NORMED:
        x1, y1 = min_loc
        x2, y2 = min_loc[0] + template.shape[1], min_loc[1] + template.shape[0]
    else:
        x1, y1 = max_loc
        x2, y2 = max_loc[0] + template.shape[1], max_loc[1] + template.shape[0]
        
    cv2.rectangle(image, (x1, y1), (x2, y2), (0, 255, 0), 3)
    cv2.imshow("Image " + str(methods[method]),image)
    cv2.imshow("Template",template)
    image = original.copy()
    cv2.waitKey(0)
cv2.destroyAllWindows()