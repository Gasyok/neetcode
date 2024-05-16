from typing import List


class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # time = [(target - position[i]) / speed[i]
        #         for i in range(len(position))]
        state = zip(position, speed)
        state = sorted(state, reverse=True)
        stack = []
        for pos, vel in state:
            dist = target - pos
            time = dist / vel

            if stack and time <= stack[-1]:
                continue

            stack.append(time)

        return len(stack)


s = Solution()
print(s.carFleet(12, [10, 8, 0, 5, 3], [2, 4, 1, 1, 3]))  # 3
print(s.carFleet(10, [0, 4, 2], [2, 1, 3]))  # 1
print(s.carFleet(10, [3], [3]))  # 1

# 4 2 0
# 1 3 2

# 6 (8/3) 5


# 2 will slow down by 4 then
# 5 will slow down by 4 also


# [6] [6, ]
