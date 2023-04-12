import cv2
import numpy as np

img = cv2.imread("line_image.jpg", 0)
cv2.imshow("Original", img)
kernel = np.ones((10,2), np.uint8)
verticalLines = cv2.erode(img, kernel, iterations=1)
cv2.imshow('output', verticalLines)
cv2.waitKey(0)
cv2.destroyAllWindows()