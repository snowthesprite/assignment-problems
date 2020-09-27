import math
import matplotlib.pyplot as plt

class Rectangle :
    def __init__(self, base, height, color) :
        self.base = base
        self.height = height
        self.color = color
        self.perimeter = 2 * self.base + 2 * self.height
        self.area = self.base * self.height
        self.vertices = [(0, 0), (self.base, 0), (self.base, self.height), (0, self.height)]

    def describe(self) :
        print('Base: {}'.format(self.base))
        print('Height: {}'.format(self.height))
        print('Color: {}'.format(self.color))
        print('Perimeter: {}'.format(self.perimeter))
        print('Area: {}'.format(self.area))
        print('Vertices: {}'.format(self.vertices))

    def render(self) : 
        plt.style.use('bmh')
        x_points = [x[0] for x in self.vertices]
        y_points = [y[1] for y in self.vertices]
        x_points.append(0)
        y_points.append(0)
        plt.gca().set_aspect("equal")
        plt.plot(x_points,y_points, self.color)
        plt.savefig('Assignment_13/squareplot.png')
        plt.clf()

class RightTriangle :
    def __init__(self, base, height, color) :
        self.base = base
        self.height = height
        self.color = color
        self.perimeter = self.base + self.height + (math.sqrt(self.base ** 2 + self.height ** 2))
        self.area = (self.base * self.height) / 2
        self.vertices = [(0, 0), (self.base, 0), (0, self.height)]

    def describe(self) :
        print('Base: {}'.format(self.base))
        print('Height: {}'.format(self.height))
        print('Color: {}'.format(self.color))
        print('Perimeter: {}'.format(self.perimeter))
        print('Area: {}'.format(self.area))
        print('Vertices: {}'.format(self.vertices))

    def render(self) : 
        plt.style.use('bmh')
        x_points = [x[0] for x in self.vertices]
        y_points = [y[1] for y in self.vertices]
        x_points.append(0)
        y_points.append(0)
        plt.gca().set_aspect("equal")
        plt.plot(x_points,y_points, self.color)
        plt.savefig('Assignment_12/triangleplot.png')
        plt.clf()


class Square(Rectangle):
    def __init__(self, sides, color) :
        super().__init__(sides, sides, color)
