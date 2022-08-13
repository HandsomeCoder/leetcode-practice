from collections import Counter

class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        cnt = Counter(secret)
        b = 0
        c = 0

        for sch, gch in zip(secret, guess):
            if sch == gch:
                b += 1
                if cnt[gch] == 0:
                    c -= 1
                else:
                    cnt[gch] -= 1
            elif gch in cnt and cnt[gch] > 0:
                cnt[gch] -= 1
                c += 1
            
        return f"{b}A{c}B"

print(Solution().getHint("1122", "1222"))


