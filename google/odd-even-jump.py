from operator import pos
from typing import List


class Solution:
    def oddEvenJumps(self, arr: List[int]) -> int:
        n = len(arr)
        next_larger = [-1 for i in range(n)]
        next_smaller = [-1 for i in range(n)]

        data = sorted([[a, i] for i, a in enumerate(arr)],
                      key=lambda x: [x[0], x[1]])
        stack = []
        next_larger[n-1], next_smaller[n-1] = n-1, n-1
        for i in range(n):
            while stack and data[i][1] > stack[-1]:
                next_larger[stack.pop()] = data[i][1]
            stack.append(data[i][1])

        data = sorted([[a, i] for i, a in enumerate(arr)],
                      key=lambda x: [-x[0], x[1]])
        stack = []
        for i in range(n):
            while stack and data[i][1] > stack[-1]:
                next_smaller[stack.pop()] = data[i][1]
            stack.append(data[i][1])

        dp = [[True for i in range(n)] for j in range(2)]
        result = 1
        for i in range(n-2, -1, -1):
            if next_larger[i] == -1:
                dp[0][i] = False
            else:
                dp[0][i] = dp[1][next_larger[i]]
                if dp[0][i]:
                    result += 1
            if next_smaller[i] == -1:
                dp[1][i] = False
            else:
                dp[1][i] = dp[0][next_smaller[i]]
        return result


print(Solution().oddEvenJumps(
    [2, 3, 1, 1, 4]), 2)
