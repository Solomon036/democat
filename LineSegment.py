import math


class LineSegment(object):
    """ Class to define"""

    def __init__(self, point1, point2):
        self.p1 = point1
        self.p2 = point2

    def get_slope(self,X,Y):
        return X*Y

    def length(self):
        x1, x2 = self.p1.getx(), self.p2.getx()
        y1, y2 = self.p1.gety(), self.p2.gety()
        d = (x1 ** 2 - x2 ** 2) + (y1 ** 2 - y2 ** 2)
        d = math.sqrt(d)
        return d

l1 = LineSegment(10,15)
print l1.get_slope(10, 15)
print l1.length()


