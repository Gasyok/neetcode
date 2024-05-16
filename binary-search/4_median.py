from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:

        if len(nums1) < len(nums2):
            nums1, nums2 = nums2, nums1

        m = len(nums1)
        n = len(nums2)
        sz = m + n

        is_odd = (sz % 2 != 0)
        half = (m + n) // 2

        left = 0
        right = n - 1

        while True:
            mid = (left + right) // 2
            diff = half - mid - 2

            n_left = nums2[mid] if mid >= 0 else float("-infinity")
            n_right = nums2[mid + 1] if (mid + 1) < n else float("infinity")
            m_left = nums1[diff] if diff >= 0 else float("-infinity")
            m_right = nums1[diff + 1] if (diff + 1) < m else float("infinity")

            if n_left <= m_right and n_right >= m_left:
                if is_odd:
                    return min(n_right, m_right)
                return (max(n_left, m_left) + min(n_right, m_right)) / 2
            elif n_left > m_right:
                right = mid - 1
            else:
                left = mid + 1


print(Solution().findMedianSortedArrays([1, 3], [2]))
