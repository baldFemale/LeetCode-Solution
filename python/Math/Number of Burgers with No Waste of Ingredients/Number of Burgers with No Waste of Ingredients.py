class Solution:
    def numOfBurgers(self, tomatoSlices: int, cheeseSlices: int) -> List[int]:
        x = tomatoSlices - 2 * cheeseSlices

        if x < 0 or x % 2 == 1:
            return []

        else:
            x = x // 2
            y = cheeseSlices - x
            if x >= 0 and y >= 0:
                return [x, y]
            else:
                return []