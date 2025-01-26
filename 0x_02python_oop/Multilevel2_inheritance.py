
class Shape:
    def __init__(self, color, is_filled):
        self.color = color
        self.is_filled = is_filled

class Circle(Shape):
    def __init__(self, color, is_filled, radius):
        super().__init__(color, is_filled)
        self.radius = radius

class Square(Shape):
    def __init__(self, color, is_filled, width):
        super().__init__(color, is_filled)
        self.width = width

class Triangle(Shape):
    def __init__(self, color, is_filled, base, height):
        super().__init__(color, is_filled)
        self.base = base
        self.height = height

# Create instances of Square and Circle
square = Square(color="red", is_filled=True, width=5)
circle = Circle(color="blue", is_filled=True, radius=10)

# Print properties of square and circle
print(square.color)      
print(circle.color)      
print(square.width)      
print(circle.radius)     
print(square.is_filled) 
print(circle.is_filled)  
