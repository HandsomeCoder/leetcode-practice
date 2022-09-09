from lib2to3.pgen2.tokenize import generate_tokens
from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def backtrack(k, first, curr):
            if len(curr) == k:  
                output.append(curr[:])
                return

            for i in range(first, n):
                curr.append(nums[i])
                backtrack(k, i + 1, curr)
                curr.pop()
        
        output = []
        n = len(nums)
        for k in range(n + 1):
            backtrack(k, 0, [])
        return output


print(Solution().subsets([1, 2, 3]))
