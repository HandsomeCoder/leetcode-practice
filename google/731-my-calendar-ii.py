from bisect import insort
from collections import defaultdict


class MyCalendarTwo:
    def __init__(self):
        self.schedule = defaultdict(lambda: 0)
        self.order = []

    def book(self, start: int, end: int) -> bool:

        if start not in self.schedule:
            insort(self.order, start)

        if end not in self.schedule:
            insort(self.order, end)

        self.schedule[start] += 1
        self.schedule[end] -= 1

        booking = 0
        for idx in self.order:
            booking += self.schedule[idx]
            if booking == 3:
                self.schedule[start] -= 1
                self.schedule[end] += 1
                return False

        return True


myCalendarTwo = MyCalendarTwo()
bookings = [(10, 20), (50, 60), (10, 40), (5, 15), (5, 10), (25, 55)]
for s, e in bookings:
    print(myCalendarTwo.book(s, e))
