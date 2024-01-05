import numpy as np
import cv2
import matplotlib.pyplot as plt

def add_salt_and_pepper_noise(image, amount, pepper_fraction):
    noisy_image = np.copy(image)

    num_salt = np.ceil(amount * image.size * (1.0 - pepper_fraction)).astype(int)
    num_pepper = np.ceil(amount * image.size * pepper_fraction).astype(int)

    salt_coords = [np.random.randint(0, i - 1, num_salt) for i in image.shape]
    noisy_image[tuple(salt_coords)] = 255
    salt_coords = list(zip(salt_coords[0], salt_coords[1]))

    pepper_coords = [np.random.randint(0, i - 1, num_pepper) for i in image.shape]
    pepper_coords = list(zip(pepper_coords[0], pepper_coords[1]))

    return noisy_image, salt_coords, pepper_coords

def enlarge_points(image, coords, color):
    for x, y in coords:
        max_x, max_y = image.shape
        for dx in [-1, 0, 1]:
            for dy in [-1, 0, 1]:
                new_x, new_y = x + dx, y + dy
                if 0 <= new_x < max_x and 0 <= new_y < max_y:
                    image[new_x, new_y] = color
    return image


image_path = 'image.png'
image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

amount_of_noise = 0.002 
pepper_fraction = 0.5  
noisy_image, salt_coords, pepper_coords = add_salt_and_pepper_noise(image, amount_of_noise, pepper_fraction)

noisy_image = enlarge_points(noisy_image, pepper_coords, 0)  
noisy_image = enlarge_points(noisy_image, salt_coords, 255) 


plt.figure(figsize=(15, 5))
plt.subplot(131), plt.imshow(image, cmap='gray'), plt.title('Original Image'), plt.axis('off')
plt.subplot(132), plt.imshow(noisy_image, cmap='gray'), plt.title('Noisy Image'), plt.axis('off')
plt.show()
