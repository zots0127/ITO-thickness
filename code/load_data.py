import numpy as np
import matplotlib.pyplot as plt

# Load the data from a .npz file
data = np.load("original_data.npz")

# The .npz file contains two arrays: 'images' and 'targets'
# 'images' is a 2D array where each row is a 1D representation of an image.
# The original shape of each image is (128, 128, 3), which has been flattened to a 1D array of length 49152.
# 'targets' is a 1D array of target values corresponding to each image.
images = data['images']
targets = data['targets']

# To reshape and display an image, select a row from the 'images' array,
# reshape it to the original shape (128, 128, 3), and use plt.imshow.
image = images[0].reshape((128, 128, 3))
plt.imshow(image)
plt.show()
