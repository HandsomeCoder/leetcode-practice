from collections import deque
from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        stack = deque([])

        blocked = water = 0 
        for idx, h in enumerate(height):

            if not stack or stack[-1][0] > h:
                stack.append((h, idx + 1))
                continue

            if len(stack) < 2:
                stack[0] = (h, idx + 1)
                continue

            curr_block = 0
            while len(stack) > 1 and stack[-1][0] < h:
                curr_block += stack.pop()[0]

            if stack:
                lh, lidx = stack[-1]
                blocked += curr_block
                water += ((idx - lidx) * min(h, lh)) - blocked

            if stack[-1][0] <= h:
                stack.pop()

            stack.append((h, idx + 1))
        return water


print(Solution().trap(
    [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))
