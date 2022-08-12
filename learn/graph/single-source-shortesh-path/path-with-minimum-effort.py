from collections import defaultdict
from email.policy import default
from heapq import heapify, heappop, heappush
from pprint import pprint
from typing import List


class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        R, C = len(heights), len(heights[0])

        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        visited = [[False] * C for _ in range(R)]

        queue = [(0, (0, 0))]
        heapify(queue)
        dest = (R-1, C-1)
        max_w = -1
        
        while queue:
            w, node = heappop(queue)
            i, j = node

            if visited[i][j]:
                continue

            visited[i][j] = True

            max_w = max(w, max_w)

            if node == dest:
                break

            for x, y in directions:
                nx, ny = i + x, j + y
                if R > nx >= 0 and C > ny >= 0:
                    neigh = (nx, ny)
                    if not visited[nx][ny]:
                        heappush(
                            queue, (abs(heights[i][j] - heights[nx][ny]), neigh))

        return max_w


print(Solution().minimumEffortPath([[1, 2, 2], [3, 8, 2], [5, 3, 5]]))
print(Solution().minimumEffortPath([[1, 2, 3], [3, 8, 4], [5, 3, 5]]))
print(Solution().minimumEffortPath([[1, 2, 1, 1, 1], [1, 2, 1, 2, 1], [
      1, 2, 1, 2, 1], [1, 2, 1, 2, 1], [1, 1, 1, 2, 1]]))
