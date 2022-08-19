from collections import deque
from inspect import stack
from turtle import st


class Solution:
    def isValid(self, s: str) -> bool:
        stack = deque([])
        brackets = {"(": ")", "{": "}", "[": "]"}
        for sch in s:
            if sch in brackets:
                stack.append(sch)
            elif stack and sch == brackets[stack[-1]]:
                stack.pop()
            else:
                return False

        return True if len(stack) == 0 else False
