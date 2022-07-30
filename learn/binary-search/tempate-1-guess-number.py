# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        l, r = 0, n

        while(l <= r):
            m = (l+r) // 2
            result = guess(m)
            if(result == 0):
                return m
            elif(result == -1):
                r = m - 1
            else:
                l = m + 1