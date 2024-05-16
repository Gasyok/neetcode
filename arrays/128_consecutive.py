from typing import List


class Solution:
    def conc(self, hashset, num):
        if num not in hashset:
            return 0
        hashset.remove(num)
        return 1 + self.conc(hashset, num - 1) + self.conc(hashset, num + 1)

    def longestConsecutive(self, nums: List[int]) -> int:
        hashset = set()
        if not len(nums):
            return 0
        for num in nums:
            hashset.add(num)
        maxl = 1

        for num in nums:
            length = self.conc(hashset, num)
            maxl = max(length, maxl)
        return maxl


sol = Solution()
print(sol.longestConsecutive([100, 4, 200, 1, 3, 2]))
