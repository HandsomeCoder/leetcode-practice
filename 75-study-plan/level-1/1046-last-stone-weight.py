
from heapq import heapify, heappop, heappush
from typing import List


class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        ln = len(stones)

        stones = [(-1*s, s) for s in stones]
        heapify(stones)

        while ln > 1:
            _, y = heappop(stones)
            _, x = heappop(stones)

            if x == y:
                ln -= 2
            else:
                heappush(stones, (x - y, y - x))
                ln -= 1

        return heappop(stones)[1] if len(stones) == 1 else 0


print(Solution().lastStoneWeight([2, 7, 4, 1, 8, 1]))
