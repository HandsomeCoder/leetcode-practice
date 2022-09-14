from collections import deque
from typing import List


class RLEIterator:

    def __init__(self, encoding: List[int]):
        self.encoding = encoding
        self.idx = 0       

    def next(self, n: int) -> int:
        eln = len(self.encoding)
        while self.idx < eln:
            top = self.encoding[self.idx]
            if top == 0:
                self.idx += 2
                continue

            if top >= n:
                self.encoding[self.idx] -= n
                return self.encoding[self.idx + 1]
            else:
                n -= self.encoding[self.idx]
                self.encoding[self.idx] = 0
        return -1

# Your RLEIterator object will be instantiated and called as such:
# obj = RLEIterator(encoding)
# param_1 = obj.next(n)