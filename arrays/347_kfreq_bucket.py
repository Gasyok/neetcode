from typing import List


class Solution:

    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hash = {}
        res = []
        for _, val in enumerate(nums):
            hash[val] = hash.get(val, 0) + 1

        bucket = [[] for _ in range(len(nums) + 1)]

        for key, val in hash.items():
            bucket[val].append(key)

        tmp = k
        for i in range(len(bucket) - 1, -1, -1):
            if tmp == 0:
                break
            if bucket[i]:
                for j in range(len(bucket[i])):
                    if tmp == 0:
                        break
                    res.append(bucket[i][j])
                    tmp -= 1

        return res
