from operator import le
from typing import List


class Solution:
    def maximumWhiteTiles(self, tiles: List[List[int]], carpetLen: int) -> int:
        def get_len(tite):
            x, y = tite
            return y + 1 - x

        def calc_empty_space(pair1, pair2):
            return pair2[0] - pair1[1] - 1

        def is_even(x):
            return x & 1 == 0

        tiles.sort()
        tln = len(tiles)
        length = [get_len(tiles[0])]

        for idx in range(1, tln):
            prev, curr = tiles[idx-1], tiles[idx]
            
            length.append(calc_empty_space(prev, curr))
            itr = get_len(curr)
            if itr >= carpetLen:
                return carpetLen
            
            length.append(itr)

        max_cover = l = r = 0
        limit, ln, cover = carpetLen, len(length), 0
        while r < ln:
            itr = length[r]
            if itr <= limit:
                limit -= itr
                if is_even(r):
                    cover += itr
                r += 1
            else:
                max_cover = max(max_cover, cover + (limit if is_even(r) else 0))
                limit += length[l]
                if is_even(l):
                    cover -= length[l]
                l += 1

        return max(max_cover, cover)