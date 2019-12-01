class Solution:
    def toHexspeak(self, num: str) -> str:
        h = hex(int(num))[2:]
        temp = []
        for i in h:
            if i=="0":
                temp.append("O")
            elif i=="1":
                temp.append("I")
            else:
                temp.append(i.upper())
        for i in temp:
            if i not in {"A", "B", "C", "D", "E", "F", "I", "O"}:
                return "ERROR"
        return "".join(temp)