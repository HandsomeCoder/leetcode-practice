
class Solution:
    def multiply(self, num1: str, num2: str) -> str:
 
        if num1 == "0" or num2 == "0":
            return "0"
        elif num1 == "1":
            return num2
        elif num2 == "1":
            return num1
        

        l1, l2 = len(num1), len(num2)

        num1, num2 = num1[::-1], num2[::-1]
        result = [0] * (l1 + l2)
        
        for j, n2 in enumerate(num2):
            for i, n1 in enumerate(num1):
                x, y = int(n1), int(n2)

                mul = (x * y) + result[i+j]
                buffer = mul % 10
                carry = mul // 10

                result[i+j] = buffer 
                result[i+j+1] += carry

        while result[-1] == 0:
            result.pop()

        return "".join(map(str, result[::-1]))
