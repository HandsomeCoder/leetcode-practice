def solution(A, B, C, D):
    def is_valid(arr):
        a, b, c, d = arr
        h, m = a * 10 + b, c * 10 + d
        return 1 if 0 <= h < 24 and 0 <= m < 60 else 0

    def get_permutation(arr, i, result, visited):
        if i == 4:
            node = tuple(arr)
            if node not in visited:
                result.append(result[-1] + is_valid(arr))
                visited.add(node)

        for j in range(i, 4):
            arr[i], arr[j] = arr[j], arr[i]
            get_permutation(arr, i+1, result, visited)
            arr[i], arr[j] = arr[j], arr[i]

    digits = [A, B, C, D]
    result = [0]
    get_permutation(digits, 0, result, set())
    return result[-1]