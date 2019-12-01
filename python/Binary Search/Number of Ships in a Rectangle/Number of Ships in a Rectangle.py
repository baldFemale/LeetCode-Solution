# """
# This is Sea's API interface.
# You should not implement it, or speculate about its implementation
# """
class Sea(object):
   def hasShips(self, topRight: 'Point', bottomLeft: 'Point') -> bool:

class Point(object):
	def __init__(self, x: int, y: int):
		self.x = x
		self.y = y

class Solution(object):
    def countShips(self, sea: 'Sea', topRight: 'Point', bottomLeft: 'Point') -> int:
        # print(topRight.x,topRight.y,bottomLeft.x,bottomLeft.y)
        if topRight.x < bottomLeft.x or topRight.y < bottomLeft.y or (not sea.hasShips(topRight, bottomLeft)):
            return 0
        elif topRight.x == bottomLeft.x and topRight.y == bottomLeft.y:
            return 1
        else:
            mid_x = (topRight.x + bottomLeft.x) // 2
            mid_y = (topRight.y + bottomLeft.y) // 2
            return self.countShips(sea, Point(mid_x, mid_y), bottomLeft) + self.countShips(sea,
                                                                                           Point(topRight.x, mid_y),
                                                                                           Point(mid_x + 1,
                                                                                                 bottomLeft.y)) + self.countShips(
                sea, topRight, Point(mid_x + 1, mid_y + 1)) + self.countShips(sea, Point(mid_x, topRight.y),
                                                                              Point(bottomLeft.x, mid_y + 1))


