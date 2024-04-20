import cv2
import numpy as np



# Load your image
image = cv2.imread('Image_01.png', cv2.IMREAD_GRAYSCALE)

# Add Gaussian noise
noisy_image = image + np.random.normal(0, 20, image.shape).astype(np.uint8)

# Implement Otsu's thresholding
_, thresholded_image = cv2.threshold(noisy_image, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

# Define the desired window size (adjust as needed)
window_width = 700
window_height = 700

# Resize the noisy and thresholded images to fit the window
resized_noisy_image = cv2.resize(noisy_image, (window_width, window_height))
resized_thresholded_image = cv2.resize(thresholded_image, (window_width, window_height))

# Display results in small windows
cv2.imshow('Noisy Image', resized_noisy_image)
cv2.imshow('Thresholded Image', resized_thresholded_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
