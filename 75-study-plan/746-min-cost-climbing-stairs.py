from typing import List

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        ln = len(cost)

        if ln == 2:
            return min(cost)

        for idx in range(2, ln):
            cost[idx] += min(cost[idx-1], cost[idx-2])

        return min(cost[-1], cost[-2])