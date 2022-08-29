from typing import List


class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        cpln = len(cardPoints)
        if cpln == k:
            return sum(cardPoints)

        def next_idx(x, k):
            x += 1
            return k - x if x >= k else x

        l, r = cpln-k, cpln-1
        prev_sum = max_sum = sum(cardPoints[l: r+1])
        while True:
            prev_sum -= cardPoints[l]
            l = next_idx(l, cpln)
            r = next_idx(r, cpln)
            prev_sum += cardPoints[r]
            
            max_sum = max(max_sum, prev_sum)

            if r + 1 == k:
                break

        return max_sum  
        