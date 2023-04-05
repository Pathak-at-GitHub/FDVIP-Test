import matplotlib.pyplot as plt
import matplotlib.image as img

# reading the image
testImage = img.imread('The-original-cameraman-image.png')

# displaying the image
plt.imshow(testImage)