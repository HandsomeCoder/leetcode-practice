from collections import deque
from re import X
from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        nrow, ncol = len(grid) - 1, len(grid[0]) - 1

        def get_valid_neighbours(i, j, nrow, ncol):
            neighbours = []
            if i > 0:
                neighbours.append((i-1, j))
            if j > 0:
                neighbours.append((i, j-1))
            if i < nrow:
                neighbours.append((i+1, j))
            if j < ncol:
                neighbours.append((i, j+1))

            return neighbours

        def explore_island(node, search_stack):
            island_stack = deque([node])
            while island_stack:
                itr = island_stack.pop()
                x, y = itr

                if grid[x][y] == "-1":
                    continue

                if (grid[x][y] == "0"):
                    search_stack.append((x, y))
                elif (grid[x][y] == "1"):
                    grid[x][y] = "-1"
                    island_stack.extend(filter(
                        lambda itr: grid[itr[0]][itr[1]] != "-1", get_valid_neighbours(x, y, nrow, ncol)))

        nrow, ncol = len(grid) - 1, len(grid[0]) - 1
        search_stack = deque([(0, 0)])
        island_count = 0
        while search_stack:

            itr = search_stack.pop()
            i, j = itr

            if grid[i][j] == "-1":
                continue

            if grid[i][j] == "1":
                island_count += 1
                explore_island((i, j), search_stack)

            grid[i][j] = "-1"
            search_stack.extend(filter(
                lambda itr: grid[itr[0]][itr[1]] != "-1", get_valid_neighbours(i, j, nrow, ncol)))

        return island_count


print(Solution().numIslands(
    [["0", "1", "0"], ["1", "0", "1"], ["0", "1", "0"]]))
print(Solution().numIslands([["1", "1", "1", "1", "0"], [
      "1", "1", "0", "1", "0"], ["1", "1", "0", "0", "0"], ["0", "0", "0", "0", "0"]]))
print(Solution().numIslands(
    [["1", "1", "0", "0", "0"], ["1", "1", "0", "0", "0"], ["0", "0", "1", "0", "0"], ["0", "0", "0", "1", "1"]]))
