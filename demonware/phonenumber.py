# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

from collections import deque


def solution(S):

    digits = deque([])
    ln = 0

    for sch in S:
        if sch.isdigit():
            digits.append(sch)
            ln += 1

    n, r = divmod(ln, 3)

    if r != 0:
        if r != 2:
            r = 2
            n -= 1
        else:
            r = 1

    group = []
    for _ in range(n):
        g = ""
        for _ in range(3):
            g += digits.popleft()
        group.append(g)

    for _ in range(r):
        g = ""
        for _ in range(2):
            g += digits.popleft()
        group.append(g)

    return "-".join(group)