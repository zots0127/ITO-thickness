import numpy as np
from random import randint
import matplotlib.pyplot as plt
from skimage.transform import resize

# Load the data from a .npz file
data = np.load("original_data.npz")
images = data['images']
targets = data['targets']

def random_crop(image):
    # Randomly crop a 100x100 region from the image
    start_x = randint(0, image.shape[0]-100)
    start_y = randint(0, image.shape[1]-100)
    return image[start_x:start_x+100, start_y:start_y+100, :]

# Augment the images
augmented_images = []
augmented_targets = []

for image, target in zip(images, targets):
    # Reshape the image to its original shape
    image = image.reshape((128, 128, 3))
    
    # Randomly crop the image and resize it back to 128x128
    cropped_image = resize(random_crop(image), (128, 128))
    
    # Flatten the cropped image and append it to the augmented_images list
    augmented_images.append(cropped_image.flatten())
    
    # Append the corresponding target to the augmented_targets list
    augmented_targets.append(target)

# Convert to numpy arrays
augmented_images = np.array(augmented_images)
augmented_targets = np.array(augmented_targets)

# Display an augmented image
image = augmented_images[0].reshape((128, 128, 3))
plt.imshow(image)
plt.show()
