# not efficient but it would work in C way
# But that's okay, i pretend that i control the cappacity of the stack,
# but ofc it's not efficient in python
class MinStack:

    def __init__(self):
        self.__stack = []
        self.__min_stack = []
        self.__top = -1
        self.__cappacity = 1

    def push(self, val: int) -> None:
        self.__top += 1
        if self.__top >= self.__cappacity // 2:
            self.__cappacity *= 2
            self.__stack.extend([None] * (self.__top + 1))

        if not self.__min_stack or val <= self.__min_stack[-1]:
            self.__min_stack.append(val)
        self.__stack[self.__top] = val

    def pop(self) -> None:
        if self.__top == -1:
            return

        if self.__stack[self.__top] == self.__min_stack[-1]:
            self.__min_stack.pop()

        self.__stack[self.__top] = None

        self.__top -= 1
        if self.__top <= self.__cappacity // 4:
            self.__stack = self.__stack[:self.__cappacity // 2]
            self.__cappacity = self.__cappacity // 2

    def top(self) -> int:
        return self.__stack[self.__top]

    def getMin(self) -> int:
        return self.__min_stack[-1]


obj = MinStack()
obj.push(2)
obj.push(3)
obj.push(0)
obj.push(0)
obj.pop()
obj.pop()
obj.pop()
print(obj.top())
# print(obj.__stack)
# print(obj.__min_stack)
print(obj.getMin())
