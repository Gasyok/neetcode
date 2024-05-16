from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        left = 0
        ans = 0
        profit = 0

        for right, _ in enumerate(prices):
            profit = prices[right] - prices[left]

            while profit < 0 and left < right:
                profit = prices[right] - prices[left]
                left += 1

            ans = max(ans, prices[right] - prices[left])

        return ans


sol = Solution()
print(sol.maxProfit([7, 1, 5, 3, 6, 4]))
