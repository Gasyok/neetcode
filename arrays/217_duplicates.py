from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        seen = {}
        for idx, num in enumerate(nums):
            if num in seen:
                return True
            seen[num] = idx

        return False


s = Solution()

print(s.containsDuplicate([1, 2, 3, 1]))
# assert s.containsDuplicate([1, 2, 3, 4]) is False
# assert s.containsDuplicate([1, 1, 1, 3, 3, 4, 3, 2, 4, 2]) is True
