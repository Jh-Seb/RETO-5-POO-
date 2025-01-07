import math
from .base_shape import Shape
from .point import Point
from .line import Line

class Triangle(Shape):
    def __init__(self, base=0, height=0, side1=0, side2=0, side3=0):
        super().__init__(is_regular=False)
        self.base = base
        self.height = height
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3
        self.vertices = self.compute_vertices()
        self.edges = self.compute_edges()

    def compute_area(self):
        return 0.5 * self.base * self.height

    def compute_perimeter(self):
        return self.side1 + self.side2 + self.side3

    def compute_vertices(self):
        return [Point(0, 0), Point(self.base, 0), Point(self.base / 2, self.height)]

    def compute_edges(self):
        vertices = self.compute_vertices()
        edges = []
        for i in range(3):
            edges.append(Line(vertices[i], vertices[(i + 1) % 3]))
        return edges

    def compute_inner_angles(self):
        a, b, c = self.side1, self.side2, self.side3
        angle_A = math.degrees(math.acos((b**2 + c**2 - a**2) / (2 * b * c)))
        angle_B = math.degrees(math.acos((a**2 + c**2 - b**2) / (2 * a * c)))
        angle_C = 180 - angle_A - angle_B
        return [angle_A, angle_B, angle_C]
