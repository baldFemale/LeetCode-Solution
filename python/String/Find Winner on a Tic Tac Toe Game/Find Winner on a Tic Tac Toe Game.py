class Solution:
    def tictactoe(self, moves: List[List[int]]) -> str:
        chess = [[0 for i in range(3)] for j in range(3)]

        for i, move in enumerate(moves):
            if i % 2 == 0:
                chess[move[0]][move[1]] = 1
            else:
                chess[move[0]][move[1]] = 2

        for i in range(3):
            if chess[i] == [1, 1, 1]:
                return "A"
            if chess[i] == [2, 2, 2]:
                return "B"
            if [chess[0][i], chess[1][i], chess[2][i]] == [1, 1, 1]:
                return "A"
            if [chess[0][i], chess[1][i], chess[2][i]] == [2, 2, 2]:
                return "B"
            if [chess[0][0], chess[1][1], chess[2][2]] == [1, 1, 1]:
                return "A"
            if [chess[0][0], chess[1][1], chess[2][2]] == [2, 2, 2]:
                return "B"
            if [chess[0][2], chess[1][1], chess[2][0]] == [1, 1, 1]:
                return "A"
            if [chess[0][2], chess[1][1], chess[2][0]] == [2, 2, 2]:
                return "B"
        if sum([sum(i) for i in chess]) == 13:
            return "Draw"

        return "Pending"

