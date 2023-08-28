import cv2
import numpy as np

# Cargar imagen en escala de grises
img = cv2.imread("flor2.jpg")
img = cv2.resize(img,(600,400))

# Kernel
kernel_x = np.array([[1, -1, 0]], dtype=np.float32)
kernel_y = np.array([[0, 0, 0]], dtype=np.float32)

# Filtro
sobel_x = cv2.filter2D(img, -1, kernel_x)
sobel_y = cv2.filter2D(img, -1, kernel_y)
sobel = cv2.addWeighted(sobel_x, 0.5, sobel_y, 0.5, 0)
sobel_norm = cv2.normalize(sobel, None, 0, 255, cv2.NORM_MINMAX, cv2.CV_8U)

# Mostrar resultados
print(kernel_y)

cv2.imshow('Original', img)
cv2.imshow('filtro', sobel_norm)
cv2.waitKey(0)
cv2.destroyAllWindows()