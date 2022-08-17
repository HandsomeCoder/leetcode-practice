from bisect import bisect_right
from unicodedata import digit


class Solution:
    def nextClosestTime(self, time: str) -> str:
        time = list(time)
        limit = [2, 3 if time[0] == "2" else 9, -1, 5, 9]

        idx = [0, 1, 3, 4]
        digits = [int(time[i]) for i in idx]
        digits.sort()

        for i in reversed(idx):
            itr = int(time[i])
            if itr == limit[i]:
                continue

            next_digit_idx = -1

            l, r = 0, 3
            while l < r:
                m = (l+r) // 2
                if digits[m] > itr:
                    r = m
                else:
                    l = m+1

            next_digit_idx = -1 if digits[r] == itr else r


            if next_digit_idx == -1 or digits[next_digit_idx] > limit[i]:
                continue

            time[i] = str(digits[next_digit_idx])
            min_digit = min(digits)
            for j in range(i+1, 5):
                if j == 2:
                    continue
                time[j] = str(min_digit)

            
            return "".join(time)
        
        time[1] = time[3] = time[4] = time[0]
        return "".join(time)

print(Solution().nextClosestTime("13:55"))