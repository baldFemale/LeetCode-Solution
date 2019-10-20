class Solution(object):
    def balancedString(self, s):
        """
        :type s: str
        :rtype: int
        """
        freq = {ch: 0 for ch in 'QWER'}
        for ch in s:
            freq[ch] += 1
        desired_len = int(len(s) / 4)
        fixes = {ch: -desired_len + freq[ch] if desired_len - freq[ch] < 0 else 0 for ch in 'QWER'}


        i = 0
        j = 0
        res = len(s)

        dic = {ch: 0 for ch in 'QWER'}
        while i < len(s) and j < len(s):
            for k in dic.keys():
                while j < len(s) and dic[k] < fixes[k]:
                    dic[s[j]] += 1
                    j += 1
            if j != len(s) or (j == len(s) and dic[s[j - 1]] == fixes[s[j - 1]]):
                while i < len(s) and dic[s[i]] > fixes[s[i]]:
                    dic[s[i]] -= 1
                    i += 1
                print(i, j)
                res = min(res, j - i)
                dic[s[i]] -= 1
                i += 1

        return res
