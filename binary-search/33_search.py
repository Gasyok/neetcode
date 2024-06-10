from typing import List


# prikol 1
# TODO: MAKE THIS WORK!
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        sz = len(nums)
        left = 0
        right = sz - 1
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] == target:
                return mid
            is_transition = nums[right] < nums[left]
            is_left = target >= nums[left]
            is_start_left = nums[mid] < nums[left]

            if is_transition and is_left and is_start_left:
                right = mid - 1
            elif is_transition and not is_left and not is_start_left:
                left = mid + 1
            else:
                if nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
        return -1


if __name__ == "__main__":
    print(Solution().search([4, 5, 6, 7, 0, 1, 2], 0))  # 4
    print(Solution().search([4, 5, 6, 7, 0, 1, 2], 3))  # -1
    print(Solution().search([1], 0))  # -1
    print(Solution().search([1], 1))  # 0
    print(Solution().search([1, 3], 3))  # 1
    print(Solution().search([3, 1], 3))  # 0
    print(Solution().search([6, 7, 1, 2, 3, 4, 5], 1))  # 2
    print(Solution().search([3, 5, 1], 3))  # 0
