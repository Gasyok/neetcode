from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        ans = []

        for i, num in enumerate(nums):
            if num > 0:
                break
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            left = i + 1
            right = len(nums) - 1

            while left < right:
                # if left > i + 1 and nums[left] == nums[left - 1]:
                #     left += 1
                #     continue
                target = nums[left] + nums[right]

                if target == -num:
                    ans.append([num, nums[left], nums[right]])
                    left += 1
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                elif target > -num:
                    right -= 1
                else:
                    left += 1
        return ans


obj = Solution()
# print(obj.threeSum([-1, 0, 1, 2, -1, -4, -2]))
# print(obj.threeSum([0, 0, 0, 0]))
print(obj.threeSum([-2, 0, 0, 2, 2]))
# print(obj.threeSum([-2, 0, 1, 1, 2]))
