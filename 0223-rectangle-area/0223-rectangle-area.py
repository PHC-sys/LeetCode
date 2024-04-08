class Solution:
    def computeArea(self, ax1: int, ay1: int, ax2: int, ay2: int, bx1: int, by1: int, bx2: int, by2: int) -> int:
        x1, x2, x3 = abs(ax1 - ax2), abs(bx1 -bx2), max(ax1, ax2, bx1, bx2) - min(ax1, ax2, bx1, bx2) 
        y1, y2, y3 = abs(ay1 - ay2), abs(by1 - by2), max(ay1, ay2, by1, by2) - min(ay1, ay2, by1, by2)
        if x3 < x1 + x2 and y3 < y1 + y2: intrs = (x1 + x2 - x3) * (y1 + y2 - y3) 
        else: intrs = 0
        return x1 * y1 + x2 * y2 - intrs