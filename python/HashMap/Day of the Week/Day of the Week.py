class Solution(object):
    def dayOfTheWeek(self, day, month, year):
        """
        :type day: int
        :type month: int
        :type year: int
        :rtype: str
        """
        # 1997/1/1 Friday

        s = set([i for i in range(1971, 2101) if i % 4 == 0])
        s.remove(2100)

        months = {
            1: 31,
            2: 28,
            3: 31,
            4: 30,
            5: 31,
            6: 30,
            7: 31,
            8: 31,
            9: 30,
            10: 31,
            11: 30,
            12: 31
        }

        days = -1

        for i in range(1, month):
            days += months[i]
        y = year - 1971
        days += y * 365

        days += day

        for i in s:
            if i < year:
                days += 1
            if i == year and month > 2:
                days += 1

        days = days % 7

        res = {
            6: "Thursday",
            0: "Friday",
            1: "Saturday",
            2: "Sunday",
            3: "Monday",
            4: "Tuesday",
            5: "Wednesday"
        }
        return res[days]
