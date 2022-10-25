from typing import List


class Solution:
    def minTotalDistance(self, grid: List[List[int]]) -> int:

        def get_min_distance(arr):
            l, r = 0, len(arr)-1

            distance = 0
            while l < r:
                distance += (arr[r] - arr[l])
                l += 1
                r -= 1
            return distance

        R, C = len(grid), len(grid[0])
        cols, rows = [], []
        for x in range(R):
            for y in range(C):
                if grid[x][y] == 1:
                    rows.append(x)

        for y in range(C):
            for x in range(R):
                if grid[x][y] == 1:
                    cols.append(y)


        return get_min_distance(rows) + get_min_distance(cols)



print(Solution().minTotalDistance(
    [[1, 1, 1, 0], [0, 0, 0, 0], [1, 0, 0, 1]]))
