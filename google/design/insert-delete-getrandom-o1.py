

from random import randint


class RandomizedSet:

    def __init__(self):
        self.data = {}
        self.arr = []
        self.top = -1

    def insert(self, val: int) -> bool:
        if val in self.data:
            return False

        self.top += 1
        self.data[val] = self.top

        if len(self.arr) == self.top:
            self.arr.append(val)
        else:
            self.arr[self.top] = val
        
        return True


    def remove(self, val: int) -> bool:
        if val not in self.data:
            return False

        idx = self.data.pop(val)
        
        if idx < self.top:
            last = self.arr[self.top]
            self.arr[idx] = last
            self.data[last] = idx

        self.top -= 1
        return True

    def getRandom(self) -> int:
        return self.arr[randint(0, self.top)]


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()