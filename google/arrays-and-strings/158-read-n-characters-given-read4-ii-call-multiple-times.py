# The read4 API is already defined for you.
# def read4(buf4: List[str]) -> int:

from collections import deque
from typing import List

file_content = deque(list("1234567890abcdefghijklmnopqrstuvwxyz"))


def read4(buf: List[str]) -> int:

    if not file_content:
        return 0

    for i in range(4):
        buf[i] = file_content.popleft()

        if not file_content:
            break

    return len(buf)


class Solution:
    def __init__(self):
        self.unread_char = deque([])
        self.eof = False
        self.buffer = [''] * 4

    def read(self, buf: List[str], n: int) -> int:

        idx = 0
        while n > 0 and self.unread_char:
            buf[idx] = self.unread_char.popleft()
            idx += 1
            n -= 1
        
        while not self.eof and n > 0:
            count = read4(self.buffer)

            if count < 4:
                self.eof = True
                if count == 0:
                    break

            if n >= count:
                n -= count
                for i in range(count):
                    buf[idx] = self.buffer[i]
                    idx += 1
            else:
                for i in range(count):
                    if i < n:
                        buf[idx] = self.buffer[i]
                        idx += 1
                    else:
                        self.unread_char.append(self.buffer[i])
                n = 0

        return idx


buftest = ['']*50
print(Solution().read(buftest, 4))
print(buftest)


buftest = ['']*50
print(Solution().read(buftest, 10))
print(buftest)

buftest = ['']*50
print(Solution().read(buftest, 15))
print(buftest)

buftest = ['']*50
print(Solution().read(buftest, 3))
print(buftest)

buftest = ['']*50
print(Solution().read(buftest, 2))
print(buftest)

buftest = ['']*50
print(Solution().read(buftest, 1))
print(buftest)