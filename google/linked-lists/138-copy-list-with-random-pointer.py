# Definition for a Node.
from typing import Optional


class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

class Solution:
    def copyRandomList(self, head: Optional[Node]) -> Optional[Node]:
        if head == None:
            return None

        nitr = new_head = Node(-1)
        itr = head
        node_mapping, idx = {}, 0
        while itr:
            nitr.next = Node(itr.val)
            node_mapping[itr] = nitr.next
            itr = itr.next 
            nitr = nitr.next
            idx += 1

        itr, nitr, idx = head, new_head.next, 0
        while itr:
            nitr.random = node_mapping[itr.random] if itr.random else None 
            itr = itr.next
            nitr = nitr.next

        return new_head.next 