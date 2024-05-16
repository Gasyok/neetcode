from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash = dict()
        for idx, num in enumerate(nums):
            diff = target - num
            if num in hash:
                return [idx, hash[num]]
            hash[diff] = idx
        return []


# [2, 11, 7, 15] t = 9

# 0, 2
# hash[9 - 2] = 0
# {7: 0}

# 1, 11
# hash[9 - 11] = 1
# {7: 0, -2: 1}

# 2, 7
# hash[9 - 7] = 2
# {7: 0, -2: 1, 2: 2}

# if num in hash:
#     return [idx, hash[num]]
