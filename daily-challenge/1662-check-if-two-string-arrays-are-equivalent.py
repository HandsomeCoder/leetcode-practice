from typing import List


class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:

        word2.append(["#"])
        widx = cidx = 0
        wln, ln = len(word2), len(word2[widx])

        for word in word1:
            for wch in word:
                if wch != word2[widx][cidx]:
                    return False

                cidx += 1
                if cidx == ln:
                    cidx, widx = 0, widx + 1
                    if widx == wln:
                        widx -= 1
                    ln = len(word2[widx])

        return word2[widx][cidx] == "#"