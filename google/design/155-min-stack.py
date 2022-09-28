from collections import deque

class MinStack:

    def __init__(self):
        self.stack = deque([])
        self.min_stack = deque([])

    def push(self, val: int) -> None:
        self.stack.append(val)

        if not self.min_stack or (self.min_stack[-1][0] > val):
            self.min_stack.append([val, 1])
        elif self.min_stack[-1][0] == val:
            self.min_stack[-1][1] += 1

    def pop(self) -> None:
        item = self.stack.pop()
        if self.min_stack[-1][0] == item:
            self.min_stack[-1][1] -= 1
            if self.min_stack[-1][1] == 0:
                self.min_stack.pop()

    def top(self) -> int:
        return self.stack[-1]
        
    def getMin(self) -> int:
        return self.min_stack[-1][0]