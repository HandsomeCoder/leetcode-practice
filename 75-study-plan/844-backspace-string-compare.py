from collections import deque
from itertools import zip_longest
from tkinter import S


class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        sln, tln = len(s), len(t)

        def get_last_valid_idx(idx, str):
            if idx < 0:
                return -1

            if str[idx] != "#":
                return idx

            skip = 0
            while True:
                while idx >= 0 and str[idx] == "#":
                    idx -= 1
                    skip += 1

                if skip == 0:
                    break

                idx -= 1
                skip -= 1

            return idx if idx >= 0 else -1

        while sln >= 0 or tln >= 0:
            sln = get_last_valid_idx(sln - 1, s)
            tln = get_last_valid_idx(tln - 1, t)

            if sln == -1 or tln == -1:
                if sln == tln:
                    break
                else:
                    return False

            if s[sln] != t[tln]:
                return False

        return True


print(Solution().backspaceCompare("bxj##tw", "bxo#j##tw"), True)
print(Solution().backspaceCompare("a#c#", "ac##"), True)
print(Solution().backspaceCompare("##ac", "ac"), True)
print(Solution().backspaceCompare("a#c", "b"), False)
