from math import ceil
from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        R, C = len(matrix), len(matrix[0])
        def find(x, target):
            nonlocal C
            l, r = 0,  C - 1
            while l <= r:
                y = (l + r) // 2
                if matrix[x][y] == target:
                    return True
                elif matrix[x][y] > target:
                    r = y - 1
                else:
                    l = y + 1
            return False


        low, high = 0, R-1
        while low < high:
            mid = ceil((low + high) / 2)
            if matrix[mid][0] <= target:
                low = mid
            else:
                high = mid - 1

        return find(low, target)