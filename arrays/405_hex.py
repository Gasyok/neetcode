class Solution:
    def toHex(self, num: int) -> str:
        hexmap = '0123456789abcdef'

        if num < 0:

        if num == 0:
            return "0"
        s = []
        while num:
            x = num % 16
            s.append(x)
            num = num // 16
        res = []
        for i in range(len(s), -1, -1):
            res.append(s[i])

        return res
