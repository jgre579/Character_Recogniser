from emnist import *
import numpy as np


class Model:
    def __init__(self):
        super().__init__()

    def loadCombinedDataset(self):
        train_images, train_labels = extract_training_samples("balanced")
        test_images, test_labels = extract_test_samples("balanced")
        print(train_images.shape)
        print(test_images.shape)

        self.images = numpy.concatenate((train_images, test_images), axis=0)
        print(self.images.shape)

    def removeCombinedDataset(self):
        clear_cached_data()

    def get_image(self, index):

        return self.images[index]
