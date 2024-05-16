from typing import Optional


class Node:
    # def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
    def __init__(self, x: int, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        ...


x = Node(5)
y = Node(6)

hash_map = {x: y}


print(hash_map[x])
print(x in hash_map)
