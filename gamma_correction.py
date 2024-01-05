import numpy as np
import cv2
from matplotlib import pyplot as plt

def adjust_gamma(image, gamma=1.0):
    invGamma = 1.0 / gamma
    table = np.array([((i / 255.0) ** invGamma) * 255
                      for i in np.arange(0, 256)]).astype("uint8")

    return cv2.LUT(image, table)

image = cv2.imread('image.png')
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

gamma_values = [0.5, 1.0, 1.5, 2.0]
images = []

for gamma in gamma_values:
    adjusted = adjust_gamma(image, gamma=gamma)
    images.append(adjusted)

fig, axs = plt.subplots(1, 4, figsize=(20, 5))

for i, img in enumerate(images):
    axs[i].imshow(img)
    axs[i].set_title(f"Gamma: {gamma_values[i]}")
    axs[i].axis('off')

plt.show()
