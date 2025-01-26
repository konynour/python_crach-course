from abc import ABC, abstractmethod

class Shape(ABC): 
    @abstractmethod
    def area(self):  
        pass

    @abstractmethod
    def parameter(self): 
        pass

class Squara(Shape):
    def __init__(self, side):
        self.__side = side

    def area(self):
        return self.__side * self.__side

    def parameter(self):
        return 4 * self.__side

class Rect(Shape):
    def __init__(self, length, width):
        self.__length = length
        self.__width = width

    def area(self):
        return self.__length * self.__width

    def parameter(self):
        return 2 * (self.__length + self.__width)

# Creating instances and printing results
squara = Squara(10)
print(f"Squara area is {squara.area()} and parameter is {squara.parameter()}")

rect = Rect(10, 5)
print(f"Rect area is {rect.area()} and parameter is {rect.parameter()}")
print("-----------------------------------------------------------------------------------------------------")
        


