from typing import List


class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        root = [i for i in range(n)]
        rank = [1 for _ in range(n)]

        n_connected_tree = n
        def find(i):
            if i == root[i]:
                return i
            
            root[i] = find(root[i])
            return root[i]

        def union(i,j):
            ri = find(i)
            rj = find(j)  

            if ri == rj:
                return False

            if rank[ri] == rank[rj]:
                root[rj] = ri
                rank[ri] += 1
            elif rank[ri] > rank[rj]:
                root[rj] = ri
            else:
                root[ri] = rj
            
            return True
        

        
        for i, j in edges:
            if union(i, j):
                n_connected_tree -= 1
            else: return False
        
        return n_connected_tree == 1