class Solution:
    def longestValidParentheses(self, s: str) -> int:
        sln = len(s)
        max_len = 0
        open_one = close_one = open_two = close_two = 0
        for idx in range(sln):
            if s[idx] == "(":
                open_one += 1
            else:
                close_one += 1

            if open_one == close_one:
                max_len = max(max_len, open_one + close_one)
            elif close_one > open_one:
                open_one = close_one = 0

            if s[sln-1-idx] == "(":
                open_two += 1
            else:
                close_two += 1

            if open_two == close_two:
                max_len = max(max_len, open_two + close_two)
            elif close_two < open_two:
                open_two = close_two = 0

        return max_len