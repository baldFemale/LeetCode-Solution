class Solution(object):
    def dietPlanPerformance(self, calories, k, lower, upper):
        """
        :type calories: List[int]
        :type k: int
        :type lower: int
        :type upper: int
        :rtype: int
        """
        n = len(calories)
        temp = []
        cur = sum(calories[0:k-1])
        for i in range(0,n-k+1):
            cur+=calories[i+k-1]
            temp.append(cur)
            cur-=calories[i]
        res = 0
        for i in temp:
            if i>upper:
                res+=1
            elif i<lower:
                res-=1
        return res
