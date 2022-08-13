from typing import List


class Solution:
    def findBall(self, grid: List[List[int]]) -> List[int]:
        R, C = len(grid), len(grid[0])

        if R == 0 or C == 0:
            return None
        if C == 1:
            return [-1]

        result = []
        for i in range(C):
            x, y = 0, i
            while x < R:
                move = 0
                if grid[x][y] == 1 and y + 1 < C and grid[x][y+1] == 1:
                    y += 1
                elif grid[x][y] == -1 and y - 1 > -1 and grid[x][y-1] == -1:
                    y += (-1)
                else:
                    y += -1
                    break
                x += 1

            result.append(y)

        return result


print(Solution().findBall([[1, 1, 1, -1, -1], [1, 1, 1, -1, -1],
      [-1, -1, -1, 1, 1], [1, 1, 1, 1, -1], [-1, -1, -1, -1, -1]]))

print(Solution().findBall([[-1]]))
print(Solution().findBall([[1]]))

print(Solution().findBall([[1, 1, 1, 1, 1, 1], [-1, -1, -1, -
      1, -1, -1], [1, 1, 1, 1, 1, 1], [-1, -1, -1, -1, -1, -1]]))
