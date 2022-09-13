from typing import List


class Solution:
    def wordCount(self, startWords: List[str], targetWords: List[str]) -> int:
        sortedWords = set()
        for start in map(sorted, startWords):
            sortedWords.add("".join(start))

        cnt = 0
        for target in targetWords:
            tln = len(target)
            if tln == 1:
                continue

            target = sorted(target)
            for i in range(tln):
                mod_target = "".join(target[:i] + target[i+1:])
                if mod_target in sortedWords:
                    cnt += 1
                    break

        return cnt