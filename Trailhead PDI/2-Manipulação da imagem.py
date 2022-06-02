import cv2
imagem = cv2.imread('imgs/Ponte.jpg')
(b, g, r) = imagem[0, 0]
print('O pixel (0, 0) tem as seguintes cores:')
print('Vermelho:', r, 'Verde:', g, 'Azul:', b)

for y in range(0, imagem.shape[0]):
    for x in range(0, imagem.shape[1]):
        imagem[y, x] = (255, 0, 0)

cv2.imshow("Modified image", imagem)
cv2.waitKey(0)

image = cv2.imread('imgs/Ponte.jpg')

for y in range(0, imagem.shape[0], 10): # rows
    for x in range(0, imagem.shape[1], 10): # columns
        imagem[y:y+5, x: x+5] = (0,255,255)
cv2.imshow("Modified image", imagem)
cv2.waitKey(0)