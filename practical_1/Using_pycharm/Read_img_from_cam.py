import cv2
import numpy as np

cam = cv2.VideoCapture(0)

result , image = cam.read()

if result:
    cv2.imshow('color',image)
    cv2.imwrite('new_image.png', image)

    cv2.waitKey()
    cv2.destroyAllWindows()
else:
    print("Error occurs here")

