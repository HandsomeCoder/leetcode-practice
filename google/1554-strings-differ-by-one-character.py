from typing import List


class Solution:
    def differByOne(self, dict: List[str]) -> bool:
        dl = len(dict)
        wln = len(dict[0])
        replace_char = [set() for _ in range(wln)]
        words = set(dict)
        for idx in range(dl):
            word = dict[idx]
            for wi in range(wln):
                for rch in replace_char[wi]:
                    if rch == word[wi]:
                        continue

                    if word[:wi]+rch+word[wi+1:] in words:
                        return True

                replace_char[wi].add(word[wi])
        return False      