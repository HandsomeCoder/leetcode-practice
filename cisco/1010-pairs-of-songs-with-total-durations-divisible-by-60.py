from collections import defaultdict
from email.policy import default
from typing import List


class Solution:
    cache = {}

    def get_remain(self, x: int) -> int:
        if x not in self.cache:
            self.cache[x] = (x % 60)

        return self.cache[x]

    def numPairsDivisibleBy60(self, time: List[int]) -> int:

        compliment = defaultdict(lambda: 0)

        count = 0
        for item in time:
            remain = self.get_remain(item)
            if remain in compliment:
                count += compliment[remain]

            compliment[0 if remain == 0 else (60 - remain)] += 1

        return count


print(Solution().numPairsDivisibleBy60([60, 60, 60]))
