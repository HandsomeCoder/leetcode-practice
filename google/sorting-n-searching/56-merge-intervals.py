from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        ln = len(intervals)
        intervals.sort(key=lambda x: x[0])
        merged = [intervals[0]]

        for idx in range(1, ln):
            l, r = intervals[idx]
            if merged[-1][1] >= l:
                merged[-1][1] = max(merged[-1][1], r)
            else:
                merged.append([l, r])
        return merged


print(Solution().merge([[1, 3], [2, 6], [8, 10], [15, 18]]))
print(Solution().merge([[1, 4], [4, 5]]))
