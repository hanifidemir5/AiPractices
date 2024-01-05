import numpy as np
import cv2
from scipy import ndimage
import matplotlib.pyplot as plt

def contraharmonic_mean_filter(image, kernel_size, q):
    image = image.astype(float)

    numerator = ndimage.generic_filter(image, lambda x: (x**q).sum(), size=kernel_size)
    denominator = ndimage.generic_filter(image, lambda x: (x**(q-1)).sum(), size=kernel_size)

    result = np.where(denominator != 0, numerator / denominator, 0)

    return result.astype(np.uint8)

image_path = 'image.png'
image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)


q_value = 1.5 
kernel_size = 3  
filtered_image = contraharmonic_mean_filter(image, kernel_size, q_value)

cv2.imwrite('image.png', filtered_image)

plt.figure(figsize=(15, 5))
plt.subplot(121), plt.imshow(image, cmap='gray'), plt.title('Original Image'), plt.axis('off')
plt.subplot(122), plt.imshow(filtered_image, cmap='gray'), plt.title('Filtered Image'), plt.axis('off')
plt.show()