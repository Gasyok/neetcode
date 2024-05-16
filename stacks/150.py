from typing import List


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            try:
                stack.append(int(token))
            except ValueError:
                last = stack.pop()
                second = stack.pop()
                if token == "+":
                    element = last + second
                elif token == "*":
                    element = last * second
                elif token == "/":
                    element = int(second / last)
                else:
                    element = second - last
                stack.append(element)

        return int(stack[0])


# x = ["4", "13", "5", "/", "+"]
x = ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]
# 10, 6, 9, 3
# 10, 6

s = Solution()
print(s.evalRPN(x))
