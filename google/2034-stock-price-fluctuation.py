from heapq import heapify, heappop, heappush


class StockPrice:

    def __init__(self):
        self.timestamp_recorded = {}
        self.latest_timestamp = -1

        self.min_records = []
        self.max_records = []

        heapify(self.min_records)
        heapify(self.max_records)

    def update(self, timestamp: int, price: int) -> None:
        self.latest_timestamp = max(self.latest_timestamp, timestamp)
        self.timestamp_recorded[timestamp] = price
        heappush(self.min_records, (price, timestamp))
        heappush(self.max_records, (-price, timestamp))

    def current(self) -> int:
        return self.timestamp_recorded[self.latest_timestamp]

    def maximum(self) -> int:
        while (-1 * self.timestamp_recorded[self.max_records[0][1]]) != self.max_records[0][0] :
            heappop(self.max_records)

        return -1 * self.max_records[0][0]

    def minimum(self) -> int:
        while self.timestamp_recorded[self.min_records[0][1]] != self.min_records[0][0] :
            heappop(self.min_records)

        return self.min_records[0][0]