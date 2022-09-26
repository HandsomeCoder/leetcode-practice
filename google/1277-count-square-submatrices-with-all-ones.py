from typing import List


class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        R, C = len(matrix), len(matrix[0])

        cnt = sum(matrix[0])        
        for i in range(1,R):
            cnt += matrix[i][0]
        
        for r in range(1,R):
            for c in range(1,C):
                if matrix[r][c] == 1:
                    matrix[r][c] += (min(matrix[r-1][c], matrix[r][c-1]) if matrix[r-1][c-1] else 0)
                    cnt += matrix[r][c]

        return cnt  