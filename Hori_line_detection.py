import cv2
import numpy as np

img = cv2.imread("line_image.jpg")
cv2.imshow('original', img)

kernel = np.ones((2, 19), np.uint8)
horizontal_lines = cv2.erode(img, kernel, iterations=1)
cv2.imshow('output', horizontal_lines)

cv2.waitKey(0)
cv2.destroyAllWindows()