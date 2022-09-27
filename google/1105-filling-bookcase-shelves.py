from typing import List


class Solution:
    def minHeightShelves(self, books: List[List[int]], shelfWidth: int) -> int:
        bln = len(books)
        shelves = [0 for _ in range(bln+1)]

        for idx in range(bln):
            cw, ch = books[idx]
            shelves[idx] = shelves[idx-1] + ch

            rw, rh, pi = cw, ch, idx - 1
            while pi >= 0 and books[pi][0] + rw <= shelfWidth:
                pw, ph = books[pi]
                rh = max(rh, ph)
                rw += pw
                
                shelves[idx] = min(shelves[idx], rh + shelves[pi-1])
                pi -= 1

        return shelves[bln-1]