from typing import List


class Solution:

    def maxHeapify(self, arr, heapsize, i):
        left = 2 * i + 1
        right = 2 * i + 2
        largest = i
        if left < heapsize and arr[left][1] > arr[largest][1]:
            largest = left
        if right < heapsize and arr[right][1] > arr[largest][1]:
            largest = right
        if largest != i:
            arr[i], arr[largest] = arr[largest], arr[i]
            self.maxHeapify(arr, heapsize, largest)

    def buildMaxheap(self, arr, heapsize):
        # heapsize = len(arr)
        for i in range(heapsize // 2, -1, -1):
            self.maxHeapify(arr, heapsize, i)

    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hash = {}
        res = []
        for _, val in enumerate(nums):
            hash[val] = hash.get(val, 0) + 1

        arr = list(hash.items())
        heapsize = len(arr)
        for _ in range(k):
            self.buildMaxheap(arr, heapsize)
            res.append(arr[0][0])
            arr[0], arr[heapsize - 1] = arr[heapsize - 1], arr[0]
            heapsize -= 1
            arr.pop()

        return res
