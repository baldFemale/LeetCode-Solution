import heapq


class Solution(object):
    def kthSmallestPrimeFraction(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: List[int]
        """
        A = A
        reverse_A = A[::-1]

        heap = []
        for i in range(len(A) - 1):
            heap.append((1.0 * A[0] / reverse_A[i], i, 0))

        heapq.heapify(heap)

        while K > 0:
            K -= 1
            v, i, j = heapq.heappop(heap)
            if j < len(A) - i - 2:
                heapq.heappush(heap, (1.0 * A[j + 1] / reverse_A[i], i, j + 1))
            else:
                heapq.heappush(heap, (float("inf"), i, j + 1))

        return [A[j], reverse_A[i]]
