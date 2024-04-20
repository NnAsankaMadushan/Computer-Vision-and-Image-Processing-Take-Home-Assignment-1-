import cv2
import numpy as np

def region_growing(image, seed):
    visited = np.zeros_like(image)
    queue = [seed]
    region = []

    while queue:
        x, y = queue.pop(0)
        if visited[x, y] == 0:
            visited[x, y] = 1
            region.append((x, y))

            for dx in range(-1, 2):
                for dy in range(-1, 2):
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < image.shape[0] and 0 <= ny < image.shape[1]:
                        if abs(image[nx, ny] - image[x, y]) < 20:
                            queue.append((nx, ny))

    return region

# Load your image
image = cv2.imread('image.jpg', cv2.IMREAD_GRAYSCALE)

# Define seed point (you can choose any point inside the object)
seed_point = (100, 100)

# Get segmented region
segmented_region = region_growing(image, seed_point)

# Create a mask for visualization
mask = np.zeros_like(image)
for x, y in segmented_region:
    mask[x, y] = 255

# Define the desired window size (adjust as needed)
window_width = 600
window_height = 600

# Resize the original and segmented images to fit the window
resized_image = cv2.resize(image, (window_width, window_height))
resized_mask = cv2.resize(mask, (window_width, window_height))

# Display results in small windows
cv2.imshow('Resized Original Image', resized_image)
cv2.imshow('Resized Segmented Region', resized_mask)
cv2.waitKey(0)
cv2.destroyAllWindows()
