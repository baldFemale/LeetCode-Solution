class Solution(object):
    def invalidTransactions(self, transactions):
        """
        :type transactions: List[str]
        :rtype: List[str]
        """
        res = []
        for i in range(len(transactions)):
            tran = transactions[i].split(",")
            if int(tran[2]) > 1000:
                res.append(transactions[i])
                continue
            for j in range(len(transactions)):
                if i == j:
                    continue
                tran2 = transactions[j].split(",")
                if tran2[0] == tran[0] and (int(tran2[1]) - 60 <= int(tran[1]) <= int(tran2[1]) + 60) and tran[3] != \
                        tran2[3]:
                    res.append(transactions[i])
                    print(transactions[i])
                    break
        return res
