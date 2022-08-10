from typing import List

class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:

        mapping = {}

        def find(node):
            if node not in mapping:
                mapping[node] = (node, 1)

            nroot, weight = mapping[node]

            if nroot != node:
                mroot, tweight = find(nroot)
                mapping[node] = (mroot, weight * tweight)

            return mapping[node]

        def union(x, y, weight):
            xroot, xweight = find(x)
            yroot, yweight = find(y)

            if xroot != yroot:
                mapping[xroot] = (yroot, yweight * weight / xweight)

        for (x, y), weight in zip(equations, values):
            union(x, y, weight)

        result = []
        for x, y in queries:
            if x in mapping and y in mapping:
                if x == y:
                    result.append(1.0)
                else:
                    xroot, xweight = find(x)
                    yroot, yweight = find(y)

                    if xroot == yroot:
                        result.append(round(xweight / yweight, 6))
                    else:
                        result.append(-1.0)
            else:
                result.append(-1.0)

        return result