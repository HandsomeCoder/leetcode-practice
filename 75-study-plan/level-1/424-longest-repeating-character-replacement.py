from collections import Counter

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        ln = len(s)

        if ln == 1:
            return ln

        mapping = {}
        start = 0
        for idx, sch in enumerate(s):
            pch = s[start]
            if pch == sch:
                continue

            if pch not in mapping:
                mapping[pch] = [(0, start, idx - 1)]
            else:
                cost  = start - mapping[pch][-1][2] - 1
                mapping[pch].append((cost, start, idx - 1))

            start = idx

        pch = s[start]
        if pch not in mapping:
            mapping[pch] = [(0, start, ln - 1)]
        else:
            cost  = start - mapping[pch][-1][2] - 1
            mapping[pch].append((cost, start, ln - 1))

        max_ln = k
        for _, values in mapping.items():
            buffer = k
            i = j = 0
            vln = len(values)

            while(j < vln):

                left = values[i]
                right = values[j]

                diff = right[0]
                if diff <= buffer:
                    buffer -= diff
                    max_ln = max(max_ln, right[2] - left[1] + 1 + buffer)
                    j += 1
                else:
                    i += 1
                    left = values[i]
                    buffer += left[0]

            max_ln = min(max_ln, ln)
            if max_ln == ln:
                break

        return max_ln

print(Solution().characterReplacement("ABAB", 2))
print(Solution().characterReplacement("AABABBA", 1))