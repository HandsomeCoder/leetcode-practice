from collections import deque
from pprint import pprint
from typing import List


class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        R, C = len(grid), len(grid[0])
        max_value = 40 * 40
        s_matrix = [[max_value for _ in range(C)] for _ in range(R)]
        not_visited = [[True for _ in range(C)] for _ in range(R)]

        not_visited[0][0] = False
        s_matrix[0][0] = 0

        queue = deque([(0, 0, 0, 0)])
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        while queue:
            x, y, move, ob = queue.popleft()
            not_visited[x][y] = False

            for dx, dy in directions:
                nx = x + dx
                ny = y + dy

                if 0 <= nx < R and 0 <= ny < C and not_visited[nx][ny]:
                    s_matrix[nx][ny] = min(s_matrix[nx][ny], move + 1)
                    if grid[nx][ny] == 0:
                        queue.append((nx, ny, move + 1, ob))
                    elif ob < k:
                        queue.append((nx, ny, move + 1, ob + 1))

        return -1 if s_matrix[-1][-1] == max_value else s_matrix[-1][-1]

pprint(Solution().shortestPath(
    [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
    [0, 1, 1, 1, 1, 1, 1, 1, 1, 0], 
    [0, 1, 0, 0, 0, 0, 0, 0, 0, 0], 
    [0, 1, 0, 1, 1, 1, 1, 1, 1, 1], 
    [0, 1, 0, 0, 0, 0, 0, 0, 0, 0], 
    [0, 1, 1, 1, 1, 1, 1, 1, 1, 0], 
    [0, 1, 0, 0, 0, 0, 0, 0, 0, 0], 
    [0, 1, 0, 1, 1, 1, 1, 1, 1, 1], 
    [0, 1, 0, 1, 1, 1, 1, 0, 0, 0], 
    [0, 1, 0, 0, 0, 0, 0, 0, 1, 0], 
    [0, 1, 1, 1, 1, 1, 1, 0, 1, 0], 
    [0, 0, 0, 0, 0, 0, 0, 0, 1, 0]], 1))
