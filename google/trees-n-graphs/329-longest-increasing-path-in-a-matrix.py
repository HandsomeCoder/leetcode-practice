from typing import List


class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        R, C = len(matrix), len(matrix[0])

        if R == 1 and C == 1:
            return 1

        result = [[-1 for _ in range(C)] for _ in range(R)]

        def explore(i, j):
            if result[i][j] != -1:
                return result[i][j]

            result[i][j] = 1
            directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
            for x, y in directions:
                mi = i + x
                mj = j + y
                if 0 <= mi < R and 0 <= mj < C and matrix[i][j] < matrix[mi][mj]:
                    result[i][j] = max(result[i][j], 1 + explore(mi, mj))

            return result[i][j]

        longest_inc_seq = -1
        for i in range(R):
            for j in range(C):
                if result[i][j] == -1:
                    longest_inc_seq = max(longest_inc_seq, explore(i, j))

        return longest_inc_seq


print(Solution().longestIncreasingPath(
    matrix=[[9, 9, 4], [6, 6, 8], [2, 1, 1]]))
print(Solution().longestIncreasingPath(
    matrix= [[3,4,5],[3,2,6],[2,2,1]]))

print(Solution().longestIncreasingPath(
    matrix= [[1,2],[4,3]]))

print(Solution().longestIncreasingPath(
    matrix= [[1,2,3],[6,5,4],[7,8,9]]))
