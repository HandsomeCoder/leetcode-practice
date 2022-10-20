class Solution:
    def intToRoman(self, num: int) -> str:
        mapping = [[(9, "IX"), (5, "V"), (4, "IV"), (1, "I")],
                    [(90, "XC"), (50, "L"), (40, "XL"), (10, "X")],
                    [(900, "CM"), (500, "D"), (400, "CD"), (100, "C")], 
                    [(1000, "M")]]


        mul = 1
        decimal = 0
        result = []
        while num:
            x = num % 10
            num //= 10

            x *= mul

            available = mapping[decimal]
            idx = 0
            interim = []
            while x:
                n, val = available[idx]
                if x >= n:
                    x -= n
                    interim.append(val)
                    continue
            
                idx += 1

            result.append("".join(interim))
            decimal += 1 
            mul *= 10

        return "".join(result[::-1])

print(Solution().intToRoman(58))