import bisect


class Solution(object):
    def countSteppingNumbers(self, low, high):
        """
        :type low: int
        :type high: int
        :rtype: List[int]
        """
        s = set([i for i in range(10)])

        dic = {}
        dic[0] = s

        # print(s)

        for i in range(10):
            temp = set()
            for j in dic[i]:
                if j == 0:
                    continue
                last = j % 10
                if last > 0:
                    temp.add(j * 10 + last - 1)
                if last < 9:
                    temp.add(j * 10 + last + 1)

                first = j // (10 ** (i))
                if first > 1:
                    temp.add((first - 1) * (10 ** (i + 1)) + j)
                if first < 9:
                    temp.add((first + 1) * (10 ** (i + 1)) + j)
            dic[i + 1] = temp
            # print(temp)

        temp = []
        for i in dic.values():
            temp += list(i)
        temp.sort()
        left = bisect.bisect_left(temp, low)
        right = bisect.bisect_right(temp, high)
        return temp[left:right]
