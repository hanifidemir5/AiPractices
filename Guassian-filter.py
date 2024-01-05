import cv2
import numpy as np

image = cv2.imread('image.png')

kernel_size = (5, 5)  
blurred_image = cv2.GaussianBlur(image, kernel_size, 0)

cv2.imshow('Original Image', image)
cv2.imshow('Blurred Image', blurred_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
