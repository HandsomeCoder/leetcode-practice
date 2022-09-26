from typing import List


class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:

        def find(idx, computed, informTime):
            if computed[idx] != -1:
                return computed[idx]

            computed[idx] = informTime[idx]
            computed[idx] += find(manager[idx], computed, informTime)
            
            return computed[idx]

        max_time = informTime[headID]
        ln = len(manager)
        computed = [-1 for _ in range(ln)]
        computed[headID] = informTime[headID]

        for idx in range(ln):
            max_time = max(max_time, find(idx, computed, informTime))

        return max_time
