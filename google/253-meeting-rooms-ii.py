from typing import List


class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        start_time  = sorted(list(map(lambda x: x[0], intervals)))
        end_time = sorted(list(map(lambda x: x[1], intervals)))
        ln = len(intervals)

        s_idx = e_idx = rooms = 0
        while s_idx < ln:
            if end_time[e_idx] <= start_time[s_idx]:
                e_idx += 1
            else:
                rooms += 1
            s_idx += 1

        return rooms