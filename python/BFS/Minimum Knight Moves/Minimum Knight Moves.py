from collections import deque


class Solution(object):
    def minKnightMoves(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        x = abs(x)
        y = abs(y)

        q = deque()
        seen = set()

        q.append((0, 0, 0))

        while q:
            for i in range(len(q)):
                xx, yy, c = q.popleft()
                if xx == x and yy == y:
                    return c
                if (xx, yy) in seen:
                    continue
                seen.add((xx, yy))

                for dx, dy in [[1, 2], [1, -2], [2, 1], [2, -1], [-1, 2], [-1, -2], [-2, 1], [-2, -1]]:
                    if -2 < dx + xx <= x and -2 < dy + yy <= y:
                        q.append((dx + xx, dy + yy, c + 1))
