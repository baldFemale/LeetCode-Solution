from collections import Counter

class Solution:
    def maxRepOpt1(self, text):
        c = Counter(text)
        res = 0
        for i in range(len(text)):
            j = i
            current = text[i]
            diff = 0
            count = 0
            while j<len(text) and (diff==0 or current==text[j]) and count<c[current]:
                if current!=text[j]:
                    diff+=1
                count+=1
                j+=1
            res = max(res,count)
        return res
