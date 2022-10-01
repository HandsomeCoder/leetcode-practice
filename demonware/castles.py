# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    ln = len(A)
    l = 0
    dA = [A[0]]
    while l < ln:
        if dA[-1] != A[l]:
            dA.append(A[l])    
        l += 1
            
    if len(dA) == 1:
        return 1

    cnt = 2
    ln = len(dA)
    for itr in range(1, ln-1):
        if dA[itr-1] > dA[itr] < dA[itr+1] or dA[itr-1] < dA[itr] > dA[itr+1]:
            cnt += 1

    return cnt


print(solution([2, 2, 5, 6, 3, 3]))
