import cv2
img = cv2.imread('imgs/Ponte.jpg')
(canalAzul, canalVerde, canalVermelho) = cv2.split(img)
cv2.imshow("Vermelho", canalVermelho)
cv2.imshow("Verde", canalVerde)
cv2.imshow("Azul", canalAzul)
cv2.waitKey(0)

resultado = cv2.merge([canalAzul, canalVerde, canalVermelho])

import numpy as np 
import cv2
img = cv2.imread('imgs/Ponte.jpg')
(canalAzul, canalVerde, canalVermelho) = cv2.split(img)
zeros = np.zeros(img.shape[:2], dtype = "uint8")
cv2.imshow("Vermelho", cv2.merge([zeros, zeros, canalVermelho]))
cv2.imshow("Verde", cv2.merge([zeros, canalVerde, zeros]))
cv2.imshow("Azul", cv2.merge([canalAzul, zeros, zeros]))
cv2.imshow("Original", img)
cv2.waitKey(0)

