import cv2
import PIL
import numpy as np

image  = cv2.imread('Img8.png',0)
cv2.imshow("original_image", image)
cv2.waitKey(0)
[w,h] = image.shape

## with out background
for i in range(0, w):
    for j in range(0, h):
        if image[i][j] > 100 and image[i][j] <200:
            image[i][j] = 210

cv2.imshow('R_image', image)
cv2.waitKey(0)

image2  = cv2.imread('Img8.png',0)
cv2.imshow("original_image_1", image2)
cv2.waitKey(0)
[w,h] = image.shape
## With background
for i in range(0,w):
    for j in range(0,h):
        if image2[i][j]>100 and image2[i][j]<200:
            image2[i][j] = 255
        else:
            image2[i][j] = 0

cv2.imshow('R_image_1', image2)
cv2.waitKey(0)
cv2.destroyAllWindows()

