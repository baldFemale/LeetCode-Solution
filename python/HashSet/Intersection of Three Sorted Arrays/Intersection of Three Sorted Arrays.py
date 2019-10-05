class Solution(object):
    def arraysIntersection(self, arr1, arr2, arr3):
        """
        :type arr1: List[int]
        :type arr2: List[int]
        :type arr3: List[int]
        :rtype: List[int]
        """
        s1 = set(arr1)
        s2 = set(arr2)
        s3 = set(arr3)

        s = s1 & s2 & s3
        return sorted(list(s))
