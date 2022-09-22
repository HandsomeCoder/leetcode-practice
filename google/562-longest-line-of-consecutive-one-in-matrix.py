from typing import List


class Solution:
    def longestLine(self, mat: List[List[int]]) -> int:

        R, C = len(mat), len(mat[0])
        results = [[[0, 0, 0, 0] for _ in range(C)] for _ in range(2)]

        max_len = 0
        for r in range(R):
            selector = r & 1
            curr = results[selector]
            prev = results[1 - selector]

            for c in range(C):
                if mat[r][c] == 0:
                    for i in range(4):
                        curr[c][i] = 0
                else:
                    for direction in [-1, 0, 1]:
                        idx = direction + 1
                        curr[c][idx] = 1

                        nc = c + direction
                        if 0 <= nc < C:
                            curr[c][idx] = curr[c][idx] + prev[nc][idx]

                    curr[c][3] = 1
                    if (0 <= c-1 < C):
                        curr[c][3] += curr[c-1][3]

                    max_len = max(max_len, max(curr[c]))
                
        return max_len
