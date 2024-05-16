from collections import defaultdict
from typing import List


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        left = 0
        ans = 0
        hash = dict()

        for right, char in enumerate(s):
            while hash.get(char, 0) > 0 and left < right:
                hash[s[left]] -= 1
                left += 1

            hash[char] = 1
            ans = max(ans, right - left + 1)

        return ans


# sol = Solution()
print(Solution().lengthOfLongestSubstring("abcabcbb"))
