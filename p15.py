
from abc import ABC, abstractmethod
import math


# Abstract base class
class Shape(ABC):

    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def __str__(self):
        pass


# Vector class with operator overloading
class Vector(Shape):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def area(self):
        return 0  # A vector has no geometric area

    def __add__(self, other):
        if not isinstance(other, Vector):
            return NotImplemented
        return Vector(self.x + other.x, self.y + other.y)

    def __eq__(self, other):
        if not isinstance(other, Vector):
            return NotImplemented
        return self.x == other.x and self.y == other.y

    def __lt__(self, other):
        if not isinstance(other, Vector):
            return NotImplemented
        return self.magnitude() < other.magnitude()

    def magnitude(self):
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def __str__(self):
        return f"Vector({self.x}, {self.y})"


# Circle class implementing the abstract contract
class Circle(Shape):
    def __init__(self, radius):
        if radius < 0:
            raise ValueError("Radius cannot be negative")
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

    def __eq__(self, other):
        if not isinstance(other, Circle):
            return NotImplemented
        return self.radius == other.radius

    def __lt__(self, other):
        if not isinstance(other, Circle):
            return NotImplemented
        return self.area() < other.area()

    def __str__(self):
        return f"Circle(radius={self.radius})"


if __name__ == "__main__":
    print("=" * 45)
    print("       ABSTRACT SHAPE MATH ENGINE")
    print("=" * 45)

    # Vector operations
    v1 = Vector(3, 4)
    v2 = Vector(1, 2)
    v3 = Vector(3, 4)

    print("\n--- Vector Operations ---")
    print("Vector 1:", v1)
    print("Vector 2:", v2)
    print("Addition:", v1 + v2)
    print("Magnitude of Vector 1:", v1.magnitude())
    print("Are v1 and v3 equal?", v1 == v3)
    print("Is v2 smaller than v1?", v2 < v1)

    # Circle operations
    c1 = Circle(3)
    c2 = Circle(5)
    c3 = Circle(3)

    print("\n--- Circle Operations ---")
    print("Circle 1:", c1)
    print("Circle 2:", c2)
    print(f"Area of Circle 1: {c1.area():.2f}")
    print(f"Area of Circle 2: {c2.area():.2f}")
    print("Are c1 and c3 equal?", c1 == c3)
    print("Is Circle 1 smaller than Circle 2?", c1 < c2)

    # Polymorphism
    print("\n--- Polymorphic Area Calculation ---")
    shapes = [v1, c1, c2]

    for shape in shapes:
        print(f"{shape}: Area = {shape.area():.2f}")
