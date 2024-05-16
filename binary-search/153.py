from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        sz = len(nums)
        left = 0
        right = sz - 1

        while left < right:
            mid = left + (right - left) // 2
            # print(nums[left], nums[mid], nums[right])

            if nums[right] >= nums[left]:
                return nums[left]

            if nums[mid] >= nums[left]:
                if (right - left + 1) % 2 == 0:
                    left = mid + 1
                else:
                    left = mid
            else:
                right = mid

        return nums[left]


if __name__ == '__main__':
    print(Solution().findMin([3, 4, 5, 1, 2]))  # 1
    print(Solution().findMin([4, 5, 6, 7, 0, 1, 2]))  # 0
    print(Solution().findMin([11, 13, 15, 17]))  # 11
    print(Solution().findMin([2, 1]))  # 1
    print(Solution().findMin([3, 1, 2]))  # 1

# 3 1 2
# 1 2
# 1

# 2 3 0 1
# 0 1
# 1

# 5 1 2 3
# 5 1
# 1

# 1 2 3
# 1 2
# 1
