from abc import ABC, abstractmethod

class Shape(ABC): 
    @abstractmethod
    def area(self):  #  Method name should be lowercase "self", not "Self"
        pass

class Circle(Shape):  #class name capitalization
    def __init__(self, radius):  # parameter name  "radius"
        self.radius = radius

    def area(self):  
        return 3.14 * self.radius ** 2

class Square(Shape):  
    def __init__(self, side): # Constructor name should be "__init__"
        self.side = side

    def area(self):  
        return self.side ** 2

class Triangle(Shape):  
    def __init__(self, base, height): 
        self.base = base
        self.height = height

    def area(self):  
        return 0.5 * self.base * self.height

# Create a list of shapes
shapes = [Circle(4), Square(5), Triangle(7, 6)]

# Print areas of shapes
for shape in shapes:
    print(f"{shape.area()} cm²")
