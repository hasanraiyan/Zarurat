from PIL import Image
import numpy as np
import random

def create_random_image(width, height):
    # Create a numpy array of random RGB values
    random_image = np.random.randint(0, 256, (height, width, 3), dtype=np.uint8)
    
    # Convert the numpy array to a PIL Image
    image = Image.fromarray(random_image, 'RGB')
    
    return image

# Define the dimensions of the image
width = 1280
height = 200

# Create the random image
random_image = create_random_image(width, height)

# Save the image
random_image.save("random_image.png")
