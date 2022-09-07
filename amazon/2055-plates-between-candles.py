from math import ceil
from typing import List


class Solution:
    def platesBetweenCandles(self, s: str, queries: List[List[int]]) -> List[int]:
        
        # def find_gte(x, arr, l, r):
        #     while l < r:
        #         m = (l+r) // 2
        #         if arr[m] == x:
        #             l = m
        #             break
        #         if arr[m] < x:
        #             l = m + 1
        #         else:
        #             r = m
        #     return l


        # def find_lte(x, arr, l, r):
        #     while l < r:
        #         m = ceil((l+r) / 2)
        #         if arr[m] == x:
        #             r = m
        #             break
        #         if arr[m] < x:
        #             l = m
        #         else:
        #             r = m - 1
        #     return r

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


print(Solution().platesBetweenCandles("**|**|***|",  [[2, 5], [5, 9]]))
print(Solution().platesBetweenCandles("***|**|*****|**||**|*",
      [[1, 17], [4, 5], [14, 17], [5, 11], [15, 16]]))
