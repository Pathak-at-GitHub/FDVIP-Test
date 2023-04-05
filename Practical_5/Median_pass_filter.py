import cv2
from matplotlib import pyplot as plt
import numpy as np
img=cv2.imread('The-original-cameraman-image.png',0)
#Low pass
# kernel=np.array([[1,1,1,1,1],[1,1,1,1,1],[1,1,1,1,1],[1,1,1,1,1],[1,1,1,1,1]])
# kernel2=np.array([[1,1,1],[1,1,1],[1,1,1]])
# kernel1=kernel2/sum(kernel2)
# kernel2=kernel/sum(kernel)
# img_fil=cv2.filter2D(img,-1,kernel1)
# img_fil2=cv2.filter2D(img,-1,kernel2)
# cv2.imshow('original',img)
# cv2.imshow('filtered 3by3',img_fil)
# cv2.imshow('filtered 5by5',img_fil2)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# High pass filter
# kernel=np.array([[0,-1,0],[-1,4,-1],[0,-1,0]])
# kernel2=np.array([[-1, -1, -1, -1, -1],
# [-1, 1, 2, 1, -1],
# [-1, 2, 4, 2, -1],
# [-1, 1, 2, 1, -1],
# [-1, -1, -1, -1, -1]])
# kernel2=kernel2/(np.sum(kernel2) if np.sum(kernel2)!=0 else 1)
# kernel=kernel/(np.sum(kernel) if np.sum(kernel)!=0 else 1)
# img_fil=cv2.filter2D(img,-1,kernel)
# img_fil2=cv2.filter2D(img,-1,kernel2)
# cv2.imshow('original',img)
# cv2.imshow('filtered 3by3',img_fil)
# cv2.imshow('filtered 5by5',img_fil2)
# cv2.waitKey(0)
# cv2.destroyAllWindows()


#Median Filter
img=cv2.imread('The-original-cameraman-image.png',0)
m,n = img.shape
img_new1 = np.zeros([m, n])
for i in range(1, m - 1):
    for j in range(1, n - 1):
        temp = [img[i - 1, j - 1],
                img[i - 1, j],
                img[i - 1, j + 1],
                img[i, j - 1],
                img[i, j],
                img[i, j + 1],
                img[i + 1, j - 1],
                img[i + 1, j],
                img[i + 1, j + 1]]

        temp = sorted(temp)
        img_new1[i, j] = temp[4]

img_new1 = img_new1.astype(np.uint8)
cv2.imshow('Original',img)
cv2.imshow('Median Filtered',img_new1)
cv2.waitKey(0)
cv2.destroyAllWindows()