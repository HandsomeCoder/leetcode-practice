# Definition for a Node.
from collections import deque
from typing import Optional


class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

class Solution:
    def connect(self, root: 'Optional[ Node]') -> 'Optional[Node]':

        if root is None:
            return None
        
        queue = deque([root])

        while queue:
            
            next_queue = deque([])
            left = None

            while True:
                if not queue:
                    break

                if not left:
                    left = queue.popleft()
                else:
                    right = queue.popleft()
                    left.next = right
                    left = right
                    
                if left.left:
                    next_queue.append(left.left)
                    next_queue.append(left.right)

            queue = next_queue

        return root

            


