class Solution(object):
    def checkStraightLine(self, coordinates):
        """
        :type coordinates: List[List[int]]
        :rtype: bool
        """
        coordinates.sort(key=lambda x: x[0])

        dif_x, dif_y = coordinates[1][0] - coordinates[0][0], coordinates[1][1] - coordinates[0][1]

        for i in range(2, len(coordinates)):
            if (coordinates[i][0] - coordinates[i - 1][0]) * dif_y != (
                    coordinates[i][1] - coordinates[i - 1][1]) * dif_x:
                return False
        return True
