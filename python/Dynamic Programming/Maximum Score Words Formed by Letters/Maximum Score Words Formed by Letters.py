class Solution(object):
    def maxScoreWords(self, words, letters, score):
        """
        :type words: List[str]
        :type letters: List[str]
        :type score: List[int]
        :rtype: int
        """

        def check(word, state):
            for j in word:
                state[ord(j) - ord("a")] -= 1
                if state[ord(j) - ord("a")] < 0:
                    return False, None
            return True, state

        def get_score(word):
            res = 0
            for j in word:
                res += score[ord(j) - ord("a")]
            return res

        state = [0 for i in range(26)]
        for i in letters:
            state[ord(i) - ord("a")] += 1

        word_index = [1 for i in range(len(words))]
        cache = {}

        def dp(state, word_index):
            if tuple(state + word_index) in cache:
                return cache[tuple(state + word_index)]
            res = 0
            for i, w in enumerate(word_index):
                if w == 1:
                    tag, temp_state = check(words[i], list(state))
                    if tag == True:
                        res = max(res, get_score(words[i]) + dp(temp_state, word_index[:i] + [0] + word_index[i + 1:]))
            cache[tuple(state + word_index)] = res
            return res

        return dp(state, word_index)
