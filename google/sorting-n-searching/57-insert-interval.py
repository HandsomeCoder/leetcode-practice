from heapq import merge
from math import ceil
from typing import List


class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        ln = len(intervals)
        if ln == 0:
            return [newInterval]

        l1 = l2 = 0
        r1 = r2 = ln-1
        while l1 < r1 or l2 < r2:
            m1 = ceil((l1 + r1) / 2)
            m2 = (l2 + r2) // 2
            if intervals[m1][0] <= newInterval[0]:
                l1 = m1
            else:
                r1 = m1 - 1

            if intervals[m2][0] >= newInterval[1]:
                r2 = m2
            else:
                l2 = m2 + 1

        low = l1
        if intervals[l1][1] < newInterval[0]:
            low += 1
        elif intervals[l1][0] > newInterval[0]:
            low -= 1

        high = r2
        if newInterval[1] > intervals[r2][1]:
            high += 1
        elif newInterval[1] < intervals[r2][0]:
            high -= 1

        if low == high:
            if low == -1:
                return [newInterval] + intervals
            elif low == ln:
                return intervals + [newInterval]

        low = low if low > -1 else 0
        high = high if high < ln else ln-1

        return intervals[:low] + [[min(newInterval[0], intervals[low][0]),
                                   max(newInterval[1], intervals[high][1])]] + intervals[high+1:]


# print(Solution().insert([[1, 3], [6, 9]], [2, 5]))
# # print(Solution().insert([[1, 3], [6, 9]], [0, 5]))
# print(Solution().insert([[1, 3], [6, 9]], [10, 12]))
# print(Solution().insert([[0, 5], [9, 12]], [7, 16]))
# print(Solution().insert([[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]],  [4, 8]))
# print(Solution().insert([[2, 4]],  [1, 10]))
# print(Solution().insert([[1, 10]],  [2, 4]))
# print(Solution().insert([[1, 10]],  [2, 40]))
print(Solution().insert([[1, 5], [6, 8]],  [0, 9]))
