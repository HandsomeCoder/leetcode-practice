from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        
        if head == None:
            return False

        if head.next == None:
            return True
        
        slow = fast = head
        while fast.next != None and fast.next.next != None:
            slow = slow.next
            fast = fast.next.next

        if not fast.next:
            slow = slow.next
        
        itr = head
        
        while slow:
            if itr.val != slow.val:
                return False

            itr = itr.next
            slow = slow.next

        return True