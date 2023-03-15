import cv2
import numpy as np

flag = 1
# image1 = cv2.imread('Img1.jpg', flag)
# image1 = cv2.resize(image1,(512,512))
# cv2.imshow("Image 1", image1)
# cv2.waitKey(0)

image2 = cv2.imread('Img3.jpg', flag)
image2 = cv2.resize(image2,(512,512))
cv2.imshow("Image 2", image2)
cv2.waitKey(0)

mul_image = cv2.multiply(image2,np.ones(4), scale=2)
cv2.imshow("mul_image", mul_image)
cv2.waitKey(0)

cv2.destroyAllWindows()
