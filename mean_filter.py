import cv2
import numpy as np
import matplotlib.pyplot as plt

def apply_mean_filter(image_path, kernel_size):

    image = cv2.imread(image_path, 0)  # 0 to read image in grayscale mode

    kernel = np.ones((kernel_size, kernel_size), np.float32) / kernel_size**2
    
    mean_filtered_image = cv2.filter2D(image, -1, kernel)
    
    plt.figure(figsize=(10, 5))
    plt.subplot(1, 2, 1), plt.imshow(image, cmap='gray'), plt.title('Original Image'), plt.axis('off')
    plt.subplot(1, 2, 2), plt.imshow(mean_filtered_image, cmap='gray'), plt.title('Mean Filtered Image'), plt.axis('off')
    plt.show()


apply_mean_filter('image.png', 5)

