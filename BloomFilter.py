from sklearn.utils import murmurhash3_32
from bitarray import bitarray
import math
import numpy as np
import random


def getSize(n, fp_rate):
    size = -(n * math.log(fp_rate)) / (math.log(2) ** 2)
    return int(size)


class BloomFilter():
    def __init__(self, n, fp_rate):
        # Size of the array (round up to the nearest power of 2
        self.size = getSize(n, fp_rate)

        # Initialize the array
        self.bit_array = bitarray(self.size)

        # Calculate the number of hash functions
        self.hash_number = math.ceil(np.log(2) * math.log(fp_rate, 0.618))

        # Initialize all bits to 0
        self.bit_array.setall(0)

    def insert(self, key):
        for i in range(self.hash_number):
            pos = murmurhash3_32(key, i) % self.size
            self.bit_array[pos] = 1

    def test(self, key):
        for i in range(self.hash_number):
            pos = murmurhash3_32(key, i) % self.size
            if self.bit_array[pos] == 0:
                return False
        return True
