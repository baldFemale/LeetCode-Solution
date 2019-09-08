class Solution(object):
    def distanceBetweenBusStops(self, distance, start, destination):
        """
        :type distance: List[int]
        :type start: int
        :type destination: int
        :rtype: int
        """
        if start == destination:
            return 0
        elif start > destination:
            return min(sum(distance[destination:start]), sum(distance[start:]) + sum(distance[:destination]))
        else:
            return min(sum(distance[start:destination]), sum(distance[destination:]) + sum(distance[:start]))
