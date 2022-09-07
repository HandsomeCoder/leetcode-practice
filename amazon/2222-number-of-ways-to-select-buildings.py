from collections import defaultdict
from email.policy import default
from unittest import result


class Solution:
    def numberOfWays(self, s: str) -> int:
        sln = len(s)
        counter = defaultdict(lambda: 0)
        groups = {"0": [0 for _ in range(sln)], "1": [0 for _ in range(sln)]}
        for idx in range(sln):
            sch= s[idx]
            counter[sch] += 1
            groups["0"][idx] = counter["0"]
            groups["1"][idx] = counter["1"]



        result= 0
        for idx in range(1, sln-1):
            sch= s[idx]
            alt= "1" if sch == "0" else "0"
            result += (groups[alt][idx] * (groups[alt][-1] - groups[alt][idx]))
        return result

print(Solution().numberOfWays("10001100100"))
