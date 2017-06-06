from typing import List


class Solution:
    def num(self, n):
        if n == 0:
            return 0

        return 2 + self.num(n - 1)

    def generateParenthesis(self, n: int) -> List[str]:
        def helper(opened, closed, string):
            if len(string) == n * 2:
                ans.append(string)
                return

            if opened < n:
                helper(opened + 1, closed, string + "(")

            if closed < opened:
                helper(opened, closed + 1, string + ")")

        ans = []
        helper(0, 0, "")
        return ans


s = Solution()
print(s.generateParenthesis(6))


# () n = 1
# )(

# (()) n = 2
# ()()
# )()(
# ))((

# ({n = 1})
# ){n = 1}(

# ({n = 2}) n = 3
# ){n = 2}(


# 2 + [n - 1] -all
# 1 + [n - 1] -valid


# 1 + [2 + 2] = 5

# via reccursion can measure the number of possible variant
