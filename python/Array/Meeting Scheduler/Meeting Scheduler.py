class Solution(object):
    def minAvailableDuration(self, slots1, slots2, duration):
        """
        :type slots1: List[List[int]]
        :type slots2: List[List[int]]
        :type duration: int
        :rtype: List[int]
        """
        slots1.sort(key=lambda x: x[0])
        slots2.sort(key=lambda x: x[0])
        i = 0
        j = 0

        while i < len(slots1) and j < len(slots2):

            if slots1[i][0] + duration > slots1[i][1] and i + 1 < len(slots1):
                i += 1
            if slots2[j][0] + duration > slots2[j][1] and j + 1 < len(slots2):
                j += 1

            if i < len(slots1) and j < len(slots2):
                if slots1[i][0] < slots2[j][0]:
                    if slots2[j][0] + duration <= min(slots1[i][1], slots2[j][1]):
                        return [slots2[j][0], slots2[j][0] + duration]
                    else:
                        i += 1
                else:
                    if slots1[i][0] + duration <= min(slots1[i][1], slots2[j][1]):
                        return [slots1[i][0], slots1[i][0] + duration]
                    else:
                        j += 1
        return []
