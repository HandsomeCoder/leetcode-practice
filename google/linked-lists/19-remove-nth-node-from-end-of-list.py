# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:        
        pln = ln = 0 
        prev = itr = head
        while itr:
            if ln - pln > n:
                prev = prev.next
                pln += 1

            itr = itr.next
            ln += 1

        if ln == n :
            if ln == 1:
                return None
            else:
                prev = prev.next
                head.next = None
                head = prev
        elif n == 1:
            prev.next = None
        else:
            temp = prev.next.next
            prev.next.next = None
            prev.next = temp
        
        return head




