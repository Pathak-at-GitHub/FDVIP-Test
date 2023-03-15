import PIL
import cv2

flag = 0
img1 = cv2.imread('Img1.jpg', flag)
img1 = cv2.resize(img1,(512,512))
cv2.imshow('Image 1',img1)
cv2.waitKey(0)

img2 = cv2.imread('Img2.jpg',flag)
img2 =cv2.resize(img2, (512,512))
cv2.imshow('Image 2', img2)
cv2.waitKey(0)

cv2.destroyAllWindows()
