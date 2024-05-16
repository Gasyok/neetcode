from typing import List


class Solution:
    def trap(self, heights: List[int]) -> int:
        left = []
        right = []
        highest = 0

        left_ans = 0
        right_ans = 0

        for i, height in enumerate(heights):
            while left and height >= highest:
                _, h = left.pop()
                left_ans += highest - h

            highest = max(highest, height)
            left.append((i, height))

        highest = 0
        for i, height in reversed(left):
            while right and height >= highest:
                _, h = right.pop()
                right_ans += highest - h
            highest = max(highest, height)
            right.append((i, height))

        # print(left_ans, right_ans)
        return left_ans + right_ans


obj = Solution()
obj.trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1])  # 6
obj.trap([4, 2, 0, 3, 2, 5])  # 9
obj.trap([4, 2, 3])  # 1
obj.trap([2, 0, 2])  # 2
obj.trap([0, 7, 1, 4, 6])  # 7
