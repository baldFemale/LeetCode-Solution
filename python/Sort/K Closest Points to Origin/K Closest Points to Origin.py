class Solution(object):
    def kClosest(self, points, K):
        """
        :type points: List[List[int]]
        :type K: int
        :rtype: List[List[int]]
        """

        # understanding quick-sort,heap & sort

        def compare(x, y):
            return x[0] * x[0] + x[1] * x[1] - y[0] * y[0] - y[1] * y[1]

        def partition(l, r):
            pivot = points[l]
            while l < r:
                while l < r and compare(points[r], pivot) >= 0:
                    r -= 1
                points[l] = points[r]

                while l < r and compare(points[l], pivot) < 0:
                    l += 1
                points[r] = points[l]
            points[l] = pivot
            return l

        l = 0
        r = len(points) - 1

        while l < r:
            middle = partition(l, r)
            if middle == K:
                break
            else:
                if middle > K:
                    r = middle - 1
                else:
                    l = middle + 1
        return points[:K]




