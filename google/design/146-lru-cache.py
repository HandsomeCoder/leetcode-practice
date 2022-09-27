class Node:
    def __init__(self, data) -> None:
        self.prev = self.next = None
        self.data = data

class LRUCache:

    def __init__(self, capacity: int):
        self.head, self.tail = Node(None), Node(None)
        self.capacity = capacity
        self.length = 0
        self.mapping = {}

        self.head.next = self.tail
        self.tail.prev = self.head


    def __insert_left(self, node):
        node.next = self.head.next
        node.next.prev = node
        self.head.next = node
        node.prev = self.head

    def __remove(self, node):
        node.next.prev = node.prev
        node.prev.next = node.next
        node.next = node.prev = None

    def __pop_right(self):
        node = self.tail.prev
        self.__remove(node)
        return node


    def __move_to_head(self, node):
        if self.head.next == node:
            return

        self.__remove(node)
        self.__insert_left(node)

    def __clear_node(self, node):
        node.data = node.next = node.prev = None
        node = None

    def get(self, key: int) -> int:
        if key not in self.mapping:
            return -1

        self.__move_to_head(self.mapping[key])
        return self.mapping[key].data[1]

    def put(self, key: int, value: int) -> None:
        
        data = (key, value)

        if key in self.mapping:
            node = self.mapping[key]
            node.data = data
            self.__move_to_head(node)

        else: 
            node = Node(data)
            self.mapping[key] = node
            self.__insert_left(node)
            self.length += 1


            if self.length > self.capacity:
                node = self.__pop_right()
                self.mapping.pop(node.data[0])
                self.__clear_node(node)
                self.length -= 1