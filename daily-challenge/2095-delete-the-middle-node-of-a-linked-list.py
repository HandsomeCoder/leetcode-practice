# Definition for singly-linked list.
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head.next == None:
            return None

        if head.next.next == None:
            head.next = None
            return head

        slow = fast = head

        while fast.next:
            slow = slow.next
            fast = fast.next.next

        
        slow.val = slow.next.val
        temp = slow.next
        slow.next = slow.next.next

        temp.val = temp.next = None
        temp = None
        return head