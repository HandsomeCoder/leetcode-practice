class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums)-1

        while(l <= r):
            m = int((l+r)/2)

            itr = nums[m]

            if itr == target:
                return m
            elif itr > target:
                r = m-1
            else:
                l = m+1
        return -1