# Euler Circuit

class Solution:
    def crackSafe(self, n: int, k: int) -> str:
        def explore(result, visited, path, k):
            for i in range(k):
                i = str(i)
                s = path + i
                if s in visited:
                    continue

                visited.add(s)
                explore(result, visited, s[1:], k)
                result.append(i)

        path = "0" * (n-1)
        result = []
        visited = set([path])
        explore(result, visited, path, k)
        result.append(path)
        return ''.join(map(str, result[::-1]))

print(Solution().crackSafe(3, 2))
        

