from audioop import mul
from collections import deque


class Solution:
    def decodeString(self, s: str) -> str:
        
        def is_num(ch):
            return "0" <= ch <= "9"

        def is_alpha(ch):
            return "a" <= ch <= "z"

        def decode(idx, str):
            multiplier = ""
            decoded = ""

            while is_num(str[idx]):
                multiplier += str[idx]
                idx += 1

            idx += 1

            while str[idx] != "]":

                while is_alpha(str[idx]):
                    decoded += str[idx]
                    idx += 1

                if str[idx] != "]":
                    idx, lc_decoded = decode(idx, str)
                    decoded += lc_decoded

            return (idx + 1, decoded * int(multiplier))
                
    
        idx, decoded = decode(0, "1["+s+"]")
        return decoded + s[idx:]

print(Solution().decodeString("3[a]2[bc]"))
print(Solution().decodeString("2[b]abd"))
print(Solution().decodeString("2[b2[a]3[4[d]]]3[a]"))


