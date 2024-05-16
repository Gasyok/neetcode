from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix:
            return False
        m = len(matrix)
        n = len(matrix[0])
        row_left, col_left = 0, 0
        row_right, col_right = m - 1, n - 1
        row_mid, col_mid = m // 2, n // 2

        while row_left <= row_right:
            row_mid = row_left + (row_right - row_left) // 2

            if matrix[row_mid][0] == target:
                return True

            if matrix[row_mid][0] < target:
                row_left = row_mid + 1
            else:
                row_right = row_mid - 1

        row_mid = row_right

        while col_left <= col_right:
            col_mid = col_left + (col_right - col_left) // 2

            if matrix[row_mid][col_mid] == target:
                return True

            if matrix[row_mid][col_mid] < target:
                col_left = col_mid + 1
            else:
                col_right = col_right - 1

        return False


obj = Solution()
print(obj.searchMatrix([[1]], 1))
print(obj.searchMatrix(
    [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 3))  # True
print(obj.searchMatrix(
    [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 13))  # False
