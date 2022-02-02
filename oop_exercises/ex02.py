from cmath import pi


class Cylinder:
    
    def __init__(self,height=1,radius=1):
        self.height = height
        self.radius = radius
        pass
        
    def volume(self):
        # formula:
        # h*π*r^2
        return self.height * pi * (self.radius**2)
    
    def surface_area(self):
        # formulas:
        # L = 2 * π * r * h
        # T = B = π * r^2
        # total = L + T + B = 2 * π * r * h + 2(π * r^2) = 2 * π * r * (h + r)
        lateral_area = 2 * pi * self.radius * self.height
        top_bottom_area = (pi * (self.radius**2)) * 2
        return top_bottom_area + lateral_area


c = Cylinder(2,3)


print(c.volume())       # 56.548667764616276
print(c.surface_area()) # 94.24777960769379
