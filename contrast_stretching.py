from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

def contrast_stretching(img, lower_percentile, upper_percentile):

    img_array = np.asarray(img)

    lower_bound = np.percentile(img_array, lower_percentile)
    upper_bound = np.percentile(img_array, upper_percentile)

    stretched_img = np.clip((img_array - lower_bound) / (upper_bound - lower_bound) * 255, 0, 255).astype(np.uint8)

    stretched_img = Image.fromarray(stretched_img)

    return stretched_img


img_path = 'image.png'
original_img = Image.open(img_path)

stretched_img = contrast_stretching(original_img, 5, 95)

plt.figure(figsize=(12, 6))
plt.subplot(1, 2, 1)
plt.imshow(original_img, cmap='gray')
plt.title('Original Image')
plt.axis('off')

plt.subplot(1, 2, 2)
plt.imshow(stretched_img, cmap='gray')
plt.title('Contrast Stretched Image')
plt.axis('off')

plt.show()
