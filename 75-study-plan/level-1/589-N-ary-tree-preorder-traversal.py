from typing import List

# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution:
    def preorder(self, root: Node) -> List[int]:
        
        if root == None:
            return []

        result = []
        stack = [root]

        while stack:
            itr = stack.pop()
            result.append(itr.val)

            if itr.children:
                itr.children.reverse()
                stack.extend(itr.children)

        return result
