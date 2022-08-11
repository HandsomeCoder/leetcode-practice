
# Definition for a Node.
from collections import deque


class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

class Solution:
    def cloneGraph(self, node: Node) -> Node:

        if not node:
            return None

        mapping = {}
        visited = set()

        stack = deque([node])
        

        while stack:
            itr = stack.pop()
            idx = itr.val - 1

            if  idx in visited:
                continue

            visited.add(idx)

            if not mapping[idx]:
                mapping[idx] = Node(itr.val)

            clone_node = mapping[idx]
            for neigh in itr.neighbors:
                idx = neigh.val - 1
                if not mapping[idx]:
                    mapping[idx] = Node(neigh.val)

                clone_node.neighbors.append(mapping[idx])
                stack.append(neigh)
                

        return mapping[node.val - 1]

n1 = Node(1)
n2 = Node(2)
n3 = Node(3)
n4 = Node(4)

n1.neighbors = [n2, n4]
n2.neighbors = [n1, n3]
n3.neighbors = [n2, n4]
n4.neighbors = [n1, n3]

print(Solution().cloneGraph(n1))