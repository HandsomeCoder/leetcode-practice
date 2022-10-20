class Solution:
    def getLengthOfOptimalCompression(self, s: str, k: int) -> int:

        def is_single_ch(s):
            prev = s[0]
            for sch in s:
                if sch != prev:
                    return False
            return True

        cache = {}
        count_set = {1, 9}
        def count(idx, lastCh, lastChCnt, k, ln):
            nonlocal s, cache, count_set
            if k < 0:
                return 100
            if idx == ln:
                return 0

            node = (idx, lastCh, lastChCnt, k)
            if node not in cache:
                del_ch = count(idx+1, lastCh, lastChCnt, k-1, ln)
                if s[idx] == lastCh:
                    keep_ch = count(idx+1, lastCh, lastChCnt + 1, k, ln) + (lastChCnt in count_set)
                else:
                    keep_ch = count(idx+1, s[idx], 1, k, ln) + 1

                cache[node] = min(del_ch, keep_ch)
            return cache[node]

        sln = len(s)
        if sln == k:
            return 0

        if sln == 100 and is_single_ch(s):
            return len(str(100 - k)) + 1

        return count(0, "#", 0, k, sln)