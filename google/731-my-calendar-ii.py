from sortedcontainers import SortedDict


class MyCalendarTwo:
    def __init__(self):
        self.schedule = SortedDict()
        self.order = []

    def book(self, start: int, end: int) -> bool:

        if start not in self.schedule:
            self.schedule[start] = 0

        if end not in self.schedule:
            self.schedule[end] = 0

        self.schedule[start] += 1
        self.schedule[end] -= 1

        booking = 0
        for event in self.schedule.values():
            booking += event
            if booking == 3:
                self.schedule[start] -= 1
                self.schedule[end] += 1
                return False

        return True