from typing import List


class Solution:
    def maximumEvenSplit(self, finalSum: int) -> List[int]:
        if finalSum & 1 == 1:
            return []

        itr = 2
        result = []
        while finalSum - itr > itr:
            result.append(itr)
            finalSum -= itr
            itr += 2

        if finalSum > 0:
            result.append(finalSum)

        return result