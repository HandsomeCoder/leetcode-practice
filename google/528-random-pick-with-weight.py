from bisect import bisect_left
from itertools import accumulate
from random import random
from typing import List


class Solution:

    def __init__(self, w: List[int]):
        self.w = list(accumulate(w))

    def pickIndex(self) -> int:
        value = random() * self.w[-1]
        return bisect_left(self.w, value)