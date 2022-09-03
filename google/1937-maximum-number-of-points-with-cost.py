from bisect import bisect_left
from typing import List


class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        R = len(points)

        if R == 1:
            return max(points[0])

        C = len(points[0]) 
        cln = C-1

        for r in range(1, R):
            prev_max_value = -1
            # prev_max_value_idx = []
            # for idx, val in enumerate(points[r-1]):
            #     if val == prev_max_value:
            #         prev_max_value_idx.append(idx)
            #     elif val > prev_max_value:
            #         prev_max_value = val
            #         prev_max_value_idx = [idx]

            for c_idx, c_val in enumerate(points[r]):

                prev = points[r-1]                
                if prev_max_value == -1:
                    for idx in range(c_idx, cln):
                        diff = abs(idx - c_idx)
                        val = prev[idx] - diff
                        if val > prev_max_value:
                            prev_max_value = val
                            prev_max_value_diff = diff
                
                
                
                
                
                value = c_val
                # p_max_value = value + prev_max_value
                # if len(prev_max_value_idx) == 1:
                #     p_max_value -= abs(c_idx - prev_max_value_idx[0])
                # else:
                #     s_idx = bisect_left(prev_max_value_idx, c_idx)
                #     max_idx = len(prev_max_value_idx) - 1
                #     p_max_value -= min(abs(c_idx - prev_max_value_idx[min(max_idx, s_idx)]), abs(
                #         c_idx - prev_max_value_idx[min(max_idx, s_idx+1)]))


                low = high = c_idx
                for p_idx in range(max(1,c_val)):
                    new_val = c_val - p_idx
                    value = max(value, new_val + prev[low], new_val + prev[high])
                    if low == 0 and high == cln:
                        break

                    low = max(0, low-1)
                    high = min(cln, high+1)

                points[r][c_idx] = value

        return max(points[-1])