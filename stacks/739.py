from typing import List


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0]*len(temperatures)

        stack = []
        for i, temp in enumerate(temperatures):
            while stack and stack[-1][1] < temp:
                pop = stack.pop()
                res[pop[0]] = (i - pop[0])
            stack.append((i, temp))

        return res
    # def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
    #     res = []
    #     temp_help = [[] for _ in range(71)]

    #     for i, temp in enumerate(temperatures):
    #         temp_help[temp-30].append(i)

    #     for i, temp in enumerate(temperatures):
    #         found = 0
    #         for j in range(temp - 30 + 1, 71):
    #             if temp_help[j]:
    #                 for k in temp_help[j]:
    #                     if k > i:
    #                         if found:
    #                             found = min(found, k - i)
    #                         else:
    #                             found = k - i

    #         res.append(found)

    #     return res


sol = Solution()
print(sol.dailyTemperatures([73, 74, 75, 71, 69, 72, 76, 73]))
