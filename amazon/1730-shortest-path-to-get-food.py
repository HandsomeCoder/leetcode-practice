from collections import deque
from typing import List


class Solution:
    def getFood(self, grid: List[List[str]]) -> int:
        R, C = len(grid), len(grid[0])
        queue = deque()
        for i in range(R):
            for j in range(C):
                if grid[i][j] == "*":
                    queue.append((i, j, 0))
                    break

        direction = [(0, 1), (0, -1), (-1, 0), (1, 0)]
        while queue:
            x, y, step = queue.popleft()
            if grid[x][y] == "X":
                continue

            grid[x][y] = "X"
            for a, b in direction:
                nx = x + a
                ny = y + b
                if 0 <= nx < R and 0 <= ny < C and grid[nx][ny] != "X":
                    if grid[nx][ny] == "#":
                        return step+1
                    queue.append((nx, ny, step+1))
        return -1