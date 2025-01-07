from .rectangle import Rectangle

class Square(Rectangle):
    def __init__(self, side=0):
        super().__init__(width=side, height=side)
        self.is_regular = True
