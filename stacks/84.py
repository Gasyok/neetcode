from typing import List


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        area = 0
        for i, height in enumerate(heights):
            j = i
            while stack and height < stack[-1][1]:
                j, h = stack.pop()
                area = max(area, (i - j) * h)

            stack.append((j, height))

        for i, height in stack:
            area = max(area, (len(heights) - i) * height)

        return area


obj = Solution()

print(obj.largestRectangleArea([5, 4, 1, 2]))  # 8
print(obj.largestRectangleArea([2, 1, 5, 6, 2, 3]))  # 10
print(obj.largestRectangleArea([2, 4]))  # 4
print(obj.largestRectangleArea([2, 1, 2]))  # 3
