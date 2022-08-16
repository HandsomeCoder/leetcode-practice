from cgitb import reset
from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        ln = len(digits)
        idx = ln-1 
        carry = 1
        while carry > -1:
            if idx == -1:
                idx = 0
                digits = [0] + digits 

            total = digits[idx] + carry

            carry  = -1
            if total > 9:
                carry = 1
                digits[idx] = total - 10
            else:
                digits[idx] = total

            idx -= 1

        return digits