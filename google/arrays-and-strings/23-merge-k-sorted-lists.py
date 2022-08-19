# Definition for singly-linked list.
from collections import deque
from genericpath import exists
from heapq import heapify, heappop, heappush
from typing import List, Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        itr = merged_root = ListNode()
        queue = []
        heapify(queue)
        id = 0
        for item in lists:
            if item:
                heappush(queue, (item.val, id, item))
                id += 1

        while queue:
            value, _, node = heappop(queue)
            itr.next = ListNode(value)
            itr = itr.next
            node = node.next
            if node:
                heappush(queue, (node.val, id, node))
                id += 1

        return merged_root.next
