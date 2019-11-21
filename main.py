import matplotlib.pyplot as plt
import random
from scipy import ndarray
import skimage as sk
from skimage import transform
from skimage import util
import numpy as np
import argparse
import os

def random_rotation(image_array):
    # pick a random degree of rotation between 25% on the left and 25% on the right
    random_degree = random.uniform(-2, 2)
    return sk.transform.rotate(image_array, random_degree)

def random_noise(image_array):
    # add random noise to the image
    return sk.util.random_noise(image_array)

def horizontal_flip(image_array):
    # horizontal flip doesn't need skimage, it's easy as flipping the image array of pixels !
    return image_array[:, ::-1]

parser = argparse.ArgumentParser(description = "enter the path")
parser.add_argument("--direct",help='enter the path')
args = parser.parse_args()
data_directory = args.direct

data = os.listdir(data_directory)

for i in data:
    os.chdir(data_directory)
    images = os.listdir(i)
    os.chdir(data_directory+i)
    for step, img in enumerate(images):
        os.chdir("/media/data_dump/hemant/data/image_net/test"+i)
        image = sk.io.imread(img)

        # Randomly choosing how many time to do 
        # three operations on a single image
        for j in range(np.random.randint(1,10)):
            image = horizontal_flip(random_rotation(random_noise(image)))
        # save_directory = " "
        sk.io.imsave(str(step)+img,image)
