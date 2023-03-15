import PIL
import cv2

flag = 0
image1 = cv2.imread('Img1.jpg', flag)
image1 = cv2.resize(image1, (512,512))
cv2.imshow('image',image1)
cv2.waitKey(0)

image2 = cv2.imread('Img2.jpg', flag)
image2 = cv2.resize(image2,(512,512))
cv2.imshow('image 2',image2) 
cv2.waitKey(0)

sub_image = cv2.add(image2,image1)
cv2.imshow('subtracted_images',sub_image)
cv2.waitKey(0)

cv2.destroyAllWindows()



