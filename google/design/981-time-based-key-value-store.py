from collections import defaultdict
from math import ceil

class TimeMap:

    def __init__(self):
        self.timemap = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.timemap:
            self.timemap[key] = defaultdict(lambda: "")
            self.timemap["#"+key] = []
        
        self.timemap[key][timestamp] = value
        self.timemap["#"+key].append(timestamp)

    def __get_closest_timestamp(self, times, target):
        l, r = 0, len(times) - 1
        while l < r:
            m = ceil((l + r) / 2)
            if times[m] == target:
                l = m
                break
            elif times[m] <= target:
                l = m
            else:
                r = m - 1
        return times[l]

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.timemap:
            return ""

        if timestamp in self.timemap[key]:
            return self.timemap[key][timestamp] 

        c_timestamp = min(timestamp, self.__get_closest_timestamp(self.timemap["#"+key], timestamp))
        return self.timemap[key][c_timestamp]


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)