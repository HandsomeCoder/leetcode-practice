from collections import defaultdict
from email.policy import default


class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        pair = defaultdict(lambda: 0)
        left = pair_count = 0
        max_length = -1

        for idx, sch in enumerate(s):
            if sch in pair:
                pair[sch] = idx
                continue

            if pair_count == 2:
                max_length = max(idx - left, max_length)
                rch, prev = "", s[idx-1]
                for pch, pidx in pair.items():
                    if pch == prev:
                        continue
                    left = pidx + 1
                    rch = pch

                pair.pop(rch)
            else:
                pair_count += 1

            pair[sch] = idx

        max_length = max(len(s) - left, max_length)
        return max_length


print(Solution().lengthOfLongestSubstringTwoDistinct("eceba"))
print(Solution().lengthOfLongestSubstringTwoDistinct("ccaabbb"))



