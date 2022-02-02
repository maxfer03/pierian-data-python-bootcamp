# Fill in the Line class methods to accept coordinates 
# as a pair of tuples and return the slope and distance of the line.

from cmath import sqrt


class Line:
    
    def __init__(self,coor1,coor2):
        self.coor1 = coor1
        self.coor2 = coor2
    
    def distance(self):
        # formula:
        # √[(x₂ - x₁)² + (y₂ - y₁)²]
        calc = (self.coor2[0] - self.coor1[0])**2 + (self.coor2[1] - self.coor1[1])**2
        calc = calc**(1/2)
        return calc
    
    def slope(self):
        # formula:
        # (y2-y1)/(x2-x1)
        calc = (self.coor2[1] - self.coor1[1])/(self.coor2[0] - self.coor1[0])
        return calc


coordinate1 = (3,2)
coordinate2 = (8,10)

li = Line(coordinate1,coordinate2)

print('distance:', li.distance()) # should return 9.433981132056603
print('slope:   ',li.slope())     # shoud return 1.6
