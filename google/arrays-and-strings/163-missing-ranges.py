from typing import List


class Solution:
    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[str]:
        missing_ranges = []
        ln = len(nums)

        def get(idx):
            if idx == 0: return lower-1
            if idx == ln+1: return upper+1
            return nums[idx-1]

        for idx in range(1, ln+2):
            prev, curr = get(idx-1), get(idx)
            diff = abs(curr - prev)

            if diff == 1:
                continue
            
            missing_ranges.append(str(curr-1) if diff == 2 else f"{prev+1}->{curr-1}")
            
        return missing_ranges


print(Solution().findMissingRanges(nums=[0, 1, 3, 50, 75], lower=0, upper=99))
