from typing import List


class Solution:
    def removeOnes(self, grid: List[List[int]]) -> bool:
        rln, cln = len(grid), len(grid[0])

        if rln == 1:
            return True

        for row in range(1, rln):
            same = diff = 0
            for prev, curr in zip(grid[row-1], grid[row]):
                if prev == curr:
                    same += 1
                else:
                    diff += 1

            if same != cln and diff != cln:
                return False
                
        return True
