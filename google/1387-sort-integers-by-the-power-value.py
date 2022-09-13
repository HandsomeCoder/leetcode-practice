class Solution:
    cache = {1: 0}
    def getKth(self, lo: int, hi: int, k: int) -> int:
        def get_pow(n):
            if n not in self.cache:
                self.cache[n] = (get_pow((n*3) + 1) if n & 1 else get_pow(n / 2)) + 1

            return self.cache[n]

        nums = []
        for n in range(lo, hi+1):
            nums.append((get_pow(n), n))

        nums.sort()

        return nums[k-1]
