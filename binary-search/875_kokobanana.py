from typing import List


class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        greatest = 0
        for pile in piles:
            greatest = max(greatest, pile)

        left = 1
        right = greatest

        while left <= right:
            mid = left + (right - left) // 2  # k
            hours = 0
            for i in range(len(piles)):

                num = piles[i] // mid
                rest = piles[i] % mid

                if not rest:
                    hours += num
                else:
                    hours += num + 1

            if hours > h:
                left = mid + 1
            else:
                right = mid - 1

        return left

    # 1 2 3 4 5 6 7 8 9 10 11
    # 5 -> true


print(Solution().minEatingSpeed([1], 1))

print(Solution().minEatingSpeed([3, 6, 7, 11], 8))
print(Solution().minEatingSpeed([30, 11, 23, 4, 20], 5))
print(Solution().minEatingSpeed([30, 11, 23, 4, 20], 6))
print(Solution().minEatingSpeed([312884470], 968709470))  # 1
print(Solution().minEatingSpeed([312884470], 312884469))  # 2
print(Solution().minEatingSpeed([2, 6, 7, 11], 5))  # 7
