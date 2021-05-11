from math import pi

class Cylinder:
    
    def __init__(self, height=1, radius=1):
        self.height = height
        self.radius = radius

    def volume(self):
        return pi * (self.radius ** 2) * self.height

    def surface_area(self):
        # 2.pi.r.(r + h)
        return 2 * pi * self.radius * (self.radius + self.height)

c = Cylinder(2, 3)
print(f'Volume = {c.volume():.2f}')
print(f'Área da superfície: {c.surface_area():.1f}')