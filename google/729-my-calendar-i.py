class Node:
    def __init__(self, val) -> None:
        self.val = val
        self.left = self.right = None


class MyCalendar:

    def __init__(self):
        self.bookings = None

    def book(self, start: int, end: int) -> bool:

        event = (start, end)

        if not self.bookings:
            self.bookings = Node(event)
            return True

        itr = self.bookings
        while itr:
            booking_starts, booking_ends = itr.val
            if booking_ends <= start:
                if itr.right:
                    itr = itr.right
                else:
                    itr.right = Node(event)
                    return True
            elif booking_starts >= end:
                if itr.left:
                    itr = itr.left
                else:
                    itr.left = Node(event)
                    return True
            else:
                return False