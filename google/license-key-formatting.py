from collections import deque


class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        s = s.upper()[::-1]
        result = []
        buffer = []
        for sch in s:
            if sch == "-":
                continue
            
            buffer.append(sch)

            if len(buffer) == k:
                result.append("".join(buffer[::-1]))
                buffer = []

        if buffer:
            result.append("".join(buffer[::-1]))

        return "-".join(result[::-1])
        
print(Solution().licenseKeyFormatting("5F3Z-2e-9-w", 4))