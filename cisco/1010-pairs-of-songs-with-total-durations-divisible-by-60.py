from typing import List


class Solution:
    cache = {}

    def get_remain(self, x: int) -> int:
        if x not in self.cache:
            self.cache[x] = (x % 60)

        return self.cache[x]

    def numPairsDivisibleBy60(self, time: List[int]) -> int:

        compliment = [0 for _ in range(60)]
        count = 0
        for item in time:
            remain = self.get_remain(item)
            if remain in compliment:
                count += compliment[remain]

            compliment[0 if remain == 0 else (60 - remain)] += 1

        return count