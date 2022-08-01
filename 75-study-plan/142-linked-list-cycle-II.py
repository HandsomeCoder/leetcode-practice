from cmath import sin
from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        single = double = head
        while double and double.next:
            single = single.next
            double = double.next.next

            if(single == double):
                target = head
            
                while(target != single):
                    target = target.next
                    single = single.next
                
                return target
    
        return None

print(Solution().detectCycle(ListNode(1)))