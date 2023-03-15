import cv2
import numpy as np
flag = 1
image = cv2.imread('wallpaper.jpg', flag)

cv2.imshow('color', image)

cv2.imwrite('wallpaper.jpg',image)
## rotate right left 👇
cv2.rotate(image, cv2.ROTATE_90_CLOCKWISE)
cv2.rotate(image, cv2.ROTATE_90_COUNTERCLOCKWISE)
cv2.rotate(image, cv2.ROTATE_180)


cv2.waitKey(0)
cv2.destroyAllWindows()
