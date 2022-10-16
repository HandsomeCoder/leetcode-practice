from math import inf

class Solution:
    def getLengthOfOptimalCompression(self, s: str, k: int) -> int:

        def count(idx, lastCh, lastChCnt, k, ln):
            nonlocal s

            if k < 0:
                return inf
            if idx == ln:
                return 0

            del_ch = count(idx+1, lastCh, lastChCnt, k-1, ln)
            if s[idx] == lastCh:
                keep_ch = count(idx+1, lastCh, lastChCnt + 1, k) + (lastChCnt in {1, 9, 99})
            else:
                keep_ch = count(idx+1, s[idx], 1, k)

            return min(del_ch, keep_ch)


        sln = len(s)
        if sln == k:
            return 0

        return count(0, "#", 0, k, sln)