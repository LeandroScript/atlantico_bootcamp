from matplotlib import pyplot as plt
import numpy as np
import cv2
img = cv2.imread('imgs/Ponte.jpg')
cv2.imshow("Imagem Colorida", img)
channels = cv2.split(img)
colors = ("b", "g", "r")
plt.figure()
plt.title("Color Histogram")
plt.xlabel("Intensity")
plt.ylabel("# of Pixels")
for (channel, color) in zip(channels, colors):
    hist = cv2.calcHist([channel], [0], None, [256], [0, 256])
    plt.plot(hist, color = color)
    plt.xlim([0, 256])
    plt.show()