from typing import List
from collections import defaultdict


class Solution:

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hash_map = defaultdict(list)

        for s in strs:
            helper = [0] * 26  # a-z
            for ch in s:
                helper[ord(ch) - ord("a")] += 1
            hash_map[tuple(helper)].append(s)

        return hash_map.values()
