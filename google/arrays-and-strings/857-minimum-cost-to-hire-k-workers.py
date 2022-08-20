from fractions import Fraction
from heapq import heapify, heappop, heappush
from math import inf
from typing import List


class Solution:
    def mincostToHireWorkers(self, quality: List[int], wage: List[int], k: int) -> float:

        if k == 1:
            return round(min(wage), 5)

        ln = len(quality)
        workers = [(Fraction(wage[i], quality[i]), quality[i])
                   for i in range(ln)]

        if k == ln:
            return float(max(workers, key=lambda x: x[0])[0]) * sum(list(map(lambda x: x[1], workers)))

        workers.sort()
        min_wages = inf

        pool = []
        heapify(pool)
        total_quality = 0
        for ratio, q in workers:
    
            heappush(pool, -q)
            total_quality += q
            if len(pool) > k:
                total_quality += heappop(pool)

            if len(pool) == k:
                wages = ratio * total_quality
                min_wages = min(min_wages, wages)

        return round(float(min_wages), 5)