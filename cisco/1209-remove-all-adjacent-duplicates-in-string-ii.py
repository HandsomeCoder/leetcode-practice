from collections import deque


class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        sln = len(s)
        if sln == 1:
            return s

        s = list(s)
        s.append("#")
        sln += 1

        stack = deque([])
        itr, cnt = s[0], 1

        for idx in range(1, sln):
            if itr == s[idx]:
                cnt += 1
                continue

            if stack and stack[-1][0] == itr:
                cnt += stack.pop()[1]

            r = cnt % k
            if r > 0:
                stack.append((itr, r))

            itr, cnt = s[idx], 1

        result = []
        while stack:
            seg, cnt = stack.pop()
            result.append(seg * cnt)

        return "".join(result[::-1])