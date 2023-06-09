import cv2 as cv
import numpy as np

from matplotlib import pyplot as plt
img = cv.imread('line.jpg', cv.IMREAD_GRAYSCALE)
assert img is not None, "file could not be read"
edges = cv.Canny(img, 100, 200)
plt.subplot(121), plt.imshow(img, cmap='gray')
plt.title("Original Images"), plt.xticks([]), plt.yticks([])
plt.subplot(122), plt.imshow(edges, cmap='gray')
plt.title("Edge Image"), plt.xticks([]), plt.yticks([])
plt.show()