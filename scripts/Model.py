from email.mime import image
from emnist import *
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from PIL import Image
from os import mkdir, path


class Model:
    def get_image_address(name):
        return "dataset-images/" + name + ".png"

    def __init__(self):
        super().__init__()

    def load_combined_dataset(self):
        train_images, train_labels = extract_training_samples("balanced")
        test_images, test_labels = extract_test_samples("balanced")
        print(train_images.shape)
        print(test_images.shape)

        self.images = numpy.concatenate((train_images, test_images), axis=0)
        print(self.images.shape)

        im = Image.fromarray(self.images[30])
        im.save(Model.get_image_address(str(30)))
        # im.show()

    def remove_combined_dataset(self):
        clear_cached_data()

    def get_image(self, index):

        return self.images[index]
