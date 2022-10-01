from collections import Counter


def solution(S, L):
    s_counter = Counter(S)
    max_value = 0
    for l in L:
        counter = Counter(l)
        min_value = len(S)
        for key, value in counter.items():
            min_value =  min(min_value, s_counter.get(key, 0) // value)
        max_value = max(max_value, min_value)
    return max_value