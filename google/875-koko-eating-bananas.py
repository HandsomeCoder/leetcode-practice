from math import ceil
from typing import List

class Solution:

    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def hours_used(piles, per_hour):
            hours = 0
            for pile in piles:
                hours += ceil(pile / per_hour)
            return hours

        pln = len(piles)
        r = max(piles)
        if pln == h:
            return r

        l = max(1, sum(piles) // (h+1))
        min_hours = r
        while l <= r:
            m = (l + r) // 2
            hu = hours_used(piles, m)

            if hu <= h:
                r = m - 1
                min_hours = min(min_hours, m)
            else:
                l = m + 1

        return min_hours


print(Solution().minEatingSpeed(piles=[312884470], h=312884469))
