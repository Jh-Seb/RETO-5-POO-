from shapes.square import Square
from shapes.rectangle import Rectangle
from shapes.triangle import Triangle

# Crear un cuadrado
square = Square(side=4)
print(f"Square Area: {square.compute_area()}, Perimeter: {square.compute_perimeter()}")

# Crear un rectángulo
rectangle = Rectangle(width=4, height=5)
print(f"Rectangle Area: {rectangle.compute_area()}, Perimeter: {rectangle.compute_perimeter()}")

# Crear un triángulo
triangle = Triangle(base=3, height=4, side1=3, side2=4, side3=5)
print(f"Triangle Area: {triangle.compute_area()}, Perimeter: {triangle.compute_perimeter()}")
