import cv2
import numpy as np
from matplotlib import pyplot as plt

image = cv2.imread('image.png', 0)  # Load as grayscale

kernel = np.ones((5, 5), np.uint8)

opening = cv2.morphologyEx(image, cv2.MORPH_OPEN, kernel)

closing = cv2.morphologyEx(image, cv2.MORPH_CLOSE, kernel)

plt.subplot(131), plt.imshow(image, cmap='gray'), plt.title('Original Image')
plt.subplot(132), plt.imshow(opening, cmap='gray'), plt.title('Opening Operation')
plt.subplot(133), plt.imshow(closing, cmap='gray'), plt.title('Closing Operation')
plt.show()
