class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        ln = len(palindrome)

        if ln == 1:
            return ""

        l, r = 0, ln-1
        while l < r:
            if l != r and palindrome[l] != "a":
                return palindrome[:l] + "a" + palindrome[l+1:]
            l += 1
            r -= 1

        pidx = ln - 1
        return palindrome[:pidx] + "b"    