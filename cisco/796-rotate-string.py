class Solution:
    def rotateString(self, s: str, goal: str) -> bool:

        sln, gln = len(s), len(goal)

        if sln != gln:
            return False

        lps = [0] * gln
        prev, curr = 0, 1

        while curr < gln:
            if goal[curr] == goal[prev]:
                prev += 1
                lps[curr] = prev
                curr += 1
            elif prev == 0:
                lps[curr] = 0
                curr += 1
            else:
                prev = lps[prev - 1]

        src = s + s
        sln = len(src)
        i = j = 0

        while i < sln:
            if src[i] == goal[j]:
                i += 1
                j += 1
            elif j == 0:
                i += 1
            else:
                j = lps[j-1]

            if j == gln:
                return True

        return False