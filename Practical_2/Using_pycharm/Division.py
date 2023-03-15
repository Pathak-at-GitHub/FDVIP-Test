import cv2
import numpy as np

image1 = cv2.imread('Img4.jpg')
image1 = cv2.resize(image1,(512,512))
cv2.imshow("image1",image1)
cv2.waitKey(0)
div_image = cv2.divide(image1,np.ones(4), scale=1/2)
cv2.imshow("mul_image", div_image)
cv2.waitKey(0)

cv2.destroyAllWindows()