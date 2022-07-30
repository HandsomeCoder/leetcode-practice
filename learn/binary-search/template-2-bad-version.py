# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        l, r = 1, n

        while(l <= r):
            m = (l+r) // 2
            
            curr = isBadVersion(m)
            next = isBadVersion(m+1)
            if((not curr) and next):
                return m
            elif(next):
                r = m - 1
            else:
                l = m + 1

        return 1