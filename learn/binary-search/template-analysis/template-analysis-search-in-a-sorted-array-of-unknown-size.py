# """
# This is ArrayReader's API interface.
# You should not implement it, or speculate about its implementation
# """

class ArrayReader:
    def get(self, index: int) -> int:
        return 1


class Solution:
    def search(self, reader: ArrayReader, target: int) -> int:
        l, r = 0, 1

        value = reader.get(r)
        while(value <= target):
            l = r
            r *= 2
            value = reader.get(r)

        while(l <= r):
            m = (l+r) // 2
            itr = reader.get(m)
            if itr == target:
                return m
            elif itr > target:
                r = m - 1
            else:
                l = m + 1
        
        return -1
            