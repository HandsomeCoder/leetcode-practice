from typing import List

class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        def prefix_max(arr):
            ln = len(arr)
            result = [item for item in arr]
            for idx in range(1, ln):
                result[idx] = max(result[idx], result[idx-1] - 1)

            return result

        def suffix_max(arr):
            ln = len(arr)
            result = [item for item in arr]
            for idx in reversed(range(ln-1)):
                result[idx] = max(result[idx], result[idx+1] - 1)
                
            return result

        R = len(points)
        if R == 1:
            return max(points[0])

        C = len(points[0])
        for r in range(1, R):
            prefix, suffix = prefix_max(points[r-1]), suffix_max(points[r-1])
            for c_idx in range(C):
                points[r][c_idx] = points[r][c_idx] + max(prefix[c_idx], suffix[c_idx])

        return max(points[-1])