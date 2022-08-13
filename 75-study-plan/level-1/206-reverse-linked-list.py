from typing import Optional

#Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None:
            return head

        p, n = head, head.next
        p.next = None

        while(n != None):
            head = n
            n = head.next
            head.next = p
            p = head

        return head
        

        