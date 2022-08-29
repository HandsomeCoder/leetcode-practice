from typing import List


class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        amount += 1
        count = [0 for _ in range(amount)]
        count[0] = 1

        coins.sort()
        for coin in coins:
            for idx in range(1, amount):
                prev_idx = idx - coin
                if prev_idx < 0:
                    continue
                
                count[idx] += count[prev_idx]

        return count[-1]