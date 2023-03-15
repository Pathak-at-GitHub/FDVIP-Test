import cv2

flag = 0
image1 = cv2.imread('Img1.jpg')
image1 = cv2.resize(image1, (512,512))
cv2.imshow("Image 1",image1)
cv2.waitKey(0)

image2 = cv2.imread('Img2.jpg')
image2 = cv2.resize(image2, (512,512))
cv2.imshow("Image 2",image2)
cv2.waitKey(0)

subtracted_image = cv2.subtract(image2, image1)
cv2.imshow("sub Image", subtracted_image)
cv2.waitKey(0)



cv2.destroyAllWindows()
