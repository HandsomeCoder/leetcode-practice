from typing import List


class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        s = list(s)
        n = len(s)
        roots = [i for i in range(n)]
        ranks = [1 for _ in range(n)]

        mapping = {i: [i] for i in range(n)}
        def find(x):
            if x != roots[x]:
                roots[x] = find(roots[x])
            
            return roots[x]

        def union(x, y):
            xroot = find(x)
            yroot = find(y)

            if xroot != yroot:
                key, value = xroot, yroot 
                if ranks[xroot] == ranks[yroot]:
                    roots[yroot] = xroot
                    ranks[xroot] += 1
                elif ranks[xroot] > ranks[yroot]:
                    roots[yroot] = xroot
                else:
                    roots[xroot] = yroot
                    key, value = yroot, xroot

                mapping[key].extend(mapping[value])
                mapping.pop(value)

                return True

            return False

        n_connected_graph = n
        for x, y in pairs:
            if union(x, y):
                n_connected_graph -= 1
                if n_connected_graph == 1:
                    return "".join(sorted(s))
        
        for _, idxs in mapping.items():
            values = [s[i] for i in idxs]
            
            idxs.sort()
            values.sort()
            
            for idx, value in zip(idxs, values):
                s[idx] = value
        
        return "".join(s)

print(Solution().smallestStringWithSwaps("dcab", [[0,3],[1,2],[0,2]]))
print(Solution().smallestStringWithSwaps("dcab", [[0,3],[1,2]]))
print(Solution().smallestStringWithSwaps("cba", [[0,1],[1,2]]))
print(Solution().smallestStringWithSwaps("udyyek", [[3,3],[3,0],[5,1],[3,1],[3,4],[3,5]]))