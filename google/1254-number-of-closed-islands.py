from collections import deque
from typing import List


class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:

        def check(x, y):
            nonlocal grid, R, C
            queue = deque([(x, y)])
            valid = True
            while queue:
                x, y = queue.popleft()

                if grid[x][y] == "#":
                    continue

                grid[x][y] = "#"
                for nx, ny in [(x, y+1), (x+1, y), (x, y-1), (x-1, y)]:
                    if 0 <= nx < R and 0 <= ny < C:
                        if grid[nx][ny] == 0:
                            queue.append((nx, ny))
                    else:
                        valid = False

            return valid

        R, C = len(grid), len(grid[0])

        if R <= 2 or C <= 2:
            return 0
            
        count = 0
        for x in range(R):
            for y in range(C):
                if grid[x][y] == 0:
                    if check(x, y):
                        count += 1

        return count


print(Solution().closedIsland([[1, 1, 1, 1, 1, 1, 1, 0], 
                               [1, 0, 0, 0, 0, 1, 1, 0], 
                               [1, 0, 1, 0, 1, 1, 1, 0], 
                               [1, 0, 0, 0, 0, 1, 0, 1], 
                               [1, 1, 1, 1, 1, 1, 1, 0]]))
