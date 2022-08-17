from collections import deque
from math import ceil, floor
from typing import List


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = deque([tokens[-1]])

        def truncate(x):
            return floor(x) if x > 0 else ceil(x)

        operators = {
            "+": lambda x, y: x + y,
            "-": lambda x, y: x - y,
            "*": lambda x, y: x * y,
            "/": lambda x, y: truncate(x / y)
        }

        for token in tokens[-2::-1]:

            if token in operators:
                stack.append(token)

            elif stack[-1] not in operators:
                token = int(token)

                while stack and stack[-1] not in operators:
                    right, operation = stack.pop(), stack.pop()
                    token = operators[operation](token, right)

                stack.append(token)
            else:
                stack.append(int(token))

        return stack.pop()


print(Solution().evalRPN(["10", "6", "9", "3", "+",
      "-11", "*", "/", "*", "17", "+", "5", "+"]))
