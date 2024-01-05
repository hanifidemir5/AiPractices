import cv2
import numpy as np

def assign_rgb_colors(image_path):
    grayscale_image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

    if grayscale_image is None:
        print(f"Error loading image from {image_path}")
        return None

    normalized_image = grayscale_image / 255.0

    colored_image = cv2.applyColorMap((normalized_image * 255).astype(np.uint8), cv2.COLORMAP_JET)

    cv2.imshow('Grayscale Image', grayscale_image)
    cv2.imshow('Assigned RGB Colors', colored_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

image_path = 'image.png'  
assign_rgb_colors(image_path)
