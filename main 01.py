import cv2
import numpy as np

# Load your image
image = cv2.imread('image.jpg', cv2.IMREAD_GRAYSCALE)

# Add Gaussian noise
noisy_image = image + np.random.normal(0, 25, image.shape).astype(np.uint8)

# Implement Otsu's thresholding
_, thresholded_image = cv2.threshold(noisy_image, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

# Display results
cv2.imshow('Noisy Image', noisy_image)
cv2.imshow('Thresholded Image', thresholded_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
