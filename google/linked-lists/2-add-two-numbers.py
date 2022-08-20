# Definition for singly-linked list.
from calendar import c
from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        itr1, itr2 = l1, l2
        result = ritr = ListNode()

        while itr1 or itr2:
            s = (itr1.val if itr1 else 0) + (itr2.val if itr2 else 0) + carry

            if s > 9:
                ritr.next = ListNode(s % 10)
                carry = s // 10
            else:
                ritr.next = ListNode(s)
                carry = 0

            itr1 = (itr1.next if itr1 else None)
            itr2 = (itr2.next if itr2 else None)
            ritr = ritr.next
        
        if carry > 0:
            ritr.next = ListNode(carry)

        return result.next

