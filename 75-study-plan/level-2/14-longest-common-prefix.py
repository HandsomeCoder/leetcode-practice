from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        n = len(strs)
        if n == 0:
            return ""
        
        if n == 1:
            return strs[0]

        ln = min([len(s) for s in strs])
        prefix = []

        for i in range(ln):
            mch = strs[0][i]
            is_continue = True
            for word in strs:
                if mch != word[i]:
                    is_continue = False

            if not is_continue:
                break

            prefix.append(mch)

        return "".join(prefix)

print(Solution().longestCommonPrefix(["flower","flow","flight"]))