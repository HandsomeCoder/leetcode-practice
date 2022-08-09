from typing import List


class Solution:
    def numFactoredBinaryTrees(self, arr: List[int]) -> int:
        n = len(arr)

        arr.sort()
        MOD = 10 ** 9 + 7
        roots = [1] * n
        idxMap = {x: i for i, x in enumerate(arr)}
        for idx, value in enumerate(arr):
            for j in range(idx):
                if value % arr[j] == 0:
                    result = int(value / arr[j])
                    if result in idxMap:
                        roots[idx] += roots[j] * roots[idxMap[result]]
                        roots[idx] %= MOD

        return sum(roots) % MOD

print(Solution().numFactoredBinaryTrees([4,2]))
print(Solution().numFactoredBinaryTrees([18,3,6,2]))