from collections import deque
from typing import List


class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        R, C = len(grid) - 1, len(grid[0]) - 1

        def get_valid_neighbours(x, y, cost):
            result = []

            xl = x > 0
            yl = y > 0
            xh = x < R
            yh = y < C

            if xl:
                if grid[x-1][y] == 0:
                    result.append((x-1, y, cost))

                if yl and grid[x-1][y-1] == 0:
                    result.append((x-1, y-1, cost))

                if yh and grid[x-1][y+1] == 0:
                    result.append((x-1, y+1, cost))

            if xh:
                if grid[x+1][y] == 0:
                    result.append((x+1, y, cost))

                if yl and grid[x+1][y-1] == 0:
                    result.append((x+1, y-1, cost))

                if yh and grid[x+1][y+1] == 0:
                    result.append((x+1, y+1, cost))
                
            if yl and grid[x][y-1] == 0:
                result.append((x, y-1, cost))

            if yh and grid[x][y+1] == 0:
                result.append((x, y+1, cost))

            return result

        queue = deque([(0, 0, 1)])
        while queue:

            x, y, cost = queue.popleft()

            if grid[x][y] == 1:
                continue

            if x == R and y == C:
                return cost

            grid[x][y] = 1

            queue.extend(get_valid_neighbours(x, y, cost + 1))

        return -1
