import cv2
import numpy as np
import matplotlib.pyplot as plt

# Load your image
image = cv2.imread('Image_01.png', cv2.IMREAD_GRAYSCALE)

# Add Gaussian noise
noisy_image = image + np.random.normal(0, 25, image.shape).astype(np.uint8)

# Implement Otsu's thresholding
_, thresholded_image = cv2.threshold(noisy_image, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

# Display the original, noisy, and thresholded images
plt.figure(figsize=(15, 5))

plt.subplot(1, 3, 1)
plt.imshow(image, cmap='gray')
plt.title('Original Image')
plt.axis('off')

plt.subplot(1, 3, 2)
plt.imshow(noisy_image, cmap='gray')
plt.title('Noisy Image')
plt.axis('off')

plt.subplot(1, 3, 3)
plt.imshow(thresholded_image, cmap='gray')
plt.title('Thresholded Image')
plt.axis('off')

plt.show()
