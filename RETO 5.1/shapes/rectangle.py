from .base_shape import Shape
from .point import Point
from .line import Line

class Rectangle(Shape):
    def __init__(self, width=0, height=0):
        super().__init__(is_regular=True)
        self.width = width
        self.height = height
        self.vertices = self.compute_vertices()
        self.edges = self.compute_edges()

    def compute_area(self):
        return self.width * self.height

    def compute_perimeter(self):
        return 2 * (self.width + self.height)

    def compute_vertices(self):
        return [Point(0, 0), Point(self.width, 0), Point(self.width, self.height), Point(0, self.height)]

    def compute_inner_angles(self):
        return [90, 90, 90, 90]

    def compute_edges(self):
        vertices = self.compute_vertices()
        edges = []
        for i in range(4):
            edges.append(Line(vertices[i], vertices[(i + 1) % 4]))
        return edges
