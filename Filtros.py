import cv2
import numpy as np

imgsal = cv2.imread('perro.jpg')
imggau = cv2.imread('manos.jpg')

filtro_media = cv2.blur(imgsal, (5, 5))
filtro_gaussiano = cv2.GaussianBlur(imgsal, (5, 5), 0)
filtro_mediana = cv2.medianBlur(imgsal, 5)
filtro_minimo = cv2.erode(imgsal, np.ones((5, 5), np.uint8))
filtro_maximo = cv2.dilate(imgsal, np.ones((5, 5), np.uint8))

filtro_mediag = cv2.blur(imggau, (5, 5))
filtro_gaussianog = cv2.GaussianBlur(imggau, (5, 5), 0)
filtro_medianag = cv2.medianBlur(imggau, 5)
filtro_minimog = cv2.erode(imggau, np.ones((5, 5), np.uint8))
filtro_maximog= cv2.dilate(imggau, np.ones((5, 5), np.uint8))

cv2.imshow('Original Sal y Pimienta', imgsal)
cv2.imshow('Filtro media Sal y Pimienta', filtro_media)
cv2.imshow('Filtro Gaussiano Sal y Pimienta', filtro_gaussiano)
cv2.imshow('Filtro mediana Sal y Pimienta', filtro_mediana)
cv2.imshow('Filtro minimo Sal y Pimienta', filtro_minimo)
cv2.imshow('Filtro maximo Sal y Pimienta', filtro_maximo)

cv2.imshow('Original Gaussiano', imggau)
cv2.imshow('Filtro media Gaussiano', filtro_mediag)
cv2.imshow('Filtro Gaussiano Gaussiano', filtro_gaussianog)
cv2.imshow('Filtro mediana Gaussiano', filtro_medianag)
cv2.imshow('Filtro minimo Gaussiano', filtro_minimog)
cv2.imshow('Filtro maximo Gaussiano', filtro_maximog)

cv2.waitKey(0)
cv2.destroyAllWindows()
