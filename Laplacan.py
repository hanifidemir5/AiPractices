import cv2
import numpy as np

image = cv2.imread('image.png')

gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

laplacian = cv2.Laplacian(gray_image, cv2.CV_64F)

abs_laplacian = np.uint8(np.absolute(laplacian))

blurred_laplacian = cv2.GaussianBlur(abs_laplacian, (5, 5), 0)

cv2.imshow('Original Image', image)
cv2.imshow('Laplacian Filtered Image', abs_laplacian)
cv2.imshow('Blurred Laplacian Image', blurred_laplacian)
cv2.waitKey(0)
cv2.destroyAllWindows()
