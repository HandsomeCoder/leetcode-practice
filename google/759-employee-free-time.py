from typing import List


class Interval:
    def __init__(self, start: int = None, end: int = None):
        self.start = start
        self.end = end


class Solution:
    def employeeFreeTime(self, schedule: List[List[Interval]]) -> List[Interval]:

        slots = []
        for employee in schedule:
            for slot in employee:
                slots.append((slot.start, slot.end))

        slots.sort() 
        ln = len(slots)
        booked_slots = [slots[0]]
        free_time_slots = []
        for idx in range(1, ln):
            s, e = slots[idx]
            x, y = booked_slots[-1]
            
            if x <= s <= y:
                booked_slots[-1] = (min(s, x), max(e, y))
            else:
                booked_slots.append((s, e))
                if s - y > 0:
                    free_time_slots.append(Interval(y, s))

        return free_time_slots


print(Solution().employeeFreeTime(
    [[Interval(1, 2), Interval(5, 6)], [Interval(1, 3)], [Interval(4, 10)]]))
