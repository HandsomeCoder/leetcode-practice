from typing import List


class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        R, C = len(obstacleGrid), len(obstacleGrid[0])

        if obstacleGrid[0][0] == 1:
            return 0

        obstacleGrid[0][0] = 1

        grid = obstacleGrid
        for c in range(1, C):
            grid[0][c] = 0 if grid[r][c] == 1 else grid[r][c-1]

        for r in range(1, R):
            grid[r][0] = 0 if grid[r][c] == 1 else grid[r-1][c]

        for r in range(1, R):
            for c in range(1, C):
                grid[r][c] = 0 if grid[r][c] == 1 else grid[r-1][c] + grid[r][c-1]

        return grid[-1][-1]
