class Node:
    def __init__(self, val) -> None:
        self.next = None
        self.prev = None
        self.val = val


class LRUCache:

    def __init__(self, capacity: int):
        self.head = self.tail = Node(None)
        self.limit = capacity
        self.length = 0
        self.mapping = {}

    def increase_priority(self, curr):
        if curr == self.tail:
            return

        self.tail.next = curr.next
        curr.next.prev = self.tail

        curr.next = self.tail.prev
        curr.prev.next = self.tail
        self.tail.prev = curr.prev 
        
        curr.prev = curr.next
        curr.prev.next = curr



    def get(self, key: int) -> int:
        if key not in self.mapping:
            return -1

        self.increase_priority(self.mapping[key])
        return self.mapping[key].val[1]

    def put(self, key: int, value: int) -> None:
        
        if key in self.mapping:
            node = self.mapping[key]
            node.val = (key, value)
            self.increase_priority(node)

        else:        
            if self.length == self.limit:
                top = self.head.next
                self.mapping.pop(top.val[0])
                self.head.next = top.next
                top.next.prev = self.head

                top.val = top.prev = top.next = None
                top = None

                self.length -= 1

            self.mapping[key] = node = Node((key, value))
            self.tail.next = node
            node.prev = self.tail
            self.tail = self.tail.next
            self.length += 1


lRUCache = LRUCache(2)
lRUCache.put(1, 1)
lRUCache.put(2, 2)
lRUCache.get(1)
lRUCache.put(3, 3)
lRUCache.get(2)
lRUCache.put(4, 4)
lRUCache.get(1)
lRUCache.get(3)
lRUCache.get(4)