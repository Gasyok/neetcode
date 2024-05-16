class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        ans = 0

        hash = dict()
        left = 0
        max_frequent_count = 0

        for right, char in enumerate(s):
            hash[char] = hash.get(char, 0) + 1
            max_frequent_count = max(max_frequent_count, hash[char])

            while (right - left + 1) - max_frequent_count > k:
                hash[s[left]] -= 1
                left += 1

            ans = max(ans, right - left + 1)

        return ans


print(Solution().characterReplacement("ABAB", 2))
print(Solution().characterReplacement("AABABBA", 1))
print(Solution().characterReplacement("AABA", 0))
print(Solution().characterReplacement("ABABBAAAA", 2))
