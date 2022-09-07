from math import ceil
from typing import List


class Solution:
    def platesBetweenCandles(self, s: str, queries: List[List[int]]) -> List[int]:
        
        sln = len(s)
        prev_candles = []
        left_move = [None for _ in range(sln)]
        right_move = [None for _ in range(sln)]

        cnt = 0
        prev_candle_at = -1
        for idx in range(sln):
            sch = s[idx]
            if sch == "|":
                prev_candle_at = idx
                cnt += 1
            prev_candles.append(cnt)
            if cnt > 0:
                left_move[idx] = (prev_candle_at - idx)

        cnt = 0
        prev_candle_at = -1
        for idx in reversed(range(sln)):
            sch = s[idx]
            if sch == "|":
                prev_candle_at = idx

            if prev_candle_at !=  -1:
                right_move[idx] = (prev_candle_at - idx)


        result = []
        cache = {}
        for low, high in queries:
            node = (low, high)
            if node in cache:
                result.append(cache[node])
                continue

            if low == high or right_move[low] == None or left_move[high] == None:
                result.append(0)
                continue
            
            left = low + right_move[low]
            right = high + left_move[high]

            if left >= right:
                result.append(0)
                continue

            cache[node] = (right - left) - (prev_candles[right] - prev_candles[left])
            result.append(cache[node])
        return result