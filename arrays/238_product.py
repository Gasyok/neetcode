from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        prefix_product = [1] * n
        suffix_product = [1] * n

        total_l = 1
        total_r = 1
        for i in range(n):
            prefix_product[i] = total_l
            total_l *= nums[i]

            suffix_product[n - 1 - i] = total_r
            total_r *= nums[n - 1 - i]

        res = []
        for idx, _ in enumerate(nums):
            res.append(prefix_product[idx] * suffix_product[idx])
        return res


# TODO: heello
nums = [1, 2, 3, 4]
s = Solution()

print(s.productExceptSelf(nums))
