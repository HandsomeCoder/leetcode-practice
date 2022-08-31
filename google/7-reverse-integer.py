from math import ceil

class Solution:
    def reverse(self, x: int) -> int:
        if x == 0:
            return 0

        result, rx = 0, []
        limit = 2147483647
        decimal = 1
        if x > 0:
            while x > 0:
                x, ri = divmod(x, 10)
                rx.append(ri)
        else:
            limit = -2147483648
            decimal = -1
            while x < 0:
                rx.append(-1 * (x % -10))
                x = ceil(x / 10)

        for val in reversed(rx):
            if (limit // decimal < val):
                return 0
            add = (val * decimal)
            result += add
            limit -= add
            decimal *= 10

        return result