from collections import defaultdict, deque
from pprint import pprint
from typing import List


class Solution:
    def pyramidTransition(self, bottom: str, allowed: List[str]) -> bool:
        mapping = defaultdict(list)

        for l, r, m in allowed:
            mapping[(l, r)].append(m)

        def get_all_tops(bottom, curr, idx, tops):
            bln = len(bottom)
            if idx == bln:
                tops.append(tuple(curr))
                return

            node = (bottom[idx-1], bottom[idx])

            for mid in mapping[node]:
                if curr and (curr[-1], mid) not in mapping:
                    continue

                curr.append(mid)
                get_all_tops(bottom, curr, idx + 1, tops)
                curr.pop()

        cache = {}

        def dfs(bottom):
            nonlocal mapping, cache
            bln = len(bottom)
            if bln == 1:
                return True

            if bottom not in cache:
                tops = []
                get_all_tops(bottom, deque([]), 1, tops)
                cache[bottom] = tops

            for top in cache[bottom]:
                if dfs(top):
                    return True

            return False

        return dfs(tuple(bottom))


pprint(Solution().pyramidTransition(bottom="AAAA",
       allowed=["AAB", "AAC", "BCD", "BBE", "DEF"]))
