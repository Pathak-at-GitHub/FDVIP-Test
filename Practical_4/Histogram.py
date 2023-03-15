import cv2
from matplotlib import pyplot as plt

image = cv2.imread('..\IMAGES\Img3.jpg',0)
cimage = cv2.imread('..\IMAGES\Img3.jpg')


hist = cv2.calcHist([image], [0], None, [256], [0,256])
chist = cv2.calcHist([cimage], [0], None, [256], [0,256])

fig, axis = plt.subplots(1,2)


plt.title("Image")
plt.xlabel('bins')
plt.ylabel('No. of pixels')


axis[0].plot(hist)
axis[1].plot(chist)


cv2.imshow("Image", image)
cv2.imshow("cImage", cimage)
plt.show()
cv2.destroyAllWindows()
