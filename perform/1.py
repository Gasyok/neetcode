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


def test(object=None):
    return {
        "hello": {
            "test": 14,
            "lol": 14,
        },
        "l": {
            "3": 1,
        },
    }


print(test())


s = Store()
s.add(val=4)
s.add(val=5)
s.add(val=7)
print(s.get_random())
