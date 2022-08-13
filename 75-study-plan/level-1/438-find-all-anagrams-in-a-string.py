from typing import List


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        mapping = [0 for _ in range(26)]
        window = [0 for _ in range(26)]

        def convert(ch):
            return ord(ch) - 97

        ln = len(p)
        for pch in p:
            mapping[convert(pch)] += 1

        i = j = 0
        match = 0
        result = []
        sln = len(s)
        while(j < sln):

            if j - i == ln: 
                itr_i = convert(s[i])
                if window[itr_i] > 0:
                    window[itr_i] -= 1
                    if window[itr_i] < mapping[itr_i]:
                        match -= 1 
                i += 1               

            itr_j = convert(s[j])
            if mapping[itr_j] != 0:
                window[itr_j] += 1
                if window[itr_j] <= mapping[itr_j]:
                    match += 1

            if match == ln:
                result.append(i)

            j += 1

        return result

print(Solution().findAnagrams("ababababab", "aab"))
print(Solution().findAnagrams("baa", "aa"))
print(Solution().findAnagrams("cbaebabacd", "abc"))


        