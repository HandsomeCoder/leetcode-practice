from collections import deque
from typing import List


class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        stack = deque([])
        ln = len(arr)
        
        prev_min = [-1 for _ in range(ln)]
        result = [0 for _ in range(ln+1)]
        
        for idx in range(ln):
            while stack and arr[stack[-1]] > arr[idx]:
                stack.pop()
            if stack:
                prev_min[idx] = stack[-1]
            stack.append(idx)

        for idx in range(ln):
            result[idx] = result[prev_min[idx]] + ((idx - prev_min[idx]) * arr[idx])

        return sum(result) % 1000000007 