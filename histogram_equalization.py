import cv2
import numpy as np
from matplotlib import pyplot as plt

def histogram_equalization(image_path):
    img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

    equ = cv2.equalizeHist(img)

    plt.figure(figsize=(10, 5))
    plt.subplot(1, 2, 1)
    plt.imshow(img, cmap='gray')
    plt.title('Original Image')
    plt.xticks([])
    plt.yticks([])

    plt.subplot(1, 2, 2)
    plt.imshow(equ, cmap='gray')
    plt.title('Histogram Equalized Image')
    plt.xticks([])
    plt.yticks([])

    plt.show()

image_path = 'image.png'
histogram_equalization(image_path)
