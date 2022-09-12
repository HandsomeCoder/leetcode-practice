from collections import defaultdict
from email.policy import default


class Solution:
    def shortestWay(self, source: str, target: str) -> int:

        ch_idx = defaultdict(list)
        for idx, sch in enumerate(source):
            ch_idx[sch].append(idx)

        cnt = 1
        itr = defaultdict(lambda: 0)
        idx = -1
        for tch in target:
            if tch not in ch_idx:
                return -1

            idxs = ch_idx[tch]
            cln = len(idxs)
            while itr[tch] < cln and idxs[itr[tch]] <= idx:
                itr[tch] = itr[tch] + 1

            if itr[tch] == cln:
                cnt = cnt + 1
                itr = defaultdict(lambda: 0)
                idx = -1

            idx = ch_idx[tch][itr[tch]]

        return cnt