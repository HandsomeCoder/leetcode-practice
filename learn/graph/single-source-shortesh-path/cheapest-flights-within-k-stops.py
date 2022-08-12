from typing import List


class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        MAX_VALUE = 100000
        matrix = [[MAX_VALUE] * n for _ in range(2)]
        matrix[0][src] = matrix[1][src] = 0

        for i in range(k+1):
            for s, d, price in flights:
                prev = matrix[1 - i & 1]
                curr = matrix[i & 1]
                curr[d] = min(curr[d], prev[s] + price)

        return matrix[k & 1][dst] if matrix[k & 1][dst] != MAX_VALUE else -1


print(Solution().findCheapestPrice(4,
                                   [[0, 1, 100], [1, 2, 100], [2, 0, 100],
                                       [1, 3, 600], [2, 3, 200]],
                                   0,
                                   3,
                                   1))
