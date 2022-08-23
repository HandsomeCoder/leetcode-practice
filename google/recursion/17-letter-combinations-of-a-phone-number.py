from typing import List
from unittest import result


class Solution:

    cache = {}

    def letterCombinations(self, digits: str) -> List[str]:
        mapping = {
            "2": ["a", "b", "c"],
            "3": ["d", "e", "f"],
            "4": ["g", "h", "i"],
            "5": ["j", "k", "l"],
            "6": ["m", "n", "o"],
            "7": ["p", "q", "r", "s"],
            "8": ["t", "u", "v"],
            "9": ["w", "x", "y", "z"],
        }

        def build_combinations(digits):
            ln = len(digits)
            if ln == 0:
                return ""

            if ln == 1:
                return mapping[digits]

            if digits in self.cache:
                return self.cache[digits]

            mid = ln // 2

            left = build_combinations(digits[:mid])
            right = build_combinations(digits[mid:])

            self.cache[digits] = [lch+rch for lch in left for rch in right]
            return self.cache[digits]

        return build_combinations(digits)


print(Solution().letterCombinations("2323"))
