

class Solution(object):
    def smallestSufficientTeam(self, req_skills, people):
        """
        :type req_skills: List[str]
        :type people: List[List[str]]
        :rtype: List[int]
        """
        n, m = len(req_skills), len(people)

        key = {i: j for j, i in enumerate(req_skills)}
        dp = {0: []}

        for i, p in enumerate(people):
            his_skill = 0
            for sk in p:
                if sk in key:
                    his_skill |= 1 << key[sk]

            for skill_set, need in dp.items():
                with_him = skill_set | his_skill
                if with_him == skill_set:
                    continue
                if with_him not in dp or len(dp[with_him]) > len(need) + 1:
                    dp[with_him] = need + [i]
        return dp[(1 << n) - 1]
