class Shape:
    def __init__(self, is_regular: bool = False, vertices: list = [], edges: list = [], inner_angles: list = []):
        self.is_regular = is_regular
        self.vertices = vertices
        self.edges = edges
        self.inner_angles = inner_angles

    def compute_area(self):
        pass

    def compute_perimeter(self):
        pass

    def compute_inner_angles(self):
        pass
