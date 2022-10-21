# Definition for a binary tree node.
from collections import deque
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class BSTIterator:

    def __read_all_left__(self, itr):
        while itr:
            self.stack.append(itr)
            itr = itr.left

    def __init__(self, root: Optional[TreeNode]):
        self.stack = deque([])
        self.__read_all_left__(root)

    def next(self) -> int:
        itr = self.stack.pop()
        self.__read_all_left__(itr.right)
        return itr.val

    def hasNext(self) -> bool:
        return len(self.stack) > 0


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()