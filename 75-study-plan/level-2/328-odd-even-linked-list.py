# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
         
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        if head == None:
            return None

        oitr = odd_head = head
        eitr = even_head = odd_head.next

        if even_head == None:
            return head

        idx = 1
        itr = eitr.next
        while itr:

            if idx & 1 == 1:
                oitr.next = itr
                oitr = oitr.next
            else:
                eitr.next = itr
                eitr = eitr.next

            itr = itr.next
            idx += 1

        eitr.next = None
        oitr.next = even_head

        return odd_head

