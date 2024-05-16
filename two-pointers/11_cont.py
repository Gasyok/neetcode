from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:

        left = 0
        right = len(height) - 1

        ans = 0
        area = 0

        while left < len(height) - 1 and right > 0:
            area = max(area, abs(right - left) *
                       min(height[left], height[right]))
            ans = max(ans, area)

            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return ans


# print(Solution().maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]))  # 49
# print(Solution().maxArea([1, 1]))  # 1
# print(Solution().maxArea([4, 3, 2, 1, 4]))  # 16
print(Solution().maxArea([1, 3, 2, 5, 25, 24, 5]))  # 24
print(Solution().maxArea([1, 2, 3, 4, 5, 25, 24, 3, 4]))  # 24
