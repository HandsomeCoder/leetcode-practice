from collections import deque


class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        grid = [1] * n
        for row in range(1, m):
            for idx in range(n):
                grid[idx] += grid[idx-1] if idx > 0 else 0

        return grid[-1]