from collections import deque
from typing import List


class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        R, C = len(grid), len(grid[0])

        if k >= R + C - 2:
            return R + C - 2

        max_value = 2000
        s_matrix = [[None for _ in range(C)] for _ in range(R)]
        s_matrix[-1][-1] = (0, 0)
        max_reach = (max_value, k)

        def find_min_path(x, y, obj):
            if s_matrix[x][y]:
                return s_matrix[x][y]

            if grid[x][y] == 1:
                obj += 1

            directions = [(x, y+1), (x+1, y)]
            e_move, e_obj = max_reach
            for nx, ny in directions:
                if nx < R and ny < C:
                    min_moves, min_obj = find_min_path(nx, ny, 0)
                    total_obj = obj + min_obj
                    if total_obj > k:
                        continue

                    total_moves = min_moves + 1
                    if e_move == total_moves:
                        e_obj = min(e_obj, total_obj)
                    elif e_move > total_moves:
                        e_move, e_obj = total_moves, total_obj

            s_matrix[x][y] = (e_move, e_obj)
            return s_matrix[x][y]

        for r in reversed(range(R)):
            for c in reversed(range(C)):
                if grid[r][c] == 1:
                    find_min_path(r, c, 0)

        queue = deque([(0, 0, 0)])
        min_moves = max_value
        while queue:
            x, y, move = queue.popleft()
            if grid[x][y] == "#":
                continue

            grid[x][y] = "#"
            s_matrix[x][y] = None if s_matrix[x][y] == max_reach else s_matrix[x][y]
            
            if s_matrix[x][y]:
                min_moves = min(min_moves, move + s_matrix[x][y][0])
                continue

            for nx, ny in [(x, y+1), (x+1, y), (x, y-1), (x-1, y)]:
                if 0 <= nx < R and 0 <= ny < C and grid[nx][ny] != "#":
                    if grid[nx][ny] == 0:
                        queue.append((nx, ny, move + 1))
                    else:
                        min_moves = min(min_moves, move +
                                        1 + s_matrix[nx][ny][0])

        return -1 if min_moves == max_value else min_moves