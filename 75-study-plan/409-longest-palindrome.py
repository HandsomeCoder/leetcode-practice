from collections import Counter

class Solution:
    def longestPalindrome(self, s: str) -> int:
        length = 0
        result = 0
        for value in Counter(s).values():
            length += value
            if value | 1 > value:
                result += value
            else:
                result += value - 1

        return result + 1 if result < length else result
            
