import cv2
import PIL
import numpy as np

image = cv2.imread('Img7.png', 0)
[w, h] = image.shape

img1 = np.zeros([w, h, 3], dtype=np.uint8)
img2 = np.zeros([w, h, 3], dtype=np.uint8)
img3 = np.zeros([w, h, 3], dtype=np.uint8)
img4 = np.zeros([w, h, 3], dtype=np.uint8)
img5 = np.zeros([w, h, 3], dtype=np.uint8)
img6 = np.zeros([w, h, 3], dtype=np.uint8)
img7 = np.zeros([w, h, 3], dtype=np.uint8)
img8 = np.zeros([w, h, 3], dtype=np.uint8)


def bitget(nbr, pos):
    return (nbr >> pos) & 1

planes = 8

for i in range(0, w):
    for j in range(0,h):
        for p in range(planes-1, -1, -1):
            if p == 7 :
                img1[i][j] = 255* bitget(image[i][j], p)
            if p == 6 :
                img2[i][j] = 255* bitget(image[i][j], p)
            if p == 5 :
                img3[i][j] = 255* bitget(image[i][j], p)
            if p == 4 :
                img4[i][j] = 255* bitget(image[i][j], p)
            if p == 3 :
                img5[i][j] = 255* bitget(image[i][j], p)
            if p == 2 :
                img6[i][j] = 255* bitget(image[i][j], p)
            if p == 1 :
                img7[i][j] = 255* bitget(image[i][j], p)
            if p == 0 :
                img8[i][j] = 255* bitget(image[i][j], p)

            # img1[i][j] = 255* bitget(image[i][j], p)
            # cv2.imshow("image1", img1)
            # cv2.waitKey(0)
cv2.imshow("image1", img1)
cv2.imshow("image2", img2)
cv2.imshow("image3", img3)
cv2.imshow("image4", img4)
cv2.imshow("image5", img5)
cv2.imshow("image6", img6)
cv2.imshow("image7", img7)
cv2.imshow("image8", img8)

cv2.waitKey(0)

cv2.destroyAllWindows()
