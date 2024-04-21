import numpy as np
import cv2
import matplotlib.pyplot as plt

def region_growing(img, seed):
    height, width = img.shape
    segment = np.zeros((height, width), np.uint8)
    visited = np.zeros((height, width))

    # List to hold the pixel positions that need to be checked
    active_list = []
    active_list.append(seed)

    while len(active_list) > 0:
        x, y = active_list.pop()
        if visited[y,x] == 1:
            continue
        visited[y,x] = 1

        # Check if current pixel value is within the predefined range of seed pixel value
        if abs(int(img[x,y]) - int(img[seed])) <= threshold:
            segment[x,y] = img[x,y]
            # Add neighbouring pixels to the list
            if x > 0: active_list.append((x-1, y))
            if x < height-1: active_list.append((x+1, y))
            if y > 0: active_list.append((x, y-1))
            if y < width-1: active_list.append((x, y+1))

    return segment

# Load an example image (grayscale)
img = cv2.imread('Image_02.jpg', cv2.IMREAD_GRAYSCALE)

# Define a seed point and threshold value for segmentation 
seed_point = (50,50)
threshold = 20

segmented_image = region_growing(img, seed_point)

# Display the original and segmented images
plt.figure(figsize=(10,10))

plt.subplot(1,2,1)
plt.imshow(img, cmap='gray')
plt.title('Original Image')
plt.axis('off')

plt.subplot(1,2,2)
plt.imshow(segmented_image, cmap='gray')
plt.title('Segmented Image')
plt.axis('off')

plt.show()
