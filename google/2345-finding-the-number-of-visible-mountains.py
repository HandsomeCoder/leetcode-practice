from collections import deque
from typing import List


class Solution:
    def visibleMountains(self, peaks: List[List[int]]) -> int:
        def is_sub(r1, r2):
            return (r1[0] <= r2[0] <= r1[1]) and (r1[0] <= r2[1] <= r1[1])

        ln = len(peaks)
        for idx in range(ln):
            x, y = peaks[idx]
            peaks[idx] = (x-y, x+y)

        peaks.sort()
        result = deque([])
        blocked_range = []

        for curr in peaks:
            if result:               
                prev = result[-1]
                if curr == prev:
                    blocked_range.append(result.pop())
                    continue

                if is_sub(prev, curr):
                    continue

                if is_sub(curr, prev):
                    result[-1] = curr
                    continue

            if blocked_range and is_sub(blocked_range[-1], curr):
                continue

            result.append(curr)

        return len(result)


print(Solution().visibleMountains([[2, 2], [2, 2], [3, 1]]))
