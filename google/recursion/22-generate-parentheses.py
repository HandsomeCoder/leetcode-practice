from typing import List
from unittest import result


class Solution:

    cache = {}

    def generateParenthesis(self, n: int) -> List[str]:
        def generate(n):
            if n == 0:
                return []
            if n == 1:
                return ["()"]

            if n in self.cache:
                return self.cache[n]


            prev = generate(n-1)

            result = set()
            for pc in prev:
                result.add("("+pc+")")
                result.add("()"+pc)
                result.add(pc+"()")

            r = n-2
            l = n - r

            while l > 0  and r > 0 and l <= r:
                left = generate(l)
                right = generate(r)

                for lch in left:
                    for rch in right:
                        result.add(lch+rch)
                        result.add(rch+lch)
                
                r -= 1
                l += 1

            self.cache[n] = list(result)
            return self.cache[n]

        return generate(n)


print(Solution().generateParenthesis(3))
print(Solution().generateParenthesis(5))

["((()()))", "((()))()",
 "(())(())", "()(())()", "()()(())", ]
