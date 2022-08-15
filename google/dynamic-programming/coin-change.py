from typing import List


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [amount+1] * (amount+1)
        dp[0] = 0

        for total in range(1, amount+1):

            possibilies = [dp[total]]
            for coin in coins:

                if total - coin >= 0:
                    possibilies.append(dp[total - coin] + 1)

            dp[total] = min(possibilies)

        return -1 if dp[-1] == amount + 1 else dp[-1]


print(Solution().coinChange([1, 2, 5],
                            11))
