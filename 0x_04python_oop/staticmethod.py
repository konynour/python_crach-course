class MathOperations:
    @staticmethod
    def add(a, b):  # Static method
        return a + b

    @staticmethod
    def subtract(a, b):  # Static method
        return a - b

# Static methods are called on the class itself
print(MathOperations.add(5, 3))        
print(MathOperations.subtract(10, 4))  

