from sklearn.utils import murmurhash3_32
from bitarray import bitarray
import math
import random

def get_size(n, fp_rate):
    """Calculate the size of the bit array for the Bloom Filter."""
    size = -(n * math.log(fp_rate)) / (math.log(2) ** 2)
    return int(size)

def get_hash_count(m, n):
    """Calculate the optimal number of hash functions."""
    k = (m / n) * math.log(2)
    return int(k)

def hash_func(m, seed):
    """Create a hash function with a given seed."""
    def hash(key):
        return murmurhash3_32(key, seed) % m
    return hash

class BloomFilter:
    def __init__(self, n, fp_rate):
        self.size = get_size(n, fp_rate)
        self.hash_count = get_hash_count(self.size, n)
        self.bit_array = bitarray(self.size)
        self.bit_array.setall(0)
        self.hash_funcs = [hash_func(self.size, random.randint(0, 1000)) for _ in range(self.hash_count)]

    def insert(self, key):
        """Insert a key into the Bloom Filter."""
        for f in self.hash_funcs:
            index = f(key)
            self.bit_array[index] = 1

    def test(self, key):
        """Check if a key is in the Bloom Filter."""
        for f in self.hash_funcs:
            index = f(key)
            if not self.bit_array[index]:
                return False
        return True
