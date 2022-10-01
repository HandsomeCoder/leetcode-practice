from collections import Counter


def solution(A):
    counter = Counter(A)
    op = 0
    for key, value in counter.items():
        diff = abs(value - key)
        op += min(diff, value)
    return op