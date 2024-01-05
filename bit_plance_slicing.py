import numpy as np
import matplotlib.pyplot as plt
import cv2

image = cv2.imread('image.png', cv2.IMREAD_GRAYSCALE)

def bit_plane_slicing(image):
    rows, cols = image.shape
    planes = [np.zeros((rows, cols), dtype=np.uint8) for _ in range(8)]

    for i in range(8):
        planes[i] = (image >> i) & 1
        planes[i] *= 255

    return planes

bit_planes = bit_plane_slicing(image)

plt.figure(figsize=(12, 8))
plt.subplot(3, 3, 1)
plt.imshow(image, cmap='gray')
plt.title('Original Image')
plt.axis('off')

for i, plane in enumerate(bit_planes):
    plt.subplot(3, 3, i+2)
    plt.imshow(plane, cmap='gray')
    plt.title(f'Bit plane {i}')
    plt.axis('off')

plt.tight_layout()
plt.show()
