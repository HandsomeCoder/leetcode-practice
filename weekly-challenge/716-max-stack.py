from collections import defaultdict, deque
from heapq import heapify, heappop, heappush

class MaxStack:

    def __init__(self):
        self.stack = deque([])
        self.max_heap = []
        heapify(self.max_heap)
        self.counter = defaultdict(lambda: 0)

    def __calibrate_stack(self):
        while self.counter[self.stack[-1][0]] != self.stack[-1][1]:
            self.stack.pop()

    def __calibrate_heap(self):
        while self.counter[(self.max_heap[0] * -1)] == 0:
            heappop(self.max_heap)

    def push(self, x: int) -> None:
        self.counter[x] += 1
        self.stack.append((x, self.counter[x]))
        heappush(self.max_heap, -x)

    def pop(self) -> int:
        self.__calibrate_stack()

        val, _ = self.stack.pop()
        self.counter[val] -= 1
        return val        

    def top(self) -> int:
        self.__calibrate_stack()
        return self.stack[-1][0]

    def peekMax(self) -> int:
        self.__calibrate_heap()
        return self.max_heap[0] * -1

    def popMax(self) -> int:
        self.__calibrate_heap()
        
        max_val = heappop(self.max_heap)
        max_val *= -1
        self.counter[max_val] -= 1
        return  max_val