from collections import defaultdict
from email.policy import default
from typing import List


class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        sln = len(stones)

        if sln == 1:
            return 0

        roots = [i for i in range(sln)]
        ranks = [0 for _ in range(sln)]

        def find(x):
            if x != roots[x]:
                roots[x] = find(roots[x])
            return roots[x]

        def union(x, y):
            xroot = find(x)
            yroot = find(y)

            if xroot == yroot:
                return False

            if ranks[xroot] == ranks[yroot]:
                roots[yroot] = xroot
                ranks[xroot] += 1
            elif ranks[xroot] > ranks[yroot]:
                roots[yroot] = xroot
            else:
                roots[xroot] = yroot

            return True

        rgrid = defaultdict(list)
        cgrid = defaultdict(list)

        for idx, (r, c) in enumerate(stones):
            rgrid[r].append(idx)
            cgrid[c].append(idx)

        connected_components = len(stones)
        for idx, (r, c) in enumerate(stones):
            connected_stones = [ni for ni in rgrid[
                r]] + [ni for ni in cgrid[c]]
            for neigh in connected_stones:
                if idx == neigh:
                    continue

                if union(idx, neigh):
                    connected_components -= 1

        return len(stones) - connected_components


print(Solution().removeStones(
    stones=[[0, 0], [0, 1], [1, 0], [1, 2], [2, 1], [2, 2]]))

print(Solution().removeStones(
    stones=[[0, 0], [0, 2], [1, 1], [2, 0], [2, 2]]))
