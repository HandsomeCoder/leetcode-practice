from collections import deque
from math import ceil
from typing import List


class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        count = max_count = 0
        start = -1

        for idx, seat in enumerate(seats):
            if seat == 0:
                count += 1
                continue

            if start == -1:
                start = count
            else:
                max_count = max(max_count, count)
            count = 0
                        
        return max(start, count, ceil(max_count / 2))  
