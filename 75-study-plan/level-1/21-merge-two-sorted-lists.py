from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:

    def insertAfter(self, node1: ListNode, node2: ListNode):
        temp = node1.next
        node1.next = node2
        node2.next = temp
            

    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        head1 = list1
        head2 = list2

        if head1 == None:
            return head2
        elif head2 == None:
            return head1


        if head1.val > head2.val:
            itr = head2
            head2 = head2.next
            itr.next = head1
            head1 = itr

        itr = head1
        while(head2 != None):

            if(itr.next == None):
                itr.next = head2
                break
    
            node = head2

            if (itr.val <= node.val) and (itr.next != None and node.val <= itr.next.val):
                head2 = head2.next
                self.insertAfter(itr, node)

            itr = itr.next
        
        return head1 
