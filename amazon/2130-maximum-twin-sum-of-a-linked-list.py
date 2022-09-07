# Definition for singly-linked list.
from collections import deque
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        slow = fast = head
        pair = deque()
        while fast:
            pair.append(slow.val)
            slow = slow.next
            fast = fast.next.next

        max_pair = -1
        while slow:
            max_pair = max(max_pair, slow.val + pair.pop())
            slow = slow.next

        return max_pair