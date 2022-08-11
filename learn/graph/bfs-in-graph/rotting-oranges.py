from collections import defaultdict, deque
from typing import List


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        R, C = len(grid), len(grid[0])

        spread = []
        queue = deque([])
        origins = 0
        oranges = set()
        for r in range(R):
            spread.append([-1]*C)
            for c in range(C):
                if grid[r][c] == 1:
                    oranges.add((r,c))
                if grid[r][c] == 2:
                    queue.append((r, c, origins, 0))
                    origins += 1

        R -= 1
        C -= 1

        def get_valid_neighbours(r, c, oid, spread, time):
            result = []
            if r > 0 and grid[r-1][c] != 0 and spread[r-1][c] == -1:
                result.append((r-1, c, oid, time))

            if r < R and grid[r+1][c] != 0 and spread[r+1][c] == -1:
                result.append((r+1, c, oid, time))

            if c > 0 and grid[r][c-1] != 0 and spread[r][c-1] == -1:
                result.append((r, c-1, oid, time))

            if c < C and grid[r][c+1] != 0 and spread[r][c+1] == -1:
                result.append((r, c+1, oid, time))

            return result

        max_time = 0
        while queue:
            r, c, oid, time = queue.popleft()

            itr = (r, c)
 
            if itr in oranges:
                oranges.remove(itr)
            
            if spread[r][c] == -1:
                spread[r][c] = time
            else:
                continue

            max_time = max(max_time, time)

            queue.extend(get_valid_neighbours(r, c, oid, spread, time + 1))


        if len(oranges) != 0:
            return -1

        return max_time


print(Solution().orangesRotting([[2, 1, 1], [1, 1, 0], [0, 2, 1]]))
