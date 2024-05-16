class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        match = {")": "(", "]": "[", "}": "{"}
        for ch in s:
            if ch not in match:
                stack.append(ch)
            else:
                if len(stack) == 0 or stack[-1] != match[ch]:
                    return False
                stack.pop()

        return len(stack) == 0


stack = []
