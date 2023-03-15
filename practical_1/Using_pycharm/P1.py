import cv2
import numpy as np

## Importing open CV Library
#How to read a image

flag = 1

image = cv2.imread('9djykkt41ai91.jpg',flag )

(h,w,d) = image.shape


print('width = {},Height = {}, depth = {}'.format(w,h,d))

#instead or infinite loop we
cv2.imshow("color", image)
cv2.waitKey(0)

## following line is important for terminating
# program exe using any keybord key
cv2.destroyAllWindows()

# while True:


