import cv2

image1 = cv2.imread('Img6.png',0)
image1 = cv2.resize(image1,(512,512))
cv2.imshow("image 1", image1)
cv2.waitKey(0)

image2 = cv2.imread('Img5.png',0)
image2 = cv2.resize(image2 ,(512,512))
cv2.imshow("image 2", image2)
cv2.waitKey(0)

Bit_and = cv2.bitwise_and(image1, image2)
cv2.imshow('b_a',Bit_and)
cv2.waitKey(0)

Bit_Or = cv2.bitwise_or(image1, image2)
cv2.imshow('b_a',Bit_Or)
cv2.waitKey(0)

Bit_xor = cv2.bitwise_xor(image1, image2)
cv2.imshow('b_a',Bit_xor)
cv2.waitKey(0)

Bit_not = cv2.bitwise_not(image1)
cv2.imshow('b_a',Bit_not)
cv2.waitKey(0)




cv2.destroyAllWindows()

