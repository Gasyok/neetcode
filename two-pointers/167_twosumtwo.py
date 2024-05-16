from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers) - 1

        while left < right:
            summa = numbers[left] + numbers[right]
            if summa == target:
                break
            if summa < target:
                left += 1
            else:
                right -= 1

        return [left + 1, right + 1]
