from typing import List


class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        ln = len(letters)-1
        l, r = 0, ln

        while(l < r):
            m = (l + r) // 2
            itr  = letters[m]

            if itr > target:
                r = m
            else:
                l = m + 1        

        remain = letters[l]
        if  remain <= target:
            return letters[l+1 if (l+1) < ln  else 0]

        return letters[l]