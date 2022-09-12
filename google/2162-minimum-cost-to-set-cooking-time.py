from math import inf


class Solution:
    def minCostSetTime(self, startAt: int, moveCost: int, pushCost: int, targetSeconds: int) -> int:

        startAt = str(startAt)

        in_sec = None
        if targetSeconds < 100:
            in_sec = str(targetSeconds)

        in_mins_perfect, in_mins_break = None, None
        if targetSeconds > 6039:
            in_mins_perfect = "9999"
        elif targetSeconds >= 60:
            m, s = divmod(targetSeconds, 60)
            if s + 60 < 100:
                in_mins_break = str(m-1) + str(s + 60)

            if m < 100:
                in_mins_perfect = str(m) + ("0" if s <= 9 else "") + str(s)

        min_cost = inf
        for digits in [in_sec, in_mins_perfect, in_mins_break]:
            if digits == None:
                continue
            itr = startAt
            cost = 0
            for dch in digits:
                if itr != dch:
                    cost += moveCost
                    itr = dch

                cost += pushCost

            min_cost = min(min_cost, cost)

        return min_cost


print(Solution().minCostSetTime(5,
                                654,
                                729,
                                755))
