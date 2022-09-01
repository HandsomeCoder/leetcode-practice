from typing import List


class Solution:
    def candy(self, ratings: List[int]) -> int:
        rln = len(ratings)
        if rln == 1:
            return 1

        candies = [1] * rln
        idx = 1
        while idx < rln:
            if ratings[idx-1] < ratings[idx]:
                candies[idx] = candies[idx-1] + 1
            idx += 1

        idx = rln - 2
        while idx > -1:
            if ratings[idx] > ratings[idx+1]:
                candies[idx] = max(candies[idx], candies[idx+1] + 1)
            idx -= 1

        return sum(candies)
