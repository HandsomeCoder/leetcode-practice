from heapq import heapify, heappop, heappush
from typing import List


class Solution:
    def maximumMinimumPath(self, grid: List[List[int]]) -> int:

        R, C = len(grid), len(grid[0])
        stack = [(-grid[0][0], 0, 0)]
        heapify(stack)
        while stack:
            min_val, x, y = heappop(stack)
            if x + 1 == R and y + 1 == C:
                return min_val * -1

            if grid[x][y] == "#":
                continue

            grid[x][y] = "#"
            for nx, ny in [(x+1, y), (x, y+1), (x-1, y), (x, y-1)]:
                if 0 <= nx < R and 0 <= ny < C and grid[nx][ny] != "#":
                    heappush(stack, (max(min_val, -grid[nx][ny]), nx, ny))


print(Solution().maximumMinimumPath([[2, 0, 5, 2, 0], [2, 4, 4, 4, 3], [
      1, 5, 0, 0, 0], [5, 4, 4, 3, 1], [1, 3, 1, 5, 3]]))
