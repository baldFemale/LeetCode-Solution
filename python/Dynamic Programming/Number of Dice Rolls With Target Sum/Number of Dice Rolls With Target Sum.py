class Solution(object):
    def numRollsToTarget(self, d, f, target):
        """
        :type d: int
        :type f: int
        :type target: int
        :rtype: int
        """
        self.cache = {}
        def dp(d,target):
            if (d,target) in self.cache:
                return self.cache[(d,target)]
            if target>d*f or target<d:
                self.cache[(d,target)] = 0
                return 0
            if d==1 and f>=target:
                self.cache[(d,target)] = 1
                return 1
            else:
                s = 0
                for i in range(1,f+1):
                    s+=dp(d-1,target-i)
                self.cache[(d,target)] = s
                return s
        return dp(d,target)%(10**9+7)
