from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_till = min_till = prices[0]
        profit = 0
        for price in prices:
            if price < min_till:
                profit = max(max_till - min_till, profit)
                max_till = min_till = price
            elif price > max_till:
                max_till = price

        return max(max_till - min_till, profit)
            