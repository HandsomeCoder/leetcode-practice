from collections import deque
from typing import List


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:

        hln = len(heights)
        if hln == 1:
            return heights[0]

        max_area = -1
        heights.append(-1)
        hln += 1
        stack = deque([])
        
        for idx in range(hln):
            height = heights[idx]
            left_idx = idx
            while stack and stack[-1][0] > height:
                itr, l_idx = stack.pop()
                max_area = max(max_area,  (idx - l_idx) * itr)
                left_idx = l_idx

            stack.append((height, left_idx))

        return max_area