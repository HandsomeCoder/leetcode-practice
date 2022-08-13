from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        lR, uR, lC, uC = 0, len(matrix) - 1, 0, len(matrix[0]) - 1
        x, y = 0, 0

        def process_matrix_side(matrix, x, y, lower, upper, step, direction):
            buffer = []
            while True:
                buffer.append(matrix[x][y])
                if direction:
                    if lower <= x + step <= upper:
                        x += step
                    else:
                        break
                else:
                    if lower <= y + step <= upper:
                        y += step
                    else:
                        break
            return (buffer, x if direction else y)

        result = []
        while True:
            buffer, y = process_matrix_side(matrix, x, y, lC, uC, 1, False)
            result.extend(buffer)
            lR += 1
            x += 1
            if lR > uR or lC > uC:
                break

            buffer, x = process_matrix_side(matrix, x, y, lR, uR, 1, True)
            result.extend(buffer)
            uC -= 1
            y -= 1
            if lR > uR or lC > uC:
                break

            buffer, y = process_matrix_side(matrix, x, y, lC, uC, -1, False)
            result.extend(buffer)
            uR -= 1
            x -= 1
            if lR > uR or lC > uC:
                break

            buffer, x = process_matrix_side(matrix, x, y, lR, uR, -1, True)
            result.extend(buffer)
            lC += 1
            y += 1
            if lR > uR or lC > uC:
                break

        return result


print(Solution().spiralOrder([[1]]))
print(Solution().spiralOrder([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
print(Solution().spiralOrder([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]))
print(Solution().spiralOrder(
    [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15], [16, 17, 18, 19, 20], [21, 22, 23, 24, 25]]))
