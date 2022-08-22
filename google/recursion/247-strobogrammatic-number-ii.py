from collections import defaultdict
from typing import List


class Solution:
    cache = {}
    cache_zero = defaultdict(list)

    def findStrobogrammatic(self, n: int) -> List[str]:

        def build_strobogrammatic(n):
            if n in self.cache:
                return self.cache[n]

            if n == 1:
                return ["0", "1", "8"]
            elif n == 2:
                self.cache_zero[n] = ["00"]
                return ["11", "69", "88", "96"]

            prevs = build_strobogrammatic(n-2) + self.cache_zero[n-2]
            itrs = ["11", "69", "88", "96"]

            result = []
            for itr in itrs:
                for prev in prevs:
                    result.append(itr[0] + prev + itr[1])

            for prev in prevs:
                self.cache_zero[n].append("0" + prev + "0")

            self.cache[n] = result
            return self.cache[n]

        return build_strobogrammatic(n)


print(Solution().findStrobogrammatic(5))
print(Solution().findStrobogrammatic(4))
