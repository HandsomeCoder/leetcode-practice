from collections import defaultdict
from typing import List

class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        
        seen = defaultdict(lambda: 0)
        cnt = 0
        mirror = 0
        for wch in words:
            rwch = wch[1]+wch[0]

            if rwch in seen and seen[rwch] > 0:
                cnt += 4
                seen[rwch] -= 1
                if wch == rwch:
                    mirror -= 1
            else:
                if wch == rwch:
                    mirror += 1
                seen[wch] += 1

        if mirror > 0:
            cnt += 2

        return cnt