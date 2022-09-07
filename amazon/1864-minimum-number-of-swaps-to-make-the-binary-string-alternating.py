from collections import defaultdict


class Solution:
    def minSwaps(self, s: str) -> int:

        def count_swap(next_ch, s):
            cnt = 0
            for sch in s:
                if sch != next_ch:
                    cnt += 1
                next_ch = "1" if next_ch == "0" else "0"
            return cnt // 2
            
        counter = defaultdict(lambda: 0)
        for sch in s:
            counter[sch] += 1
 
        if abs(counter["0"] - counter["1"]) > 1:
            return -1

        if counter["0"] > counter["1"]:
            return count_swap("0", s)
        elif counter["1"] > counter["0"]:
            return count_swap("1", s)
        else:
            return min(count_swap("0", s), count_swap("1", s))