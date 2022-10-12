# Definition for singly-linked list.
from collections import deque
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        def merge_list(l, r):
            head = x = ListNode(None)

            while l and r:
                if l.val <= r.val:
                    x.next = l
                    l = l.next
                else:
                    x.next = r
                    r = r.next
                x = x.next

            remain = l if r == None else r

            while remain:
                x.next = remain
                remain = remain.next
                x = x.next

            return head.next



        nodes = deque([])
        itr = head
        while itr:
            nodes.append(itr)
            nodes[-1].next = None
            itr = itr.next


        while nodes:
            l = nodes.popleft()

            if not nodes:
                return l

            r = nodes.popleft()
            nodes.append(merge_list(l, r))




        
