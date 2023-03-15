import cv2
import PIL
import numpy as np

image1 = cv2.imread('Img4.jpg')
image1 = cv2.resize(image1,(512,512))

Img = cv2.imread('Img7.png')


## For Digital_negative
image2 = abs(255-image1)

## for log transformation
c = 255/(np.log(1+ np.max(image1)))
image3 = c * (np.log(image1+1))
image3 = np.array(image3, dtype=np.uint8)

## for Gamma transformation
# Apply Gamma=2.2 on the normalised image and then multiply by scaling constant (For 8 bit, c=255)
gamma_two_point_two = np.array(255*(Img/255)**2.2,dtype='uint8')
# Similarly, Apply Gamma=0.4
gamma_point_four = np.array(255*(Img/255)**0.5,dtype='uint8')
# Display the images in subplots



cv2.imshow("image1", image1)
cv2.waitKey(0)
cv2.imshow("image2", image2)
cv2.waitKey(0)
cv2.imshow("image3", image3)
cv2.waitKey(0)
cv2.imshow("image4", gamma_two_point_two)
cv2.waitKey(0)
cv2.imshow("IMG", Img)
cv2.waitKey(0)
cv2.imshow("image5", gamma_point_four)
cv2.waitKey(0)


cv2.destroyAllWindows()



