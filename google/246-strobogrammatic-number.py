class Solution:
    def isStrobogrammatic(self, num: str) -> bool:
        pair = {"0": "0", "1": "1", "8": "8", "6": "9", "9": "6"}

        l, r = 0, len(num) - 1

        while (l <= r):
            itr = num[l]

            if (itr not in pair) or (pair[itr] != num[r]):
                return False

            l += 1
            r -= 1

        return True
