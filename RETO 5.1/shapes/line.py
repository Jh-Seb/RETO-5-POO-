from .point import Point

class Line:
    def __init__(self, start: Point = Point(), end: Point = Point()):
        self.start = start
        self.end = end
        self.length = self.compute_length()

    def compute_length(self):
        return ((self.start.x - self.end.x)**2 + (self.start.y - self.end.y)**2)**0.5
