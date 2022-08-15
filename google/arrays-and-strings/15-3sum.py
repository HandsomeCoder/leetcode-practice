from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        visited, result = set(), set()
        complements = {}
        for i, first in enumerate(nums):
            if first in visited:
                continue
            visited.add(first)
            for second in nums[i+1:]:
                complement = (first + second) * -1
                if complement in complements and complements[complement] == i:
                    result.add(tuple(sorted([first, second, complement])))
                complements[second] = i

        return list(result)


print(Solution().threeSum([-1,0,1,2,-1,-4]))
