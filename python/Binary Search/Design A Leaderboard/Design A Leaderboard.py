import bisect


class Leaderboard(object):

    def __init__(self):
        self.dic = {}
        self.scores = []

    def addScore(self, playerId, score):
        """
        :type playerId: int
        :type score: int
        :rtype: None
        """
        if playerId not in self.dic:
            self.dic[playerId] = score
            index = bisect.bisect_left(self.scores, score)
            self.scores = self.scores[:index] + [score] + self.scores[index:]
        else:
            s = self.dic[playerId]
            index = bisect.bisect_left(self.scores, s)
            self.scores = self.scores[:index] + self.scores[index + 1:]

            self.dic[playerId] = score + s
            index = bisect.bisect_left(self.scores, score + s)
            self.scores = self.scores[:index] + [score + s] + self.scores[index:]
            # print(self.scores)
        # print(self.dic)

    def top(self, K):
        """
        :type K: int
        :rtype: int
        """
        # print(self.scores)
        # print(self.scores[::-1][:K])
        # print(self.dic)
        return sum(self.scores[::-1][:K])

    def reset(self, playerId):
        """
        :type playerId: int
        :rtype: None
        """
        s = self.dic[playerId]
        del (self.dic[playerId])

        index = bisect.bisect_left(self.scores, s)
        self.scores = self.scores[:index] + self.scores[index + 1:]
        # print(self.scores)
        # print(self.dic)

# Your Leaderboard object will be instantiated and called as such:
# obj = Leaderboard()
# obj.addScore(playerId,score)
# param_2 = obj.top(K)
# obj.reset(playerId)