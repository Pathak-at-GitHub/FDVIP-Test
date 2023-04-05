import cv2
import numpy as np
image = cv2.imread('Img1.jpg',0)
binr = cv2.threshold(image, 0, 255,cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]

kernel = np.ones((3,3),np.uint8)

invert = cv2.bitwise_not(binr)

dilation = cv2.dilate(invert, kernel, iterations=1)

# dilation1 = cv2.dilate(invert, kernel, iterations=2)
# dilation2 = cv2.dilate(invert, kernel, iterations=3)
# dilation3 = cv2.dilate(invert, kernel, iterations=4)

# cv2.imshow("Dilation1 Image",dilation1)
# cv2.imshow("Dilation2 Image",dilation2)
# cv2.imshow("Dilation3 Image",dilation3)

cv2.imshow("Dilation Image",dilation)
cv2.imshow("Inverted image", invert)
cv2.waitKey(0)

cv2.destroyAllWindows()

