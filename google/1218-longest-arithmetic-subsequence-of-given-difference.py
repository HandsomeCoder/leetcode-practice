from collections import defaultdict
from typing import List


class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        next_numbers = {}
        max_ln = 0
        for num in arr:
            ln = next_numbers.get(num, 0) + 1
            next_key = num + difference
            next_numbers[next_key] = ln

            max_ln = max(max_ln, ln)

        return max_ln


print(Solution().longestSubsequence([3, 4, -3, -2, -4], -5))
