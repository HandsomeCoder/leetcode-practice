from collections import deque


class Solution:
    def racecar(self, target: int) -> int:

        queue = deque([(0, 0, 1)])

        visited = set()
        while queue:
            moves, pos, speed = queue.popleft()

            if pos == target:
                return moves
            
            key = (pos, speed)
            if key in visited:
                continue

            next_pos = pos + speed
            queue.append((moves + 1, next_pos, speed * 2))

            if (next_pos > target and speed > 0) or (next_pos < target and speed < 0):
                speed = -1 if speed > 0 else 1
                queue.append((moves + 1, pos, speed))