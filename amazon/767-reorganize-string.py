from collections import Counter


class Solution:
    def reorganizeString(self, s: str) -> str:
        if len(s) == 1:
            return s

        counter = [(v, k) for k, v in Counter(s).items()]
        cln = len(counter)
        if cln == 1:
            return ""

        counter.sort(reverse=True)

        cnt, ch = counter[0]
        result = [[ch] for _ in range(cnt)]

        rln = len(result)
        idx = 0
        valid = False
        for ci in range(1, cln):
            cnt, ch = counter[ci]
            for _ in range(cnt):
                result[idx].append(ch)
                idx += 1
                if idx >= rln-1:
                    valid = True
                if idx == rln:
                    idx = 0

        return "".join(["".join(item) for item in result]) if valid else ""
