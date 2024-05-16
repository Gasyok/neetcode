import random
from typing import List
import numpy


class Store:
    def __init__(self, val=None):
        self.val = set()
        if val:
            self.val.add(val)

    def add(self, val):
        self.val.add(val)

    def remove(self, val):
        self.val.remove(val)

    def get_random(self):
        return random.choice(list(self.val))


s = Store()
s.add(val=2)
s.add(val=3)
s.add(val=5)
print(s.get_random())
