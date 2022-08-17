from bisect import bisect_right


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

            next_digit_idx = bisect_right(digits, itr)
            if next_digit_idx == -1 or next_digit_idx == 4 or digits[next_digit_idx] > limit[i]:
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

