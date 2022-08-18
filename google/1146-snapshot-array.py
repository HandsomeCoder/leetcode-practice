from bisect import bisect_left
from collections import defaultdict
from math import ceil, floor


class SnapshotArray:
    def __init__(self, length: int):
        self.current = {}
        self.snaphots = []
        self.snap_id = -1
        self.history = defaultdict(list)
        self.curr_dirty_idx = set()

    def set(self, index: int, val: int) -> None:
        self.current[index] = val
        self.curr_dirty_idx.add(index)

    def snap(self) -> int:
        self.snap_id += 1
        snap = {}
        for idx in self.curr_dirty_idx:
            snap[idx] = self.current[idx]
            self.history[idx].append(self.snap_id)
            
        self.snaphots.append(snap)
        self.curr_dirty_idx = set()
        return self.snap_id

    def get(self, index: int, snap_id: int) -> int:
        hln = len(self.history[index])

        if hln == 0:
            return 0

        l, r = 0, hln - 1
        while (l < r):
            m = ceil((l+r) / 2)
            if self.history[index][m] <= snap_id:
                l = m
            else:
                r = m-1
        last_snap_id = self.history[index][l]
        if last_snap_id > snap_id:
            return 0

 
        return self.snaphots[last_snap_id][index]


# Your SnapshotArray object will be instantiated and called as such:
# obj = SnapshotArray(length)
# obj.set(index,val)
# param_2 = obj.snap()
# param_3 = obj.get(index,snap_id)
