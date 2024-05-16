class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        n = len(s1)
        m = len(s2)

        if n > m:
            return False

        hash_s1 = [0] * 26
        hash_s2 = [0] * 26
        count = 0

        for i, ch in enumerate(s1):
            hash_s1[ord(ch) - ord('a')] += 1
            hash_s2[ord(s2[i]) - ord('a')] += 1

        for i in range(26):
            count += 1 if hash_s1[i] == hash_s2[i] else 0

        for right in range(n, m):
            if count == 26:
                return True
            idx = ord(s2[right]) - ord('a')
            hash_s2[idx] += 1
            if hash_s2[idx] == hash_s1[idx]:
                count += 1
            elif hash_s2[idx] == hash_s1[idx] + 1:
                count -= 1
            jdx = ord(s2[right - n]) - ord('a')
            hash_s2[jdx] -= 1
            if hash_s2[jdx] == hash_s1[jdx]:
                count += 1
            elif hash_s2[jdx] == hash_s1[jdx] - 1:
                count -= 1

        return count == 26


print(Solution().checkInclusion("ab", "eidboaoo"))
