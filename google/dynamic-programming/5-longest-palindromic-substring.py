class Solution:
    def longestPalindrome(self, s: str) -> str:

        def explore_palindrome(s, sln, l, r):
            while l >= 0 and r < sln and s[l] == s[r]:
                l -= 1
                r += 1

            return (r - l - 1, l + 1, r - 1)

        sl = len(s)

        max_length = 1
        idxes = (0, 0)
        for idx in range(sl):
            ln, l, r = explore_palindrome(s, sl, idx, idx)
            if ln > max_length:
                max_length, idxes = ln, (l, r)

            explore_palindrome(s, sl, idx, idx+1)
            if ln > max_length:
                max_length, idxes = ln, (l, r)

        return s[idxes[0]:idxes[1]+1]


print(Solution().longestPalindrome("aacabdkacaa"))
