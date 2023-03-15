import cv2
import numpy as np
flag = 1
image = cv2.imread("9djykkt41ai91.jpg", flag)

cv2.imshow("Color", image)

cv2.imwrite("9djykkt41ai91.png", image)
cv2.waitKey(12)
cv2.destroyAllWindows()

