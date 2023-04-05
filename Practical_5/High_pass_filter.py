import numpy as np
import cv2
from cv2 import filter2D

img = cv2.imread("The-original-cameraman-image.png")
kernel= np.array([[-1,-1,-1,-1,-1],
                    [-1,1,2,1,-1],
                    [-1,2,4,2,-1],
                    [-1,1,2,1,-1],
                    [-1,-1,-1,-1,-1]])
# kernel = np.array([[0,-1,0],
#                    [-1,4,0],
#                    [0,-1,0]])

kernel = kernel/(sum(kernel) if np.sum(kernel)!=0 else 1)

img_fil = filter2D(img, -1 , kernel)
cv2.imshow("Image",img)
cv2.imshow("Image_fil", img_fil)
cv2.waitKey()
cv2.destroyAllWindows()