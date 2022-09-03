class Solution:

    def numDecodings(self, s: str) -> int:
        sl, p1 = len(s), 1
        curr = p1 = 1 if "1" <= s[0] <= "9" else 0
        for idx in range(1, sl):
            if "1" <= s[idx] <= "9":
                curr = p1

            if "10" <= s[idx-1: idx+1] <= "26":
                curr += p2

            p2, p1 = p1, curr

        return curr