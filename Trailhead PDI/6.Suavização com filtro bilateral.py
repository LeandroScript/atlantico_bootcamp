import numpy as np
import cv2

img = cv2.imread('imgs/Ponte.jpg')
img = img[::2, ::2]
suave = np.vstack([
    np.hstack([img,
    cv2.bilateralFilter(img,  3, 21, 21)]),
    np.hstack([cv2.bilateralFilter(img,  5, 35, 35),
    cv2.bilateralFilter(img,  7, 49, 49)]),
    np.hstack([cv2.bilateralFilter(img,  9, 63, 63),
    cv2.bilateralFilter(img, 11, 77, 77)])
])

cv2.imshow("Original and smoothed by bilateral filter images", suave)
