class Solution(object):
    def relativeSortArray(self, arr1, arr2):
        """
        :type arr1: List[int]
        :type arr2: List[int]
        :rtype: List[int]
        """
        dic = {arr2[i]: i for i in range(len(arr2))}

        return sorted(arr1, key=lambda x: dic.get(x, 1000 + x))